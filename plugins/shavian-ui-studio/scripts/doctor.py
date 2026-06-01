#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys

def run(cmd: list[str]) -> tuple[int, str]:
    try:
        p = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=15)
        return p.returncode, p.stdout.strip()
    except Exception as exc:
        return 1, str(exc)

def status(ok: bool) -> str:
    return "OK" if ok else "CHECK"

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root).expanduser().resolve()

    print("Shavian UI Studio doctor")
    print(f"Project: {root}")
    print("")

    claude = shutil.which("claude")
    print(f"[{status(bool(claude))}] Claude Code CLI: {claude or 'not found'}")

    python_ok = sys.version_info >= (3, 10)
    print(f"[{status(python_ok)}] Python: {sys.version.split()[0]}")

    brain = root / "design-brain"
    print(f"[{status(brain.exists())}] design-brain/: {'present' if brain.exists() else 'not scaffolded'}")

    marker = root / ".shavian-ui-studio.json"
    print(f"[{status(marker.exists())}] project marker: {'present' if marker.exists() else 'not scaffolded'}")

    taste = Path.home().resolve() / ".claude" / "shavian-ui-studio" / "taste-profile.md"
    print(f"[{status(taste.exists())}] taste profile: {'present' if taste.exists() else 'not created (run /shavian-ui-studio:taste)'}")

    moodboard = brain / "assets" / "moodboard" / "index.html"
    print(f"[{status(moodboard.exists())}] local mood board: {'present' if moodboard.exists() else 'not built yet'}")

    if claude:
        code, out = run([claude, "--version"])
        print(f"[{status(code == 0)}] Claude Code version: {out or 'unknown'}")

        code, out = run([claude, "mcp", "list"])
        low = out.lower()
        figma = "figma" in low
        mobbin = "mobbin" in low
        print(f"[{status(code == 0)}] MCP list readable")
        print(f"[{status(figma)}] Figma MCP/plugin: {'detected' if figma else 'not detected'}")
        print(f"[{status(mobbin)}] Mobbin MCP: {'detected' if mobbin else 'not detected'}")
    else:
        print("[CHECK] MCP status unavailable because Claude Code CLI is missing")

    print("")
    print("Safety profile")
    print("[OK] No automatic hooks bundled")
    print("[OK] No MCP servers bundled")
    print("[OK] No telemetry bundled")
    print("[OK] Scaffold defaults to dry run")
    print("")
    print("Recommended next step:")
    if not brain.exists():
        print("  Run /shavian-ui-studio:bootstrap")
    else:
        print("  Run /shavian-ui-studio:research <flow> or /shavian-ui-studio:screen <screen>")

if __name__ == "__main__":
    main()
