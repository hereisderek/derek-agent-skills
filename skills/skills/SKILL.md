---
name: skills
description: Preferred skills catalog and installer for Derek's AI agents. Manage, browse, and install curated engineering skills (OpenSpec, Android skills, etc.) with automatic symlinking to universal (~/.agents/skills) and agent-specific directories.
---

# Preferred Skills Manager (`/derek-skills:skills`)

This skill manages Derek's preferred agent skills, tracking their repositories, package install commands, and providing one-command installation with universal agent symlinking.

## Preferred Skills Catalog

| Skill Name | Repository | Install Command / NPM | Purpose |
|---|---|---|---|
| **OpenSpec (Fission-AI)** | [Fission-AI/openspec](https://github.com/Fission-AI/openspec) | `npm install -g @fission-ai/openspec@latest` | Spec-driven development (SDD) for AI coding assistants (`/opsx:explore`, `/opsx:propose`, `/opsx:archive`) |
| **Android Official Skills** | [android/skills](https://github.com/android/skills) | `npx --yes skills add android/skills -g --full-depth -y` | Google official Android & KMP engineering skills suite (adaptive, camerax, compose, navigation-3, testing, wear-compose) |

## Usage Commands

You can run the manager script directly or ask the agent to run it:

```bash
# 1. Show the list of preferred skills and their installation status
./skills/skills/scripts/manage_skills.sh list

# 2. Install all preferred skills in the catalog
./skills/skills/scripts/manage_skills.sh install --all

# 3. Install a specific preferred skill
./skills/skills/scripts/manage_skills.sh install openspec
./skills/skills/scripts/manage_skills.sh install android-skills

# 4. Interactively choose which skills to install
./skills/skills/scripts/manage_skills.sh select

# 5. Re-synchronize symlinks from ~/.agents/skills to all installed agent directories
./skills/skills/scripts/manage_skills.sh sync
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

To add a new skill to the preferred catalog, append an entry to `skills/skills/skills.json`:

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
