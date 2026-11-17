---
description: Load Derek's agent skills suite overview and router. Triggered by "load derek agent skill", "load derek agent skills", "derek skills", or /derek-skills.
---

# /derek-skills (`load derek agent skill`)

Load Derek's agent skills suite router.

## What it does

1. **Presents a Token-Efficient Overview**:
   - Shows a structured table of all available engineering, infrastructure, workflow, and architecture skills without flooding the context window.
2. **On-Demand Loading Discipline**:
   - Instructs the agent to load only the specific sub-skill needed for the current task.
3. **Inspects Project Context**:
   - Detects Android/KMP workspaces (Gradle, AndroidManifest) or Web/TypeScript workspaces (package.json, tsconfig).
   - Proactively suggests installing or updating `android-cli`, `android/skills`, or `openspec`.

## Reference Skill

Read the full router specification at:
`SKILL.md`
