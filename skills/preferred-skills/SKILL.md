---
name: preferred-skills
description: Preferred skills catalog and installer for Derek's AI agents. Manage, browse, and install curated engineering skills (OpenSpec, Android skills, etc.) with automatic symlinking to universal (~/.agents/skills) and agent-specific directories.
---

# Preferred Skills Manager (`/derek-skills:preferred-skills`)

This skill manages Derek's preferred agent skills, tracking their repositories, package install commands, and providing one-command installation with universal agent symlinking.

## Preferred Skills Catalog

| Skill Name | Repository | Install Command / NPM | Purpose |
|---|---|---|---|
| **OpenSpec (Fission-AI)** | [Fission-AI/openspec](https://github.com/Fission-AI/openspec) | `npm install -g @fission-ai/openspec@latest` | Spec-driven development (SDD) for AI coding assistants (`/opsx:explore`, `/opsx:propose`, `/opsx:archive`) |
| **Android CLI (Google)** | [android/skills](https://github.com/android/skills) | `npx --yes skills add android/skills -g --skill android-cli -y` | Official Android CLI skill for device layout inspection, screenshots, UI testing, and emulator control |
| **android/skills (The Full Suite)** | [android/skills](https://github.com/android/skills) | `npx --yes skills add android/skills -g --full-depth -y` | Google's complete official suite of 21+ Android & KMP skills (adaptive, camerax, compose, navigation-3, testing-setup, r8-analyzer, edge-to-edge, wear-compose, etc.) |

## Usage Commands

You can run the manager script directly or ask the agent to run it:

```bash
# 1. Show the list of preferred skills and their installation status
./skills/preferred-skills/scripts/manage_skills.sh list

# 2. Install all preferred skills in the catalog
./skills/preferred-skills/scripts/manage_skills.sh install --all

# 3. Install a specific preferred skill
./skills/preferred-skills/scripts/manage_skills.sh install openspec
./skills/preferred-skills/scripts/manage_skills.sh install android-skills

# 4. Interactively choose which skills to install
./skills/preferred-skills/scripts/manage_skills.sh select

# 5. Re-synchronize symlinks from ~/.agents/skills to all installed agent directories
./skills/preferred-skills/scripts/manage_skills.sh sync
```

## Installation & Symlinking Convention

Following the standard convention on Derek's machine:
- Skills are installed canonically into `~/.agents/skills/`.
- Symlinks are automatically created/maintained across detected agent environments:
  - `~/.claude/skills`
  - `~/.codex/skills`
  - `~/.gemini/skills`
  - `~/.config/opencode/skills`
  - `~/.continue/skills`
  - `~/.copilot/skills`
- Compatibility symlink `~/agents` -> `~/.agents` is created if absent.

## Adding New Skills

To add a new skill to the preferred catalog, append an entry to `skills/preferred-skills/skills.json`:

```json
{
  "id": "my-skill",
  "name": "My Skill Name",
  "description": "What this skill does",
  "repo": "https://github.com/username/repo",
  "npm": "npm install -g ...",
  "installCommand": "npx --yes skills add username/repo -g -y",
  "checkPath": "~/.agents/skills/my-skill"
}
```
