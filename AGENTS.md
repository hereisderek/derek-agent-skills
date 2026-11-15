# AGENTS.md — Single Source of Agent Instructions

Operational instructions, conventions, and maintenance guide for AI agents working in `derek-agent-skills`.

---

## 1. Project Overview

`derek-agent-skills` is Derek's modular repository of reusable agent skills and commands. It is designed to work across multiple agent platforms:
- **Claude Code**: Loaded as a plugin with namespaced commands (`/derek-skills:<category>`) via `plugin.json` and `commands/`.
- **Universal Agent Ecosystem** (Antigravity, Codex, Gemini CLI, Agent Kit): Loaded canonically via `~/.agents/skills/derek-skills` pointing to this repository.

---

## 2. Directory Structure

```text
derek-agent-skills/
├── SKILL.md                          # Root skill router
├── README.md                         # User-facing overview
├── AGENTS.md                         # Agent operational guidance (this file)
├── plugin.json                       # Claude plugin declaration
├── .claude-plugin/plugin.json        # Duplicate plugin manifest for Claude
├── commands/                         # Slash commands for Claude Code
│   ├── adaptive-ui-checklist.md
│   ├── android-design-gallery-and-signing.md
│   ├── android.md
│   ├── hosts.md
│   ├── interaction-driven-animation.md
│   ├── multi-agent-orchestration.md
│   ├── pl-coding-skills-bundle.md
│   ├── preferred-skills.md
│   └── skills.md
├── skills/                           # Individual modular skill directories
│   ├── adaptive-ui-checklist/
│   ├── android/
│   ├── android-design-gallery-and-signing/
│   ├── hosts/
│   ├── interaction-driven-animation/
│   ├── multi-agent-orchestration/
│   ├── PL Coding Skills Bundle/      # Git submodule -> hereisderek/pl-coding-skills-bundle
│   └── preferred-skills/             # Preferred skills manager & catalog
└── scripts/                          # Operational & automation tooling
    ├── bootstrap.sh                  # One-step submodule & symlink setup
    ├── update-pl-bundle.sh           # Safe update utility for PL Google Drive bundle
    └── link-myskills.sh              # Agent directory symlinker
```

---

## 3. Core Operational Conventions

### 3.1 Submodules
- `skills/PL Coding Skills Bundle` is a Git submodule tracking the private repository `git@github.com:hereisderek/pl-coding-skills-bundle.git`.
- When cloning or verifying in a fresh environment, run:
  ```bash
  ./scripts/bootstrap.sh
  # or manually:
  git submodule update --init --recursive
  ```
- **Never** commit raw files directly in place of the submodule commit pointer in `derek-agent-skills`.

### 3.2 Upstream Updates for `PL Coding Skills Bundle`
- The upstream bundle is maintained by Philipp Lackner and provided as a Google Drive zip:
  `https://drive.google.com/file/d/1ymCdsrztthwg2OsfEwWpKhS0e3TpOvGG/view`
- To update the bundle:
  ```bash
  ./scripts/update-pl-bundle.sh /path/to/downloaded-bundle.zip
  ```
- The script automatically unpacks the zip, verifies contents, updates the repository while preserving `.git`, `.gitignore`, `SKILL.md`, and `README.md`, and updates the submodule reference in `derek-agent-skills`.

### 3.3 Adding a New Skill
When adding a new engineering skill:
1. Place it in `skills/<skill-name>/SKILL.md`.
2. Ensure valid YAML frontmatter:
   ```yaml
   ---
   name: <skill-name>
   description: <clear summary of triggers, purpose, and usage>
   ---
   ```
3. Add a corresponding slash command in `commands/<skill-name>.md` pointing to `skills/<skill-name>/SKILL.md`.
4. Update the routing tables in both root `SKILL.md` and `README.md`.

---

## 4. Git & Worktree Hygiene

- **Worktrees**: Use Worktrunk (`wt`) for branching and worktree management when available.
- **Pushing**: Never force-push. Remote pushes require explicit user approval.
- **Commits**: Write conventional, descriptive commit messages (`feat:`, `chore:`, `fix:`, `docs:`).
