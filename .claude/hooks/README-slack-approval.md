# Slack Approval Hook for Claude Code

Routes Claude Code tool-use permission requests to a Slack DM so you can approve or deny commands from Slack — without needing to be at the terminal.

## How it works

```
Claude wants to run a command
        │
        ▼
.claude/hooks/slack-approval.sh
        │
        ├─ Command matches SAFE_PATTERNS? → auto-approve instantly (no Slack DM)
        │
        └─ Otherwise → post Slack DM with tool + command + risk label
                            │
                            ├─ You react ✅  → Claude continues
                            ├─ You react ❌  → Claude sees "Denied via Slack"
                            └─ No reaction within timeout → auto-deny
```

**Approval method:** emoji reactions on the Slack DM message.
- ✅ `:white_check_mark:` → approve
- ❌ `:x:` → deny
- No reaction within timeout → auto-deny (default: 120 seconds)

No public callback URL or web server is needed. The hook polls Slack's `reactions.get` API every 3 seconds.

---

## Requirements

- Python 3.9+ (`python3` on PATH)
- A Slack Bot Token (`xoxb-…`) with these scopes:
  - `chat:write` — post DMs
  - `reactions:read` — read emoji reactions
- The bot must be added to your workspace and able to DM the approver

### Creating a Slack app (one-time setup)

1. Go to https://api.slack.com/apps → **Create New App** → **From scratch**
2. Name it `Claude Code Approvals`, select your workspace
3. Under **OAuth & Permissions → Scopes → Bot Token Scopes**, add:
   - `chat:write`
   - `reactions:read`
4. Click **Install to Workspace**, copy the **Bot User OAuth Token** (`xoxb-…`)
5. Open a DM with the bot in Slack to allow it to DM you (search for the app name)

---

## Setup

### Step 1 — Set environment variables

Add to your shell profile (`~/.zshrc` or `~/.bashrc`):

```bash
export SLACK_BOT_TOKEN="xoxb-your-token-here"
export SLACK_APPROVER_USER_ID="U07SX2XTY86"   # your Slack user ID
export SLACK_APPROVAL_TIMEOUT_SECONDS="120"    # seconds to wait (default: 120)
export APPROVE_REACTION="white_check_mark"     # ✅
export DENY_REACTION="x"                       # ❌
```

Then `source ~/.zshrc` (or restart your terminal).

**Alternative — per-project env in `.claude/settings.local.json`:**

```json
{
  "env": {
    "SLACK_BOT_TOKEN": "xoxb-your-token-here",
    "SLACK_APPROVER_USER_ID": "U07SX2XTY86",
    "SLACK_APPROVAL_TIMEOUT_SECONDS": "120"
  }
}
```

> ⚠️  `settings.local.json` is gitignored — safe for secrets. Never put the token in `settings.json` (which is committed).

### Step 2 — Verify the hook is registered

The hook is already registered in `.claude/settings.json`. Confirm:

```bash
cat .claude/settings.json | python3 -c "import sys,json; d=json.load(sys.stdin); print(list(d.get('hooks',{}).keys()))"
# Expected: ['PreToolUse']
```

---

## Testing

### Dry-run mode (no real Slack calls)

```bash
echo '{"tool_name":"Bash","tool_input":{"command":"rm -rf /tmp/test"},"session_id":"test-123"}' \
  | python3 .claude/hooks/slack_approval.py --dry-run
```

Expected output on stdout:
```json
{"hookSpecificOutput": {"permissionDecision": "allow"}}
```
(after a mocked wait — in dry-run the polling immediately approves to unblock)

### Test: safe command (auto-approved, no Slack DM)

```bash
echo '{"tool_name":"Bash","tool_input":{"command":"git status"},"session_id":"test"}' \
  | python3 .claude/hooks/slack_approval.py --dry-run
# Expected stdout: {"hookSpecificOutput": {"permissionDecision": "allow"}}  — exits immediately
```

### Test: deny response

```bash
# Set env so polling sees an "x" reaction immediately (mocked in dry-run)
echo '{"tool_name":"Bash","tool_input":{"command":"sudo rm -rf /"},"session_id":"test"}' \
  | SLACK_BOT_TOKEN=dry python3 .claude/hooks/slack_approval.py --dry-run
```

### Test: timeout

```bash
echo '{"tool_name":"Bash","tool_input":{"command":"git push --force origin main"},"session_id":"t"}' \
  | SLACK_APPROVAL_TIMEOUT_SECONDS=5 python3 .claude/hooks/slack_approval.py
# No reaction within 5s → stdout {"hookSpecificOutput":{"permissionDecision":"deny","permissionDecisionReason":"…"}}
```

### Test: exit codes

```bash
echo '{"tool_name":"Bash","tool_input":{"command":"git status"},"session_id":"t"}' \
  | python3 .claude/hooks/slack_approval.py; echo "exit: $?"
# Expected: exit: 0

echo '{}' | SLACK_BOT_TOKEN=bad python3 .claude/hooks/slack_approval.py; echo "exit: $?"
# Expected: exit: 0 (malformed/missing token → pass through)
```

---

## What gets sent to Slack

A DM is sent only for commands **not** in the known-safe list. Example:

```
⛔ Claude Code — approval request `a1b2c3d4`
Tool:    `Bash`
Risk:    HIGH — git push --force
Input:   `git push --force origin main`
Dir:     `/Users/you/project`
Session: `abc123def456`
Time:    2026-05-26 11:45:00 UTC

React :white_check_mark: to approve or :x: to deny.
Auto-deny in 120s if no response.
```

---

## Safe-command list (no Slack DM)

These commands auto-approve instantly without sending a Slack message:

| Category | Examples |
|---|---|
| git reads | `git status`, `git diff`, `git log`, `git show` |
| git writes | `git add`, `git commit`, `git push origin HEAD` |
| gh CLI | `gh pr create`, `gh pr view`, `gh api repos/…` |
| filesystem reads | `find`, `grep`, `ls`, `cat`, `head`, `tail` |
| computation | `node -e`, `python3 -c`, `npx --yes acorn` |
| utilities | `mkdir`, `cp`, `chmod`, `echo`, `date` |

Force pushes, `rm`, `sudo`, `git reset --hard`, and pipe-to-shell patterns always route to Slack.

---

## Behavior when `SLACK_BOT_TOKEN` is not set

The hook exits 0 silently, falling through to Claude Code's built-in permission prompt. This means the hook is a no-op when the token is missing — existing behavior is preserved.

---

## Preserving the ship workflow

The `/ship` skill commits, pushes, creates a PR, triggers Codex review, and posts Slack DMs using the **MCP Slack tool** (not this hook). That flow is unaffected because:

- `git add`, `git commit`, `git push origin HEAD` are in SAFE_PATTERNS → auto-approved, no Slack DM
- `gh pr create`, `gh pr comment` are in SAFE_PATTERNS → auto-approved
- The MCP Slack tool calls are not Bash commands → hook does not fire for them
