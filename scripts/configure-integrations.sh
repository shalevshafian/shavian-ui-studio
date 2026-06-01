#!/usr/bin/env bash
set -euo pipefail

if ! command -v claude >/dev/null 2>&1; then
  echo "Claude Code CLI was not found in PATH."
  exit 1
fi

echo "Optional integration setup"
echo ""
echo "No credentials are requested by this script."
echo "Authentication happens later through Claude Code's /mcp interface."
echo ""
echo "Planned commands:"
echo "  1. claude plugin install figma@claude-plugins-official"
echo "  2. claude mcp add mobbin --scope user --transport http https://api.mobbin.com/mcp"
echo ""
read -r -p "Run these commands? [y/N] " answer
case "$answer" in
  y|Y|yes|YES)
    ;;
  *)
    echo "Cancelled."
    exit 0
    ;;
esac

echo ""
echo "Installing the official Figma plugin..."
claude plugin install figma@claude-plugins-official || {
  echo "Figma plugin installation did not finish."
  echo "Manual fallback:"
  echo "  claude mcp add --scope user --transport http figma https://mcp.figma.com/mcp"
}

echo ""
echo "Registering Mobbin MCP..."
claude mcp add mobbin --scope user --transport http https://api.mobbin.com/mcp || {
  echo "Mobbin registration may already exist or may have failed."
  echo "Manual command:"
  echo "  claude mcp add mobbin --scope user --transport http https://api.mobbin.com/mcp"
}

echo ""
echo "Next step:"
echo "  Start Claude Code and use /mcp to authenticate Figma and Mobbin."
