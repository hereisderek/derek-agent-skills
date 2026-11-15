---
name: derek-skills
description: Derek's collection of reusable engineering skills, preferred skills manager, and infrastructure host connection directory. Invoked via `/derek-skills`, `/derek agentic skill`, or sub-category `/derek-skills:<category>`. When loaded, checks current project context and proactively suggests or updates relevant skills.
---

# Derek's Agent Skills (`/derek-skills`, `/derek agentic skill`)

Modular suite of engineering skills, preferred skills manager, and infrastructure host directory for AI agents.

---

## 1. Project Context Inspection & Proactive Skill Suggestion (On-Load Hook)

**When this skill is loaded by invoking `/derek-skills`, `/derek agentic skill`, or during agent startup:**  
The agent **MUST** inspect the active workspace directory and proactively suggest installing or updating the appropriate skills based on the project type:

### A. Android & Kotlin Multiplatform (KMP) Projects
- **Detection**: Presence of `build.gradle`, `build.gradle.kts`, `settings.gradle`, `settings.gradle.kts`, `gradlew`, or `AndroidManifest.xml`.
- **Skill Checks & Prompts**:
  1. **Android CLI (`android-cli`)**:
     - Check via `command -v android` or checking `~/.agents/skills/android-cli`.
     - *If NOT installed*: Prompt the user:
       > "Detected an Android/KMP project. Would you like me to install the official **Android CLI** (`android-cli`)? Run: `npx --yes skills add android/skills -g --skill android-cli -y`"
     - *If ALREADY installed*: Prompt the user:
       > "Android CLI is installed. Would you like to check for updates? (`android update` or `npx --yes skills update`)"
  2. **android/skills (The Full Suite)**:
     - Check via `grep -q 'android/skills' ~/.agents/.skill-lock.json 2>/dev/null || test -d ~/.agents/skills/adaptive`.
     - *If NOT installed*: Prompt to install via `npx --yes skills add android/skills -g --full-depth -y`.
     - *If ALREADY installed*: Prompt if an update check is desired (`npx --yes skills update`).
  3. **Internal Suite Recommendations**:
     - Route to [`skills/android/SKILL.md`](skills/android/SKILL.md), [`skills/adaptive-ui-checklist/SKILL.md`](skills/adaptive-ui-checklist/SKILL.md), [`skills/android-design-gallery-and-signing/SKILL.md`](skills/android-design-gallery-and-signing/SKILL.md), [`skills/interaction-driven-animation/SKILL.md`](skills/interaction-driven-animation/SKILL.md), and [`skills/PL Coding Skills Bundle/SKILL.md`](skills/PL%20Coding%20Skills%20Bundle/SKILL.md).

### B. Web, TypeScript, or Spec-Driven Projects
- **Detection**: Presence of `package.json`, `tsconfig.json`, `pnpm-workspace.yaml`, or specification directories (`specs/`, `openspec/`).
- **Skill Checks & Prompts**:
  - **OpenSpec (`openspec`)**:
    - Check via `command -v openspec`.
    - *If NOT installed*: Prompt user:
      > "Detected a web/spec-driven workspace. Install **OpenSpec** for SDD workflows (`/opsx:explore`, `/opsx:propose`)? Run: `npm install -g @fission-ai/openspec@latest`"
    - *If ALREADY installed*: Prompt if the user wants to update to latest.

### C. One-Command Setup for All Preferred Skills
To install all preferred skills together (OpenSpec, Android CLI, Android Skills Suite):
```bash
./scripts/bootstrap.sh --with-preferred
# or directly via the manager CLI:
./skills/preferred-skills/scripts/manage_skills.sh install --all
```

---

## 2. Sub-Category Routing (`/derek-skills:<sub category>`)

| Command / Syntax | Purpose | Skill Location |
| --- | --- | --- |
| `/derek-skills:hosts` | Infrastructure directory, SSH aliases & Gist mapping snapshot | [skills/hosts/SKILL.md](skills/hosts/SKILL.md) |
| `/derek-skills:preferred-skills` | Preferred skills catalog & installer (OpenSpec, Android skills, etc.) | [skills/preferred-skills/SKILL.md](skills/preferred-skills/SKILL.md) |
| `/derek-skills:android` | Master Android & Kotlin Multiplatform suite router | [skills/android/SKILL.md](skills/android/SKILL.md) |
| `/derek-skills:multi-agent-orchestration` | Multi-agent planning, dispatch, validation, or handoff | [skills/multi-agent-orchestration/SKILL.md](skills/multi-agent-orchestration/SKILL.md) |
| `/derek-skills:interaction-driven-animation` | 1:1 touch/gesture tracking & momentum flings | [skills/interaction-driven-animation/SKILL.md](skills/interaction-driven-animation/SKILL.md) |
| `/derek-skills:android-design-gallery-and-signing` | Material 3 component gallery & keystore safety | [skills/android-design-gallery-and-signing/SKILL.md](skills/android-design-gallery-and-signing/SKILL.md) |
| `/derek-skills:adaptive-ui-checklist` | Window size classes, foldables, and dual-pane ergonomics | [skills/adaptive-ui-checklist/SKILL.md](skills/adaptive-ui-checklist/SKILL.md) |
| `/derek-skills:pl-coding-skills-bundle` | Philipp Lackner Android & KMP architecture and coding bundle | [skills/PL Coding Skills Bundle/SKILL.md](skills/PL%20Coding%20Skills%20Bundle/SKILL.md) |

> **Live Infrastructure Snapshot (Gist):**  
> 🔗 [https://gist.github.com/hereisderek/9d10d746711c34f3b20c1a07282237f3](https://gist.github.com/hereisderek/9d10d746711c34f3b20c1a07282237f3)

The worktree workflow, release/CI-CD policy, markdown conversion and global rules live in [hereisderek/agent-kit](https://github.com/hereisderek/agent-kit).
