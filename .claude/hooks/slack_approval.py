#!/usr/bin/env python3
"""
Claude Code PreToolUse hook — Slack-based approval via emoji reactions.

Flow:
  1. Read the tool payload from stdin (JSON injected by Claude Code).
  2. Fast-approve commands that match SAFE_PATTERNS (no Slack DM sent).
  3. For everything else: post a DM to the approver, poll for a ✅/❌ reaction.
  4. Approved  → stdout {"decision":"allow"},  exit 0
     Denied    → stdout {"decision":"deny"…},  exit 2
     Timeout   → stdout {"decision":"deny"…},  exit 2
  5. If SLACK_BOT_TOKEN is unset, exit 0 silently (fall through to Claude Code's own prompt).

Environment variables (set in shell profile or .claude/settings.local.json → env block):
  SLACK_BOT_TOKEN              required  xoxb-… bot token with reactions:read, reactions:write, chat:write
  SLACK_APPROVER_USER_ID       optional  Slack user-id to DM (default: U07SX2XTY86)
  SLACK_APPROVAL_TIMEOUT_SECONDS optional  seconds to wait (default: 120)
  APPROVE_REACTION             optional  emoji name for approval    (default: white_check_mark)
  DENY_REACTION                optional  emoji name for denial      (default: x)
"""

import sys
import json
import os
import re
import time
import urllib.request
import urllib.error
import hashlib
import datetime

# ──────────────────────────────────────────────────────────────────────────────
# Config
# ──────────────────────────────────────────────────────────────────────────────
SLACK_BOT_TOKEN        = os.environ.get("SLACK_BOT_TOKEN", "")
SLACK_APPROVER_USER_ID = os.environ.get("SLACK_APPROVER_USER_ID", "U07SX2XTY86")
SLACK_APPROVAL_TIMEOUT = int(os.environ.get("SLACK_APPROVAL_TIMEOUT_SECONDS", "120"))
APPROVE_REACTION       = os.environ.get("APPROVE_REACTION", "white_check_mark")
DENY_REACTION          = os.environ.get("DENY_REACTION", "x")
POLL_INTERVAL          = 3   # seconds between reaction checks
DRY_RUN                = "--dry-run" in sys.argv  # test mode: no real Slack calls

# ──────────────────────────────────────────────────────────────────────────────
# Known-safe Bash command patterns — these auto-approve without a Slack DM.
# Mirror the allow list in .claude/settings.json so already-whitelisted commands
# are handled instantly by the hook rather than causing a second approval step.
# ──────────────────────────────────────────────────────────────────────────────
SAFE_PATTERNS = [
    # git read operations
    r"^git\s+(status|diff|log|show|remote|config|stash\s+list|branch|fetch|tag|rev-parse|ls-files|ls-remote)\b",
    r"^git\s+(pull|fetch)\b",
    r"^git\s+add\b",
    r"^git\s+commit\b",
    r"^git\s+stash\b",
    # git push — safe: push to origin HEAD or develop, NOT force
    r"^git\s+push\s+origin\s+HEAD(\s|$)",
    r"^git\s+push\s+origin\s+develop(\s|$)",
    # gh CLI — read operations and PR management (non-destructive)
    r"^(~/.local/bin/)?gh\s+pr\s+(create|view|list|comment|checks|status)\b",
    r"^(~/.local/bin/)?gh\s+api\s+repos/",
    r"^(~/.local/bin/)?gh\s+auth\s+status\b",
    # filesystem reads
    r"^(find|grep|ls|cat|head|tail|wc|xxd|md5|shasum|stat)\b",
    # computation
    r"^node\s+(--check|--input-type|-e)\b",
    r"^python3\s+-c\b",
    r"^npx\s+--yes\s+acorn\b",
    # directory / file ops — low risk
    r"^mkdir\b",
    r"^cp\b",
    r"^chmod\b",
    r"^unzip\b",
    # shell utilities
    r"^(echo|printf|date|which|type|env|printenv|pwd|id)\b",
    r"^(sleep|true|false)\b",
    r"^(open|code|pbcopy|pbpaste)\b",
    # process inspection (read-only)
    r"^(ps|top|htop|lsof|pgrep)\b",
]

# ──────────────────────────────────────────────────────────────────────────────
# Known-risky patterns — always labelled HIGH RISK in the Slack message.
# ──────────────────────────────────────────────────────────────────────────────
RISKY_PATTERNS = [
    (r"\brm\s",                      "rm — file deletion"),
    (r"\brmdir\b",                   "rmdir — directory deletion"),
    (r"git\s+push\s+.*--force",      "git push --force"),
    (r"git\s+push\s+.*-f\b",        "git push -f"),
    (r"git\s+reset\s+.*--hard",      "git reset --hard"),
    (r"git\s+reset\s+HEAD~",         "git reset HEAD~"),
    (r"git\s+checkout\s+--\s",       "git checkout -- (discard changes)"),
    (r"git\s+restore\s+\.",          "git restore . (discard all)"),
    (r"git\s+clean\s+.*-f",         "git clean -f (delete untracked)"),
    (r"\bsudo\b",                    "sudo — elevated privileges"),
    (r"\bkill\b",                    "kill — terminate process"),
    (r"\bpkill\b",                   "pkill — pattern-kill processes"),
    (r"\bDROP\s+TABLE\b",            "DROP TABLE — destructive SQL"),
    (r"\bTRUNCATE\b",                "TRUNCATE — destructive SQL"),
    (r"\|\s*(sh|bash|zsh)\b",        "pipe to shell — remote code exec risk"),
    (r">\s*/etc/",                   "write to /etc/"),
    (r">\s*/usr/",                   "write to /usr/"),
    (r"curl\s+.*\|\s*(sh|bash)",     "curl | shell — remote code exec"),
    (r"wget\s+.*\|\s*(sh|bash)",     "wget | shell — remote code exec"),
    (r"\bchown\b",                   "chown — ownership change"),
    (r"\bchmod\s+777\b",             "chmod 777 — world-writable"),
    (r"\bmv\b.*\s/",                 "mv — moving files (possibly to /"),
    # find with action flags that modify/delete files or execute commands
    (r"\bfind\b.*\s-delete\b",       "find -delete — filesystem deletion"),
    (r"\bfind\b.*\s-exec\b",         "find -exec — arbitrary command execution"),
    (r"\bfind\b.*\s-execdir\b",      "find -execdir — arbitrary command execution"),
    (r"\bfind\b.*\s-ok\b",           "find -ok — interactive command execution"),
    (r"\bfind\b.*\s-okdir\b",        "find -okdir — interactive command execution"),
]


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

# Shell metacharacters that introduce compound/chained commands.
# A command containing any of these cannot be matched as safe by a prefix pattern.
_COMPOUND_RE = re.compile(r"&&|\|\||\||;|`|\$\(", re.MULTILINE)


def is_safe(cmd: str) -> bool:
    if _COMPOUND_RE.search(cmd):
        return False  # compound command — never fast-approve
    for pat in SAFE_PATTERNS:
        if re.match(pat, cmd.strip(), re.IGNORECASE):
            return True
    return False


def risk_info(cmd: str):
    """Returns (is_high_risk: bool, matched_label: str)."""
    for pat, label in RISKY_PATTERNS:
        if re.search(pat, cmd, re.IGNORECASE):
            return True, label
    return False, ""


def truncate(s: str, n: int = 800) -> str:
    return s if len(s) <= n else s[:n] + "\n…(truncated)"


def slack_api(method: str, payload: dict, http_method: str = "POST") -> dict:
    if DRY_RUN:
        print(f"[dry-run] Slack {http_method} {method}: {json.dumps(payload)[:200]}", file=sys.stderr)
        return {"ok": True, "ts": "0000000000.000000", "channel": SLACK_APPROVER_USER_ID,
                "message": {"reactions": []}}
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        f"https://slack.com/api/{method}",
        data=data,
        headers={"Authorization": f"Bearer {SLACK_BOT_TOKEN}", "Content-Type": "application/json"},
        method=http_method,
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read())
    except Exception as exc:
        return {"ok": False, "error": str(exc)}


def slack_get(method: str, params: dict) -> dict:
    if DRY_RUN:
        print(f"[dry-run] Slack GET {method}: {params}", file=sys.stderr)
        return {"ok": True, "message": {"reactions": []}}
    qs = "&".join(f"{k}={urllib.request.quote(str(v))}" for k, v in params.items())
    req = urllib.request.Request(
        f"https://slack.com/api/{method}?{qs}",
        headers={"Authorization": f"Bearer {SLACK_BOT_TOKEN}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read())
    except Exception as exc:
        return {"ok": False, "error": str(exc)}


def allow():
    print(json.dumps({"hookSpecificOutput": {"permissionDecision": "allow"}}))
    sys.exit(0)


def deny(reason: str):
    print(json.dumps({
        "hookSpecificOutput": {"permissionDecision": "deny", "permissionDecisionReason": reason},
    }))
    sys.exit(0)


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────

def main():
    # ── No token → pass through silently ──────────────────────────────────────
    if not SLACK_BOT_TOKEN and not DRY_RUN:
        sys.exit(0)

    # ── Parse stdin ───────────────────────────────────────────────────────────
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)  # malformed — pass through

    tool_name  = payload.get("tool_name", "")
    tool_input = payload.get("tool_input", {})
    session_id = payload.get("session_id", "")
    cwd        = os.getcwd()

    # Extract the human-readable command / file path
    if tool_name == "Bash":
        command = tool_input.get("command", "")
        input_summary = f"`{truncate(command, 600)}`"
    elif tool_name in ("Edit", "Write"):
        fpath = tool_input.get("file_path", "?")
        command = fpath
        input_summary = f"file: `{fpath}`"
    else:
        command = json.dumps(tool_input)
        input_summary = f"```{truncate(command, 300)}```"

    # ── Classify risk first — risky flags (e.g. --force) must not be overridden
    # by a prefix-matching safe pattern (e.g. "git push origin HEAD --force")
    high_risk, risk_label = risk_info(command)

    # ── Fast-approve known-safe Bash commands (only if not high-risk) ──────────
    if not high_risk and tool_name == "Bash" and is_safe(command):
        allow()

    # ── Label for Slack message ───────────────────────────────────────────────
    if high_risk:
        risk_emoji = "⛔"
        risk_text  = f"HIGH — {risk_label}"
    else:
        risk_emoji = "⚠️"
        risk_text  = "UNKNOWN — not in safe list"

    # ── Build a unique approval ID ────────────────────────────────────────────
    uid    = hashlib.sha1(f"{session_id}{command}{time.time()}".encode()).hexdigest()[:8]
    ts_str = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    # ── Compose Slack message ─────────────────────────────────────────────────
    msg = (
        f"{risk_emoji} *Claude Code — approval required* `{uid}`\n"
        f"*Tool:*    `{tool_name}`\n"
        f"*Risk:*    {risk_text}\n"
        f"*Input:*\n{input_summary}\n"
        f"*Dir:*     `{cwd}`\n"
        f"*Session:* `{session_id[:20] if session_id else 'n/a'}`\n"
        f"*Time:*    {ts_str}\n"
        f"\n"
        f"React :{APPROVE_REACTION}: to *approve* or :{DENY_REACTION}: to *deny*.\n"
        f"Auto-deny in *{SLACK_APPROVAL_TIMEOUT}s* if no response."
    )

    # ── Post DM to approver ───────────────────────────────────────────────────
    post_resp = slack_api("chat.postMessage", {
        "channel": SLACK_APPROVER_USER_ID,
        "text": msg,
        "unfurl_links": False,
        "unfurl_media": False,
    })

    if not post_resp.get("ok"):
        err = post_resp.get("error", "unknown")
        # Cannot reach Slack — fall through to Claude Code's own prompt
        sys.stderr.write(f"[slack-approval] chat.postMessage failed: {err}\n")
        sys.exit(0)

    msg_ts   = post_resp["ts"]
    channel  = post_resp["channel"]

    # ── Dry-run: skip real polling — immediately approve so tests are fast ─────
    if DRY_RUN:
        allow()

    # ── Poll for emoji reactions ──────────────────────────────────────────────
    deadline = time.time() + SLACK_APPROVAL_TIMEOUT
    while time.time() < deadline:
        time.sleep(POLL_INTERVAL)

        r = slack_get("reactions.get", {"channel": channel, "timestamp": msg_ts, "full": "true"})
        if not r.get("ok"):
            continue  # transient error — keep polling

        reactions = {rx["name"] for rx in r.get("message", {}).get("reactions", [])}

        if APPROVE_REACTION in reactions:
            # Post a confirmation reply in the DM thread
            slack_api("chat.postMessage", {
                "channel": channel,
                "thread_ts": msg_ts,
                "text": f"✅ *Approved* `{uid}` — proceeding.",
            })
            allow()

        if DENY_REACTION in reactions:
            slack_api("chat.postMessage", {
                "channel": channel,
                "thread_ts": msg_ts,
                "text": f"❌ *Denied* `{uid}` — command blocked.",
            })
            deny(f"Denied via Slack reaction (id:{uid}).")

    # ── Timeout ───────────────────────────────────────────────────────────────
    slack_api("chat.postMessage", {
        "channel": channel,
        "thread_ts": msg_ts,
        "text": f"⏱ *Timed out* `{uid}` — no response in {SLACK_APPROVAL_TIMEOUT}s. Command auto-denied.",
    })
    deny(f"Slack approval timed out after {SLACK_APPROVAL_TIMEOUT}s (id:{uid}). Command was not approved.")


if __name__ == "__main__":
    main()
