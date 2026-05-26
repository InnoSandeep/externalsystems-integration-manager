#!/usr/bin/env bash
# Claude Code PreToolUse hook entry point.
# Pipes stdin → slack_approval.py, which handles all Slack API interaction.
# The CWD when hooks run is the project root, so the relative path resolves correctly.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "${SCRIPT_DIR}/slack_approval.py" "$@"
