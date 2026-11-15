---
description: Derek's agent skills suite router. Inspects the project and suggests or updates relevant skills.
---

# /derek-skills

Load Derek's agent skills suite router.

## What it does

1. **Inspects Project Context**:
   - Detects Android/KMP workspaces (Gradle, AndroidManifest) or Web/TypeScript workspaces (package.json, tsconfig).
2. **Proactively Recommends Skills**:
   - Suggests installing or updating `android-cli` and official `android/skills` for Android projects.
   - Suggests installing or updating `openspec` for spec-driven web projects.
3. **Provides Sub-Skill Routing**:
   - `/derek-skills:hosts`
   - `/derek-skills:preferred-skills`
   - `/derek-skills:android`
   - `/derek-skills:multi-agent-orchestration`
   - `/derek-skills:interaction-driven-animation`
   - `/derek-skills:android-design-gallery-and-signing`
   - `/derek-skills:adaptive-ui-checklist`
   - `/derek-skills:pl-coding-skills-bundle`

## Reference Skill

Read the full router specification at:
`SKILL.md`
