---
name: taste
description: View and refine the personal taste profile the workflow learns over time. Trigger when the user states a durable design preference, asks what the workflow knows about their taste, or wants to correct a learned preference.
argument-hint: "[show | a preference to record or correct]"
---

# Personal taste profile

Request: $ARGUMENTS

The taste profile is a durable, plain-text, user-owned record of design preferences that the workflow learns across every project. It lives globally at `~/.claude/shavian-ui-studio/taste-profile.md`, with a per-project overlay at `design-brain/16-taste-overlay.md`.

## Inspect

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/taste_profile.py" --init
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/taste_profile.py" --show
```
Also read the per-project overlay when a project is scaffolded.

## If the request is just "show"

Summarize the global profile and the project overlay: strongest preferences, anti-preferences, default choices, and working style. Stop.

## If the request records or corrects a preference

1. Decide scope:
   - durable and cross-project → the global profile;
   - specific to this product → `design-brain/16-taste-overlay.md`.
2. Get the global file path:
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/scripts/taste_profile.py" --path
   ```
3. Edit the right file directly. Use the existing tables and sections. For each entry record: the preference, a confidence level (LIKELY / STRONG / LOCKED), a short evidence note, and today's date.
4. Promote confidence only with real evidence: LIKELY on first observation, STRONG when confirmed across two or more projects or decisions, LOCKED only when the user explicitly says it is a hard preference.
5. Never invent preferences. Record only what the user stated or what is evidenced by approvals and rejections.
6. Map style preferences to labels in `${CLAUDE_PLUGIN_ROOT}/reference/style-taxonomy.md`.

## How other skills feed this

`/shavian-ui-studio:lock`, `/shavian-ui-studio:review`, and `/shavian-ui-studio:vision` propose taste updates after clear approvals or rejections. This skill is the manual entry point to inspect or correct what was learned.

## Report

List what changed (file and rows), the new confidence levels, and how it will affect future defaults.
