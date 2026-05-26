# /ship — Commit, PR, Codex review, Slack notify

Full end-to-end workflow for shipping a coding change:

1. Commit all staged (or stageable) changes on the current branch
2. Push the branch to origin
3. Open a PR from the current branch to `main`
4. Trigger Codex review by commenting `@codex review` on the PR
5. Watch for Codex response using the `Monitor` tool (event-driven, not polling)
6. When Codex responds:
   - Surface the full review comment in chat
   - **Always** send a Slack DM to Sandeep Jha (`U07SX2XTY86`) — no critical issues = ✅ style, issues found = ⚠️ style
7. If critical issues are found: fix them, push, re-trigger `@codex review`, re-arm the Monitor — repeat until clean
8. **Any time human input, approval, or a decision is needed** — send a Slack DM to `U07SX2XTY86` describing the situation and the options, do not ask in chat

---

## Step-by-step instructions

### 1 — Commit

- Run `git status` and `git diff` to understand what changed.
- Run `git log --oneline -5` to match the repo's commit message style.
- Stage only the relevant files (never `git add -A` blindly).
- Commit with a concise message following the repo's style, co-authored by Claude:
  ```
  Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
  ```
- If a pre-commit hook fails, fix the issue and create a **new** commit — never amend.

### 2 — Push

```bash
git push origin HEAD
```

### 3 — Create PR to main

Use the `gh` CLI binary at `~/.local/bin/gh`.

```bash
~/.local/bin/gh pr create \
  --title "<concise title under 70 chars>" \
  --body "$(cat <<'EOF'
## Summary
- <bullet points>

## Test plan
- [ ] <checklist>

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)" \
  --base main \
  --head <current-branch>
```

Capture the PR number from the output URL.

### 4 — Trigger Codex

```bash
~/.local/bin/gh pr comment <PR-number> --body "@codex review"
```

### 5 — Watch for Codex response (event-driven, not polling)

Use the `Monitor` tool with `persistent: true`. Do NOT use `ScheduleWakeup` for this — Monitor fires immediately when Codex posts, with no session-restart overhead.

```bash
TARGET_COMMIT="<HEAD-commit-short-sha>"
REVIEW_TRIGGERED_AT=$(date -u +%Y-%m-%dT%H:%M:%SZ)  # anchors thread filter to this review round
while true; do
  # Check 1: formal PR review on the target commit
  REVIEW=$(~/.local/bin/gh api repos/InnoSandeep/<repo>/pulls/<PR-number>/reviews \
    --jq 'sort_by(.submitted_at) | .[-1] | select(.user.login == "chatgpt-codex-connector[bot]") | select(.commit_id | startswith("'"$TARGET_COMMIT"'")) | {commit: .commit_id, submittedAt: .submitted_at}' 2>/dev/null || true)

  # Check 2: free-form PR thread comment — scoped to after this review round was triggered
  THREAD=$(~/.local/bin/gh api repos/InnoSandeep/<repo>/issues/<PR-number>/comments \
    --jq '[.[] | select(.user.login == "chatgpt-codex-connector[bot]") | select(.created_at > "'"$REVIEW_TRIGGERED_AT"'")] | sort_by(.created_at) | .[-1] | {createdAt: .created_at, body: .body}' 2>/dev/null || true)

  if [ -n "$REVIEW" ] || [ -n "$THREAD" ]; then
    INLINE=$(~/.local/bin/gh api repos/InnoSandeep/<repo>/pulls/<PR-number>/comments \
      --jq '[.[] | select(.user.login == "chatgpt-codex-connector[bot]") | select(.commit_id | startswith("'"$TARGET_COMMIT"'"))] | sort_by(.created_at) | .[-1] | {body: .body}' 2>/dev/null || true)
    echo "CODEX_REVIEW_READY|${REVIEW}|${INLINE}|${THREAD}"
    exit 0
  fi
  sleep 30
done
```

- The monitor emits one line (`CODEX_REVIEW_READY|…`) and exits when Codex posts via **either** endpoint
- Codex uses two endpoints depending on context: `/pulls/:id/reviews` for formal reviews with inline suggestions, `/issues/:id/comments` for clean-verdict thread comments — both are checked each iteration
- On `<task-notification>`: parse the emitted line and proceed to Step 6; inline suggestions are in the third field, thread verdict in the fourth

### 6 — Handle Codex verdict

**Track all rounds.** Maintain a running list of every Codex finding across all fix iterations — severity badge, short description, and the commit it was fixed in. Append to this list on every round that has issues.

**Send a Slack DM on EVERY Codex round — both issues and clean verdicts.**

Parse the Codex comment body, then:

- **Issues found** (any round with a P1/P2/P3 badge):
  - Print the full Codex comment in chat
  - Send Slack DM immediately — one DM per round:
    ```
    ⚠️ *PR #<N> — Codex Round <R> finding*
    *<Severity>: <finding title>*
    > <full codex comment body>
    Fixing now and re-triggering review…
    PR: <url>
    ```
  - Then fix, commit, push, re-trigger `@codex review`, re-arm Monitor — continue loop

- **No critical issues** (body contains "no major issues", "looks good", "no critical", "LGTM"):
  - Print the full Codex comment in chat
  - Send Slack DM — clean/positive style, **including the full history of all prior rounds**:
    ```
    ✅ *PR #<N> — Codex review complete*
    Verdict: No critical issues found.

    *Review history (<R> rounds):*
    • Round 1 — P1: <finding title> → fixed in <commit>
    • Round 2 — P2: <finding title> → fixed in <commit>
    • … (one line per round that had issues; omit if zero rounds)

    PR: <url>
    Branch: <branch> → main
    Ready to merge when you are!
    ```
  - Stop looping.

---

## Notes

- `gh` binary lives at `~/.local/bin/gh` — always use the full path.
- Always PR to `main`, never merge directly.
- The Slack user ID for Sandeep Jha is `U07SX2XTY86`.
- **All human-in-the-loop requests go to Slack DM, not chat.** Any time you need approval, a decision, or confirmation before proceeding, send a Slack DM to `U07SX2XTY86` describing the situation and the options. Do not block in chat waiting for a reply.
- If there is nothing to commit (clean working tree), send a Slack DM asking what the user wants to push.
- If a PR for this branch already exists, skip Step 3 and use the existing PR number.
