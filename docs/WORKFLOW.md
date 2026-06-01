# Workflow

## Fast path (idea → screen)

```text
/shavian-ui-studio:vision <your idea>
```

This runs the front of the workflow in one pass: a few sharp questions, screenshot/sketch intake, a parallel brainstorm, a mood board, and 2–3 structurally distinct directions with an honest critique.

## First-time project flow (full)

```text
/shavian-ui-studio:doctor
/shavian-ui-studio:bootstrap
/shavian-ui-studio:research <first flow>
/shavian-ui-studio:moodboard
/shavian-ui-studio:screen <first anchor screen>
/shavian-ui-studio:review <frame URL or screenshot>
/shavian-ui-studio:lock <approved decisions>
/shavian-ui-studio:taste show
/shavian-ui-studio:sync-figma <approved direction>
/shavian-ui-studio:verify <implemented screen>
```

## What the plugin knows and remembers

- **Embedded knowledge** — `reference/` holds the design principles, style taxonomy, question playbook, screenshot protocol, and parallel-brainstorm playbook the skills read, so directions are smart rather than generic.
- **Parallel brainstorm** — kickoff fans out independent agents (references, style analysis, flow, mood board) and synthesizes them into distinct directions.
- **Taste profile** — a durable, plain-text record of your preferences at `~/.claude/shavian-ui-studio/taste-profile.md`, refined (with your approval) as you accept and reject directions, plus a per-project overlay in `design-brain/16-taste-overlay.md`.

## Philosophy

The workflow separates:

- product truth;
- user taste;
- reference evidence;
- provisional hypotheses;
- locked decisions;
- visual exploration;
- implementation;
- independent review.

This prevents Claude from treating every new prompt as permission to redesign the entire product.
