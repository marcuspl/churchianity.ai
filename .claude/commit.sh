#!/bin/bash
# Usage: Write message to .claude/COMMIT_MSG first, then run .claude/commit.sh
# No arguments needed — reads from the file, commits, pushes, cleans up.
MSGFILE="$(git rev-parse --show-toplevel)/.claude/COMMIT_MSG"
if [ ! -f "$MSGFILE" ]; then
  echo "Error: No .claude/COMMIT_MSG file found. Write the message there first."
  exit 1
fi
git commit -F "$MSGFILE"
rm "$MSGFILE"
git push
