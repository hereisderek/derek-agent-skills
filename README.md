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
| `/derek-skills:docker-hosts` | Docker/Podman runtime on LXCs 2028/2029, portbridge, and Caddy proxy | `skills/docker-hosts/` |
| `/derek-skills:worktree-workflow` | Feature development lifecycle with Worktrunk (`wt`) and branch isolation | `skills/worktree-workflow/` |
| `/derek-skills:release-cicd` | Semantic release policies, tag formatting, and CI/CD rules | `skills/release-cicd/` |
| `/derek-skills:markdown-converter` | Document conversion to Markdown via Microsoft `markitdown` | `skills/markdown-converter/` |
| `/derek-skills:preferred-skills` | Preferred skills catalog and installer | `skills/preferred-skills/` |
| `/derek-skills:multi-agent-orchestration` | Multi-agent coordination, preambles, Gradle locks & delegation | `skills/multi-agent-orchestration/` |
| `/derek-skills:state-droid-remote-device` | StageDroid device leasing, wake/unlock, and UI auditing | `skills/state-droid-remote-device/` |
| `/derek-skills:android` | Android & KMP master development suite and verification hooks | `skills/android/` |
| `/derek-skills:adaptive-ui-checklist` | Window size classes, foldables, and adaptive layouts | `skills/adaptive-ui-checklist/` |
| `/derek-skills:android-design-gallery-and-signing` | Material 3 component gallery & keystore safety | `skills/android-design-gallery-and-signing/` |
| `/derek-skills:interaction-driven-animation` | 1:1 gesture tracking & momentum flings | `skills/interaction-driven-animation/` |
| `/derek-skills:pl-coding-skills-bundle` | Philipp Lackner Android & KMP architecture and coding bundle | `skills/PL Coding Skills Bundle/` |

---

## Infrastructure Host Directory (`/derek-skills:hosts`)

Contains direct connection details, SSH aliases (`.lab`, `.lab.proxy`, `.oracle.proxy`), IP mappings, and ports for all machines across Home Proxmox VE and Oracle Cloud.

> **Live Infrastructure Snapshot (Gist):**  
> 🔗 [https://gist.github.com/hereisderek/9d10d746711c34f3b20c1a07282237f3](https://gist.github.com/hereisderek/9d10d746711c34f3b20c1a07282237f3)

---

## Preferred Skills Management (`/derek-skills:preferred-skills`)

Manages and installs Derek's curated skills into `~/.agents/skills/` and symlinks them into all agent directories (`~/.claude/skills`, `~/.codex/skills`, `~/.gemini/skills`, etc.).

### Current Preferred Skills
1. **[OpenSpec (Fission-AI)](https://github.com/Fission-AI/openspec)**: Spec-driven development (`npm install -g @fission-ai/openspec@latest`)
2. **[Android CLI (Google)](https://github.com/android/skills)**: Official Android CLI tool skill (`npx --yes skills add android/skills -g --skill android-cli -y`)
3. **[android/skills (The Full Suite)](https://github.com/android/skills)**: Google's complete 21+ Android & KMP engineering skills suite (`npx --yes skills add android/skills -g --full-depth -y`)

### CLI Commands
```bash
# List all preferred skills and install status
./skills/preferred-skills/scripts/manage_skills.sh list

# Install all preferred skills
./skills/preferred-skills/scripts/manage_skills.sh install --all

# Install a specific skill
./skills/preferred-skills/scripts/manage_skills.sh install openspec
./skills/preferred-skills/scripts/manage_skills.sh install android-cli
./skills/preferred-skills/scripts/manage_skills.sh install android-skills

# Interactively select skills to install
./skills/preferred-skills/scripts/manage_skills.sh select

# Sync symlinks across agent directories
./skills/preferred-skills/scripts/manage_skills.sh sync
```

---

## Setup & Installation

### Standard Skill Installation via NPM / NPX (`skills` CLI)

Install Derek's entire skill suite directly into `~/.agents/skills/`:
```bash
npx --yes skills add hereisderek/derek-agent-skills -g --full-depth -y
```

Install recommended preferred skills individually via npm/npx:
```bash
# 1. Official Google Android skills suite (adaptive, camerax, compose, navigation-3, etc.)
npx --yes skills add android/skills -g --full-depth -y

# 2. Android CLI skill only
npx --yes skills add android/skills -g --skill android-cli -y

# 3. OpenSpec (spec-driven development)
npm install -g @fission-ai/openspec@latest
```

---

### Local Repository Setup & Bootstrap (with Submodules)

If cloning the repository locally for development or plugin linking:

```bash
# Clone with submodules and install all preferred skills in one step:
git clone --recurse-submodules git@github.com:hereisderek/derek-agent-skills.git
cd derek-agent-skills
./scripts/bootstrap.sh --with-preferred
```

To only set up the core suite without installing external preferred skills:
```bash
./scripts/bootstrap.sh
```

### Installation as a Claude / Agent Plugin

```bash
claude plugin install derek-skills
```
Or symlink into `~/.claude/skills/derek-skills` / `~/.agents/skills/derek-skills`.

---

## Project-Aware Skill Suggestions & Update Checks

When loaded by invoking `/derek-skills` or `/derek agentic skill`, the router inspects the workspace directory:
- **Android / KMP Projects**: Automatically checks for Google's official `android-cli` and `android/skills`. If missing, it prompts you with the command to install them; if already installed, it prompts to check for updates (`android update` or `npx skills update`).
- **Web / Spec-Driven Projects**: Checks for `openspec`. Prompts to install or update to the latest version.
- **Universal Setup**: Offers to run `./scripts/bootstrap.sh --with-preferred` to ensure all tooling is in place.
