---
name: lock
description: Persist explicit UI approvals, rejections, and superseded decisions in the project's design brain. Trigger when the user clearly approves, rejects, or supersedes a design decision (e.g. "I approve direction B", "let's drop the gradient"). Do not trigger on tentative or exploratory comments.
argument-hint: "<approved, rejected, or superseded decision>"
---

# Lock decisions

Decision input: $ARGUMENTS

1. Extract the exact decision and scope.
2. Classify it:
   - `LOCKED`;
   - `REJECTED`;
   - `SUPERSEDED`.
3. Update `design-brain/08-locked-decisions.md`.
4. Update affected principles, tokens, component rules, reference atlas, screen inventory, or experiment log.
5. Preserve older history by superseding rows rather than deleting them.
6. If the decision reflects a durable design preference (a style, palette tendency, density, motion, or layout strategy the user consistently chooses or rejects), record it as a taste signal:
   - cross-project preference → the global profile (path from `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/taste_profile.py" --path`);
   - project-specific preference → `design-brain/16-taste-overlay.md`.
   Use confidence LIKELY / STRONG / LOCKED with a dated evidence note. Never invent a preference; record only what is evidenced.
7. Report changed files and downstream impact.
