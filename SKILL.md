---
name: derek-agent-skills
description: Overview catalog and on-demand router for Derek's agent skills suite. Triggered by "load derek agent skill", "load derek agent skills", "derek-agent-skills", "derek skills", "derek agent skills", "/derek-agent-skills", or "/derek-skills". Provides a lightweight, token-efficient overview of available skills across workflow, infrastructure, mobile/KMP, animation, and multi-agent orchestration. Instructs agents to display the overview first and load specific sub-skills on demand only when relevant to the task.
---

# Derek's Agent Skills (`derek-agent-skills`, `/derek-agent-skills`, `/derek-skills`, `load derek agent skill`)

Modular suite of engineering skills, infrastructure directories, and preferred tools for AI agents.

---

## 1. Low-Context / On-Demand Loading Protocol

When invoked via **"load derek agent skill"**, **"load derek agent skills"**, **"derek-agent-skills"**, **"derek skills"**, **`/derek-agent-skills`**, or **`/derek-skills`**:

1. **Present the Overview**: Display the relevant category or the high-level catalog table below to the user.
2. **DO NOT Eagerly Ingest Sub-Skills**: Do **not** read or dump all sub-skill `SKILL.md` files into the context window at once. Keep the active context window lean.
3. **Smart On-Demand Load**: Identify which specific sub-skill matches the user's immediate task or project type, and read **only that individual skill file** (e.g., `skills/<name>/SKILL.md`) when execution is required.

---

## 2. Skills Catalog & Router

| Category | Command / Sub-Skill | Purpose | Skill Path |
|---|---|---|---|
| **Workflow & Git** | `/derek-skills:worktree-workflow` | Feature development lifecycle with Worktrunk (`wt`), worktree isolation, and PR/merge gates | [`skills/worktree-workflow/SKILL.md`](skills/worktree-workflow/SKILL.md) |
| **Workflow & Git** | `/derek-skills:release-cicd` | Semantic versioning, tag formatting, release workflows, and CI/CD policies | [`skills/release-cicd/SKILL.md`](skills/release-cicd/SKILL.md) |
| **Utilities** | `/derek-skills:markdown-converter` | Convert files/documents to Markdown via Microsoft `markitdown` | [`skills/markdown-converter/SKILL.md`](skills/markdown-converter/SKILL.md) |
| **Tool Management** | `/derek-skills:preferred-skills` | Curated skill package manager & sync CLI (`openspec`, `android/skills`, `android-cli`) | [`skills/preferred-skills/SKILL.md`](skills/preferred-skills/SKILL.md) |
| **Orchestration** | `/derek-skills:multi-agent-orchestration` | Multi-agent task planning, worker briefs, Gradle locks, validation delegation, and Coordinator cycle | [`skills/multi-agent-orchestration/SKILL.md`](skills/multi-agent-orchestration/SKILL.md) |
| **Device Testing** | `/derek-skills:state-droid-remote-device` | Discover, lease, wake/unlock, and audit remote/physical Android test devices via StageDroid (port 50370) and AVDs | [`skills/state-droid-remote-device/SKILL.md`](skills/state-droid-remote-device/SKILL.md) |
| **Mobile & KMP** | `/derek-skills:android` | Master Android & Kotlin Multiplatform development suite and verification hooks | [`skills/android/SKILL.md`](skills/android/SKILL.md) |
| **Mobile & KMP** | `/derek-skills:adaptive-ui-checklist` | Window size classes, foldables, hinges, and dual-pane ergonomics | [`skills/adaptive-ui-checklist/SKILL.md`](skills/adaptive-ui-checklist/SKILL.md) |
| **Mobile & KMP** | `/derek-skills:android-design-gallery-and-signing` | Material 3 component catalog and release keystore signing safety | [`skills/android-design-gallery-and-signing/SKILL.md`](skills/android-design-gallery-and-signing/SKILL.md) |
| **Animation** | `/derek-skills:interaction-driven-animation` | 1:1 gesture tracking, physics springs, and momentum flings | [`skills/interaction-driven-animation/SKILL.md`](skills/interaction-driven-animation/SKILL.md) |
| **Architecture** | `/derek-skills:pl-coding-skills-bundle` | Philipp Lackner 21-skill architecture bundle (Compose, MVI, Koin, navigation, error handling, testing) | [`skills/PL Coding Skills Bundle/SKILL.md`](skills/PL%20Coding%20Skills%20Bundle/SKILL.md) |
| **Infrastructure** | `/derek-skills:docker-hosts` | Execute Docker/Podman workloads on container LXCs (`docker-lxc` 2028, `podman-lxc` 2029), portbridge, and Caddy reverse proxy | [`skills/docker-hosts/SKILL.md`](skills/docker-hosts/SKILL.md) |

---

## 3. Project Context Inspection & Proactive Suggestions (On-Load Hook)

When loaded in a project directory, inspect the workspace and proactively suggest relevant tooling:

### A. Android & Kotlin Multiplatform (KMP) Projects
- **Detection**: Presence of `build.gradle`, `build.gradle.kts`, `settings.gradle`, `settings.gradle.kts`, `gradlew`, or `AndroidManifest.xml`.
- **Suggestions**:
  - If **Android CLI (`android-cli`)** is missing, offer: `npx --yes skills add android/skills -g --skill android-cli -y`. If installed, offer update check.
  - If **`android/skills` (Full Suite)** is missing, offer: `npx --yes skills add android/skills -g --full-depth -y`.
  - Recommend relevant internal skills: `android`, `adaptive-ui-checklist`, `state-droid-remote-device`, or `PL Coding Skills Bundle`.

### B. Web, TypeScript, or Spec-Driven Projects
- **Detection**: Presence of `package.json`, `tsconfig.json`, `pnpm-workspace.yaml`, or `specs/`.
- **Suggestions**:
  - If **OpenSpec (`openspec`)** is missing, offer: `npm install -g @fission-ai/openspec@latest`.

---

## 4. Companion Repository Note

Global agent behavioral rules (`rules/`) and machine-specific profiles (`machines/mac.md`, `agent-lxc.md`, `generic.md`) live in [hereisderek/machine-kit-skill](https://github.com/hereisderek/machine-kit-skill) (formerly `agent-kit`).
