---
name: verify
description: Verify implemented UI against the approved design system and golden screenshots. Trigger after a screen is implemented, before handoff, or when the user asks whether the built UI matches the design. Asks before running local commands.
argument-hint: "<route, screen, flow, or viewport>"
---

# Verify UI implementation

Target: $ARGUMENTS

1. Read:
   - `08-locked-decisions.md`;
   - `09-ui-rubric.md`;
   - `10-screen-inventory.md`;
   - `12-handoff-log.md`.
2. Detect how to run the project locally by inspecting its package manifest and scripts (dev server, Storybook, or build/preview).
3. If no run method is found, report that and stop before attempting to render.
4. Ask before running any local command.
5. Render the relevant screen at approved viewports.
6. Capture screenshots locally.
7. Compare against:
   - approved Figma screenshot when available;
   - `design-brain/assets/golden-screens/`;
   - tokens and component rules.
8. List visible differences in priority order.
9. Fix only differences that violate approved decisions or the rubric.
10. When useful and explicitly approved, use Figma code-to-canvas to capture the live UI as editable layers for review.
11. Update the handoff log.

Do not upload screenshots or assets without approval.
