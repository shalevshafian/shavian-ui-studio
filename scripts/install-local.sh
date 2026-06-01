#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if ! command -v claude >/dev/null 2>&1; then
  echo "Claude Code CLI was not found in PATH."
  echo "Install Claude Code first, then rerun this script."
  exit 1
fi

echo "This will add a local marketplace from:"
echo "  $ROOT"
echo ""
echo "It will not configure Figma or Mobbin."
echo "It will not run hooks or background services."
echo ""
read -r -p "Continue? [y/N] " answer
case "$answer" in
  y|Y|yes|YES)
    ;;
  *)
    echo "Cancelled."
    exit 0
    ;;
esac

claude plugin validate "$ROOT"
claude plugin validate "$ROOT/plugins/shavian-ui-studio"
claude plugin marketplace add "$ROOT" --scope user
claude plugin install shavian-ui-studio@shavian-tools

echo ""
echo "Installed."
echo "Start Claude Code inside a project and run:"
echo "  /shavian-ui-studio:doctor"
echo "  /shavian-ui-studio:bootstrap"
