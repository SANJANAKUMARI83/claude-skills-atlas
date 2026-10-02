#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
TARGET="${1:-$HOME/.claude/skills}"

mkdir -p "$TARGET"
if [ -d "$REPO_ROOT/skills" ]; then
  cp -R "$REPO_ROOT/skills/." "$TARGET/"
fi

echo "Claude Skills Atlas skills copied to: $TARGET"
echo "Prompts remain available in: $REPO_ROOT/prompts"
