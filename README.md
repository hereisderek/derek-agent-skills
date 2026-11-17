# derek-agent-skills (Derek's Agent Skills)

Modular repository and plugin of reusable agent skills: Android/KMP development, multi-agent orchestration, gesture-driven animation, preferred skills management, and infrastructure host directory.

Built to be loadable either as an individual skill, full bundle, or as a plugin with namespaced sub-categories:
```
/derek-agent-skills:<sub category>  # (or /derek-skills:<sub category>)
```

## Sub-Category Commands & Skills

| Syntax | Description | Location |
| --- | --- | --- |
| `/derek-agent-skills:docker-hosts` | Docker/Podman runtime on LXCs 2028/2029, portbridge, and Caddy proxy | `skills/docker-hosts/` |
| `/derek-agent-skills:worktree-workflow` | Feature development lifecycle with Worktrunk (`wt`) and branch isolation | `skills/worktree-workflow/` |
| `/derek-agent-skills:release-cicd` | Semantic release policies, tag formatting, and CI/CD rules | `skills/release-cicd/` |
| `/derek-agent-skills:markdown-converter` | Document conversion to Markdown via Microsoft `markitdown` | `skills/markdown-converter/` |
| `/derek-agent-skills:preferred-skills` | Preferred skills catalog and installer | `skills/preferred-skills/` |
| `/derek-agent-skills:multi-agent-orchestration` | Multi-agent coordination, preambles, Gradle locks & delegation | `skills/multi-agent-orchestration/` |
| `/derek-agent-skills:state-droid-remote-device` | StageDroid device leasing, wake/unlock, and UI auditing | `skills/state-droid-remote-device/` |
| `/derek-agent-skills:android` | Android & KMP master development suite and verification hooks | `skills/android/` |
| `/derek-agent-skills:adaptive-ui-checklist` | Window size classes, foldables, and adaptive layouts | `skills/adaptive-ui-checklist/` |
| `/derek-agent-skills:android-design-gallery-and-signing` | Material 3 component gallery & keystore safety | `skills/android-design-gallery-and-signing/` |
| `/derek-agent-skills:interaction-driven-animation` | 1:1 gesture tracking & momentum flings | `skills/interaction-driven-animation/` |
| `/derek-agent-skills:pl-coding-skills-bundle` | Philipp Lackner Android & KMP architecture and coding bundle | `skills/PL Coding Skills Bundle/` |

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

Install Derek's skill suite intact into `~/.agents/skills/derek-agent-skills`:
```bash
npx --yes skills add hereisderek/derek-agent-skills -g -y
```
*(Omitting `--full-depth` preserves the package structure intact as a single unified `derek-agent-skills` module rather than splitting sub-skills into separate flat folders).*

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
claude plugin install derek-agent-skills
```
Or symlink into `~/.claude/skills/derek-agent-skills` / `~/.agents/skills/derek-agent-skills`.

---

## Project-Aware Skill Suggestions & Update Checks

When loaded by invoking `/derek-agent-skills` (or `/derek-skills`, `load derek agent skill`), the router inspects the workspace directory:
- **Android / KMP Projects**: Automatically checks for Google's official `android-cli` and `android/skills`. If missing, it prompts you with the command to install them; if already installed, it prompts to check for updates (`android update` or `npx skills update`).
- **Web / Spec-Driven Projects**: Checks for `openspec`. Prompts to install or update to the latest version.
- **Universal Setup**: Offers to run `./scripts/bootstrap.sh --with-preferred` to ensure all tooling is in place.
