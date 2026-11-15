# derek-skills (Derek's Agent Skills)

Modular repository and plugin of reusable agent skills: Android/KMP development, multi-agent orchestration, gesture-driven animation, preferred skills management, and infrastructure host directory.

Built to be loadable either as an individual skill, full bundle, or as a plugin with namespaced sub-categories:
```
/derek-skills:<sub category>
```

## Sub-Category Commands & Skills

| Syntax | Description | Location |
| --- | --- | --- |
| `/derek-skills:hosts` | Infrastructure directory, SSH aliases & live Gist snapshot | `skills/hosts/` |
| `/derek-skills:skills` | Preferred skills catalog and installer | `skills/skills/` |
| `/derek-skills:android` | Android & KMP master development suite | `skills/android/` |
| `/derek-skills:multi-agent-orchestration` | Multi-agent coordination, preambles & delegation | `skills/multi-agent-orchestration/` |
| `/derek-skills:interaction-driven-animation` | 1:1 gesture tracking & momentum flings | `skills/interaction-driven-animation/` |
| `/derek-skills:android-design-gallery-and-signing` | Material 3 component gallery & keystore safety | `skills/android-design-gallery-and-signing/` |
| `/derek-skills:adaptive-ui-checklist` | Window size classes, foldables, and adaptive layouts | `skills/adaptive-ui-checklist/` |

---

## Infrastructure Host Directory (`/derek-skills:hosts`)

Contains direct connection details, SSH aliases (`.lab`, `.lab.proxy`, `.oracle.proxy`), IP mappings, and ports for all machines across Home Proxmox VE and Oracle Cloud.

> **Live Infrastructure Snapshot (Gist):**  
> 🔗 [https://gist.github.com/hereisderek/9d10d746711c34f3b20c1a07282237f3](https://gist.github.com/hereisderek/9d10d746711c34f3b20c1a07282237f3)

---

## Preferred Skills Management (`/derek-skills:skills`)

Manages and installs Derek's curated skills into `~/.agents/skills/` and symlinks them into all agent directories (`~/.claude/skills`, `~/.codex/skills`, `~/.gemini/skills`, etc.).

### Current Preferred Skills
1. **[OpenSpec (Fission-AI)](https://github.com/Fission-AI/openspec)**: Spec-driven development (`npm install -g @fission-ai/openspec@latest`)
2. **[Android Official Skills](https://github.com/android/skills)**: Google Android skills suite (`npx --yes skills add android/skills -g --full-depth -y`)

### CLI Commands
```bash
# List all preferred skills and install status
./skills/skills/scripts/manage_skills.sh list

# Install all preferred skills
./skills/skills/scripts/manage_skills.sh install --all

# Install a specific skill
./skills/skills/scripts/manage_skills.sh install openspec
./skills/skills/scripts/manage_skills.sh install android-skills

# Interactively select skills to install
./skills/skills/scripts/manage_skills.sh select

# Sync symlinks across agent directories
./skills/skills/scripts/manage_skills.sh sync
```

---

## Installation as a Claude / Agent Plugin

```bash
claude plugin install derek-skills
```
Or symlink into `~/.claude/skills/derek-skills` / `~/.agents/skills/derek-skills`.
