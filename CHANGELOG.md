# Changelog

## 1.1.0 — 2026-06-01

- Added `/shavian-ui-studio:vision` — the fast path from an idea to a screen, with sharp questions, screenshot/sketch intake, a parallel brainstorm, and distinct directions.
- Added `/shavian-ui-studio:moodboard` — a native Figma mood board when connected, with a self-contained local HTML fallback (`scripts/build_moodboard.py`).
- Added `/shavian-ui-studio:taste` — a durable personal taste profile that learns the user's preferences across projects (global `~/.claude/shavian-ui-studio/taste-profile.md` plus a per-project overlay).
- Added an embedded design-knowledge base (`reference/`): design principles and variable relationships, a style taxonomy, a question playbook, a screenshot protocol, and a parallel-brainstorm playbook.
- Added the `style-analyst` and `moodboard-curator` agents.
- Wired screenshots, the knowledge base, the taste profile, and the parallel brainstorm into bootstrap, screen, research, review, and lock.
- Made every skill context-activated: the workflow now runs from natural language in the conversation, with slash commands kept as optional shortcuts. Added a "how this activates" routing note to the project `CLAUDE.md` section.
- Fixed the `verify` skill: removed references to non-existent commands; it now detects how to run the project from its manifest and scripts.
- Fixed plugin/marketplace manifests to pass `claude plugin validate` (removed unsupported keys; moved the marketplace description under `metadata`).

## 1.0.0 — 2026-06-01

- Converted the workflow into a shareable Claude Code marketplace plugin.
- Added creator attribution for Shavian Music (@shavianofficial).
- Added adaptive UI project onboarding.
- Added project-local design-brain scaffolding.
- Added Figma capability matrix, including read, native write-to-canvas, Code Connect, diagrams, assets, and code-to-canvas workflows.
- Added Mobbin-backed pattern research workflow.
- Added independent critic and design-system audit agents.
- Added golden screenshot verification workflow.
- Added doctor, safe local installer, integration setup helper, checksums, privacy policy, threat model, and smoke tests.
- Removed automatic MCP registration and destructive installation behavior.
