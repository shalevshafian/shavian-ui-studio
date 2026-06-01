#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import shutil
import sys

MARKER_START = "<!-- SHAVIAN-UI-STUDIO:START -->"
VERSION = "1.1.0"

def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(2)

def validate_root(root: Path) -> Path:
    root = root.expanduser().resolve()
    home = Path.home().resolve()
    if not root.exists() or not root.is_dir():
        fail(f"Project root does not exist or is not a directory: {root}")
    if root == Path("/").resolve():
        fail("Refusing to scaffold the filesystem root.")
    if root == home:
        fail("Refusing to scaffold the user's home directory. Start Claude Code inside a specific project folder.")
    if root.is_symlink():
        fail("Refusing a symlink project root.")
    return root

def safe_target(root: Path, rel: Path) -> Path:
    target = root / rel
    resolved_parent = target.parent.resolve()
    try:
        resolved_parent.relative_to(root)
    except ValueError:
        fail(f"Target escapes project root: {rel}")
    if target.exists() and target.is_symlink():
        fail(f"Refusing to write through symlink: {target}")
    return target

def print_action(kind: str, path: Path) -> None:
    print(f"{kind:>8}: {path}")

def create_missing(root: Path, rel: Path, source: Path, apply: bool) -> None:
    target = safe_target(root, rel)
    if target.exists():
        print_action("exists", target)
        return
    print_action("create", target)
    if apply:
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            shutil.copy2(source, target)

def append_claude_section(root: Path, section_source: Path, apply: bool) -> None:
    target = safe_target(root, Path("CLAUDE.md"))
    existing = target.read_text(encoding="utf-8") if target.exists() else ""
    if MARKER_START in existing:
        print_action("exists", target)
        return
    print_action("append", target)
    if apply:
        if target.exists():
            stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
            backup = safe_target(root, Path(f".shavian-ui-studio-backups/CLAUDE.md.{stamp}.bak"))
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target, backup)
            print_action("backup", backup)
        target.parent.mkdir(parents=True, exist_ok=True)
        section = section_source.read_text(encoding="utf-8")
        sep = "\n\n" if existing.strip() else ""
        target.write_text(existing.rstrip() + sep + section.rstrip() + "\n", encoding="utf-8")

def write_manifest(root: Path, apply: bool) -> None:
    target = safe_target(root, Path(".shavian-ui-studio.json"))
    if target.exists():
        print_action("exists", target)
        return
    print_action("create", target)
    if apply:
        payload = {
            "name": "Shavian UI Studio",
            "version": VERSION,
            "createdBy": "Shavian Music (@shavianofficial)",
            "scaffoldedAt": dt.datetime.now(dt.timezone.utc).isoformat(),
            "safeDefaults": {
                "automaticHooks": False,
                "bundledMcpServers": False,
                "telemetry": False,
                "silentExternalWrites": False
            }
        }
        target.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

def main() -> None:
    parser = argparse.ArgumentParser(description="Create a safe project-local UI design brain.")
    parser.add_argument("--root", default=".", help="Project folder. Defaults to current directory.")
    parser.add_argument("--apply", action="store_true", help="Write files. Without this flag, perform a dry run.")
    args = parser.parse_args()

    root = validate_root(Path(args.root))
    script_dir = Path(__file__).resolve().parent
    plugin_root = script_dir.parent
    templates = plugin_root / "templates" / "design-brain"
    section_source = plugin_root / "templates" / "CLAUDE_UI_SECTION.md"

    if not templates.exists():
        fail(f"Templates folder missing: {templates}")

    print(f"Shavian UI Studio scaffold {'APPLY' if args.apply else 'DRY RUN'}")
    print(f"Project root: {root}")
    print("")

    for source in sorted(templates.rglob("*")):
        rel = Path("design-brain") / source.relative_to(templates)
        if source.is_dir():
            target = safe_target(root, rel)
            if not target.exists():
                print_action("mkdir", target)
                if args.apply:
                    target.mkdir(parents=True, exist_ok=True)
            continue
        create_missing(root, rel, source, args.apply)

    append_claude_section(root, section_source, args.apply)
    write_manifest(root, args.apply)

    print("")
    if args.apply:
        print("Scaffold complete. Existing files were preserved.")
    else:
        print("Dry run complete. Re-run with --apply after reviewing the planned changes.")

if __name__ == "__main__":
    main()
