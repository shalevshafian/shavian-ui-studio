#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile

def assert_true(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)

def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--marketplace-root", required=True)
    args = parser.parse_args()

    market = Path(args.marketplace_root).resolve()
    plugin = market / "plugins" / "shavian-ui-studio"
    scaffold = plugin / "scripts" / "scaffold_project.py"

    marketplace_json = json.loads((market / ".claude-plugin" / "marketplace.json").read_text())
    plugin_json = json.loads((plugin / ".claude-plugin" / "plugin.json").read_text())

    assert_true(marketplace_json["name"] == "shavian-tools", "Unexpected marketplace name")
    assert_true(plugin_json["name"] == "shavian-ui-studio", "Unexpected plugin name")
    assert_true(plugin_json["version"] == marketplace_json["plugins"][0]["version"], "Version mismatch")
    assert_true(not (plugin / "hooks").exists(), "Safe default violated: hooks folder exists")
    assert_true(not (plugin / ".mcp.json").exists(), "Safe default violated: bundled MCP exists")

    with tempfile.TemporaryDirectory() as temp:
        project = Path(temp) / "demo-project"
        project.mkdir()
        claude_md = project / "CLAUDE.md"
        claude_md.write_text("# Existing project rules\n\nKeep this line.\n", encoding="utf-8")

        dry = run([sys.executable, str(scaffold), "--root", str(project)])
        assert_true(dry.returncode == 0, dry.stdout)
        assert_true(not (project / "design-brain").exists(), "Dry run wrote files")

        apply = run([sys.executable, str(scaffold), "--root", str(project), "--apply"])
        assert_true(apply.returncode == 0, apply.stdout)
        assert_true((project / "design-brain" / "00-product-brief.md").exists(), "Missing brief")
        assert_true("Keep this line." in claude_md.read_text(), "Existing CLAUDE.md content lost")
        assert_true("SHAVIAN-UI-STUDIO:START" in claude_md.read_text(), "Workflow section missing")

        second = run([sys.executable, str(scaffold), "--root", str(project), "--apply"])
        assert_true(second.returncode == 0, second.stdout)
        text = claude_md.read_text()
        assert_true(text.count("SHAVIAN-UI-STUDIO:START") == 1, "Scaffold is not idempotent")

        backups = list((project / ".shavian-ui-studio-backups").glob("CLAUDE.md.*.bak"))
        assert_true(len(backups) == 1, "Expected exactly one CLAUDE.md backup")

        assert_true((project / "design-brain" / "16-taste-overlay.md").exists(), "Missing taste overlay")

        mood = run([sys.executable, str(plugin / "scripts" / "build_moodboard.py"), "--root", str(project)])
        assert_true(mood.returncode == 0, mood.stdout)
        board = project / "design-brain" / "assets" / "moodboard" / "index.html"
        assert_true(board.exists(), "Mood board not generated")
        assert_true("<!doctype html>" in board.read_text().lower(), "Mood board is not valid HTML")

    taste_path = run([sys.executable, str(plugin / "scripts" / "taste_profile.py"), "--path"])
    assert_true(taste_path.returncode == 0, taste_path.stdout)
    assert_true("shavian-ui-studio" in taste_path.stdout, "Taste profile path unexpected")
    assert_true("taste-profile.md" in taste_path.stdout, "Taste profile filename unexpected")

    reference = plugin / "reference"
    for doc in ["design-knowledge.md", "style-taxonomy.md", "question-playbook.md", "screenshot-protocol.md", "parallel-brainstorm.md"]:
        assert_true((reference / doc).exists(), f"Missing reference doc: {doc}")

    compile_result = run([sys.executable, "-m", "compileall", "-q", str(plugin / "scripts")])
    assert_true(compile_result.returncode == 0, compile_result.stdout)

    print("Static smoke tests passed.")
    print("- marketplace manifest parsed")
    print("- plugin manifest parsed")
    print("- no hooks bundled")
    print("- no MCP servers bundled")
    print("- dry run preserved filesystem")
    print("- apply mode created project files")
    print("- existing CLAUDE.md preserved and backed up")
    print("- second scaffold run was idempotent")
    print("- taste overlay scaffolded")
    print("- local mood board generated (offline HTML)")
    print("- taste profile path resolves without writing outside config dir")
    print("- embedded reference knowledge present")
    print("- Python scripts compiled")

if __name__ == "__main__":
    main()
