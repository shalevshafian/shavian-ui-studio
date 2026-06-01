---
name: screen
description: Design or iterate one bounded UI screen or flow using the project's design brain, references, locked decisions, and optional Figma tools. Trigger when the user wants to design, lay out, or iterate a specific screen, page, view, or component (not a whole app at once).
argument-hint: "<screen or bounded flow>"
---

# Design one screen or bounded flow

Target: $ARGUMENTS

0. Load the embedded knowledge and the user's taste:
   - read `${CLAUDE_PLUGIN_ROOT}/reference/design-knowledge.md` and `style-taxonomy.md`;
   - run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/taste_profile.py" --show` and read `design-brain/16-taste-overlay.md`.
1. Read all relevant `design-brain/` files.
2. Inspect `08-locked-decisions.md` before proposing changes.
3. Run `/shavian-ui-studio:research` when evidence is weak. If the user provides screenshots or a sketch, analyze them per `${CLAUDE_PLUGIN_ROOT}/reference/screenshot-protocol.md`.
4. If a related Figma frame exists, read:
   - design context;
   - screenshot;
   - variable definitions;
   - metadata only when needed;
   - available libraries and reusable components.
5. When structure is not locked, create two or three genuinely distinct grayscale directions.
6. Separate hierarchy from polish.
7. Include required states: loading, empty, error, success, and key edge cases where relevant.
8. Check accessibility implications.
9. Ask before any Figma write.
10. If approved to write, use a separate exploration section and native Figma structure.
11. Run `/shavian-ui-studio:review`.
12. Update screen inventory and handoff log.

Do not silently redesign approved areas. Do not upload assets without approval.
