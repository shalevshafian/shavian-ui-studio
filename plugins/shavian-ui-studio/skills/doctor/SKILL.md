---
name: doctor
description: Check whether Shavian UI Studio, Claude Code, project scaffolding, the taste profile, Figma, and Mobbin are available. Use when onboarding, troubleshooting setup, or when the user asks what is connected or what they can do. Read-only.
argument-hint: "[optional project path]"
---

# Doctor

Run a local read-only check:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/doctor.py" --root "${CLAUDE_PROJECT_DIR}"
```

Report:
- Claude Code availability and version;
- whether the current project is scaffolded;
- whether the personal taste profile exists and whether a local mood board has been built;
- whether Figma and Mobbin appear configured;
- which workflows can run now;
- which optional connections remain missing.

Do not install anything automatically.
