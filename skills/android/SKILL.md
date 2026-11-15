---
name: android
description: Master Android & Kotlin Multiplatform (KMP) development suite covering (1) Material Design 3, subtle dev Component Gallery, dynamic theme updates & signing keys, (2) Interaction-driven animations (1:1 gesture tracking, momentum fling), and (3) Mobile orchestration verification presets. Use to architect, build, preview, or test any Android or KMP application.
---

# Android & KMP Engineering Suite (`android`)

Master playbook and router for modern Android and Kotlin Multiplatform (KMP) engineering. Covers foundation setup, design systems with live-themed in-app component galleries, gesture-driven motion, and orchestration validation presets.

## When to Use

- Architecting, structuring, or reviewing Android and Kotlin Multiplatform projects
- Designing with Material Design 3, building subtle in-app Component Galleries with real-time theme updates and Material You Expressive dynamic colour, and managing safe signing keys
- Implementing gesture-triggered animations (collapsing headers, bottom sheets, carousels, swipe actions, pull-to-refresh) following `interaction-driven-animation`
- Integrating mobile-specific verification commands (`flock /tmp/dtm-gradle.lock`, APK assemble, device smoke testing) with `multi-agent-orchestration`

---

## Sub-Skills & Modules

| Module | Location | Description |
| --- | --- | --- |
| **Design, Gallery & Signing** | [`android-design-gallery-and-signing`](../android-design-gallery-and-signing/SKILL.md) | Material Design 3, window insets, subtle dev-build Component Gallery with live theme updating, Material You Expressive dynamic colour, deterministic dummy data, and debug/release keystores |
| **Interaction-Driven Motion** | [`interaction-driven-animation`](../interaction-driven-animation/SKILL.md) | 1:1 user touch tracking, momentum fling/spring on release, and instant halting without jump on touch interruption |
| **Orchestration Preset** | [`mobile-orchestration-preset.md`](mobile-orchestration-preset.md) | Pluggable verification commands for `multi-agent-orchestration` |

---

## Installation Options

- **Install as a Whole Suite**:
  ```bash
  npx skills add hereisderek/derek-agent-skills -g --skill android --full-depth -y
  ```
- **Install Individual Sub-Skills**:
  ```bash
  npx skills add hereisderek/derek-agent-skills -g --skill android-design-gallery-and-signing -y
  npx skills add hereisderek/derek-agent-skills -g --skill interaction-driven-animation -y
  ```
