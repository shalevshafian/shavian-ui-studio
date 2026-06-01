---
name: review
description: Run an independent, ruthless UI review against the product brief, anti-references, rubric, accessibility concerns, and locked decisions. Use before approving a screen or when a direction feels off.
argument-hint: "<frame URL, screenshot, route, or screen name>"
context: fork
agent: ui-critic
---

# Independent UI review

Review: $ARGUMENTS

1. Read the relevant `design-brain/` files, plus `${CLAUDE_PLUGIN_ROOT}/reference/design-knowledge.md` for objective standards and the user's taste (`taste_profile.py --show` and `design-brain/16-taste-overlay.md`). Judge against the brief and rubric first; never soften critique to flatter a taste preference.
2. For Figma frames, retrieve design context and screenshot.
3. Score every criterion in `design-brain/09-ui-rubric.md`.
4. Identify at most five highest-impact issues.
5. For each issue provide:
   - exact area;
   - why it weakens the design;
   - structural, interaction, visual, or accessibility classification;
   - one specific correction.
6. Prioritize hierarchy, spacing rhythm, component logic, and accessibility before decoration.
7. State:
   - `APPROVE`;
   - `APPROVE WITH MINOR CHANGES`;
   - `REVISE`.
8. Note any durable taste signal you observed (a style consistently approved or rejected) so `/shavian-ui-studio:lock` can persist it. Do not write it yourself.
9. Do not alter files or Figma.
