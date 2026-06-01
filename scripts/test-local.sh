#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$ROOT/plugins/shavian-ui-studio/scripts/smoke_test.py" --marketplace-root "$ROOT"

if command -v claude >/dev/null 2>&1; then
  echo ""
  echo "Running Claude Code plugin validation..."
  claude plugin validate "$ROOT"
  claude plugin validate "$ROOT/plugins/shavian-ui-studio"
else
  echo ""
  echo "Claude Code CLI not found. Static smoke tests passed; CLI validation was skipped."
fi
