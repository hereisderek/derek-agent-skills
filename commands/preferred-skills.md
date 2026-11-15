---
description: Manage and install Derek's preferred agent skills.
---

# /derek-skills:preferred-skills

Manage and install Derek's preferred agent skills.

## What it does

1. Displays Derek's preferred skills catalog (OpenSpec, Android skills, etc.).
2. Checks whether each skill is currently installed in `~/.agents/skills` or available on `PATH`.
3. Offers commands to install all skills, install specific skills, or interactively select which to install.
4. Ensures all installed skills are automatically symlinked across detected agent directories (`~/.claude/skills`, `~/.codex/skills`, `~/.gemini/skills`, `~/.config/opencode/skills`).

## Execution

Run the skill manager CLI:

```bash
python3 "$CLAUDE_PLUGIN_ROOT/skills/preferred-skills/scripts/manage_skills.py" list
```

To install all:
```bash
python3 "$CLAUDE_PLUGIN_ROOT/skills/preferred-skills/scripts/manage_skills.py" install --all
```

To install a specific skill:
```bash
python3 "$CLAUDE_PLUGIN_ROOT/skills/preferred-skills/scripts/manage_skills.py" install <skill-id>
```
