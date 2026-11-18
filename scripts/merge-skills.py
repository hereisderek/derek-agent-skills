#!/usr/bin/env python3
"""
merge-skills.py
Consolidates all modular skills within derek-agent-skills into a single self-contained SKILL.merged.md file.
Preserves 100% unabridged content, extracts metadata into structured headers, and provides a master Table of Contents.
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
OUTPUT_FILE = os.path.join(REPO_ROOT, "SKILL.merged.md")

SKILL_SPECS = [
    # Part 0: Suite Router & Catalog
    {
        "category": "Part 0: Suite Catalog & On-Demand Router",
        "anchor": "derek-agent-skills",
        "file": "SKILL.md",
        "override_name": "derek-agent-skills",
        "command": "/derek-skills",
    },
    # Part 1: Git & Workflow Automation
    {
        "category": "Part 1: Git & Workflow Automation",
        "anchor": "worktree-workflow",
        "file": "skills/worktree-workflow/SKILL.md",
        "command": "/derek-skills:worktree-workflow",
    },
    {
        "category": "Part 1: Git & Workflow Automation",
        "anchor": "release-cicd",
        "file": "skills/release-cicd/SKILL.md",
        "command": "/derek-skills:release-cicd",
    },
    # Part 2: Tooling & Infrastructure
    {
        "category": "Part 2: Tooling & Infrastructure",
        "anchor": "markdown-converter",
        "file": "skills/markdown-converter/SKILL.md",
        "command": "/derek-skills:markdown-converter",
    },
    {
        "category": "Part 2: Tooling & Infrastructure",
        "anchor": "preferred-skills",
        "file": "skills/preferred-skills/SKILL.md",
        "command": "/derek-skills:preferred-skills",
    },
    {
        "category": "Part 2: Tooling & Infrastructure",
        "anchor": "multi-agent-orchestration",
        "file": "skills/multi-agent-orchestration/SKILL.md",
        "command": "/derek-skills:multi-agent-orchestration",
    },
    {
        "category": "Part 2: Tooling & Infrastructure",
        "anchor": "docker-hosts",
        "file": "skills/docker-hosts/SKILL.md",
        "command": "/derek-skills:docker-hosts",
    },
    # Part 3: Mobile, Device Testing & Animation
    {
        "category": "Part 3: Mobile, Device Testing & Animation",
        "anchor": "state-droid-remote-device",
        "file": "skills/state-droid-remote-device/SKILL.md",
        "command": "/derek-skills:state-droid-remote-device",
    },
    {
        "category": "Part 3: Mobile, Device Testing & Animation",
        "anchor": "android",
        "file": "skills/android/SKILL.md",
        "command": "/derek-skills:android",
    },
    {
        "category": "Part 3: Mobile, Device Testing & Animation",
        "anchor": "mobile-orchestration-preset",
        "file": "skills/android/mobile-orchestration-preset.md",
        "override_name": "mobile-orchestration-preset",
        "override_desc": "Verification commands and lifecycle hooks for Android and Kotlin Multiplatform multi-agent orchestration.",
        "command": None,
    },
    {
        "category": "Part 3: Mobile, Device Testing & Animation",
        "anchor": "adaptive-ui-checklist",
        "file": "skills/adaptive-ui-checklist/SKILL.md",
        "command": "/derek-skills:adaptive-ui-checklist",
    },
    {
        "category": "Part 3: Mobile, Device Testing & Animation",
        "anchor": "android-design-gallery-and-signing",
        "file": "skills/android-design-gallery-and-signing/SKILL.md",
        "command": "/derek-skills:android-design-gallery-and-signing",
    },
    {
        "category": "Part 3: Mobile, Device Testing & Animation",
        "anchor": "interaction-driven-animation",
        "file": "skills/interaction-driven-animation/SKILL.md",
        "command": "/derek-skills:interaction-driven-animation",
    },
    # Part 4: Philipp Lackner (PL) Architecture Bundle
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-coding-skills-bundle",
        "file": "skills/PL Coding Skills Bundle/SKILL.md",
        "command": "/derek-skills:pl-coding-skills-bundle",
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-android-module-structure",
        "file": "skills/PL Coding Skills Bundle/android-module-structure/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-android-presentation-mvi",
        "file": "skills/PL Coding Skills Bundle/android-presentation-mvi/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-android-compose-components",
        "file": "skills/PL Coding Skills Bundle/android-compose-components/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-android-navigation",
        "file": "skills/PL Coding Skills Bundle/android-navigation/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-android-di-koin",
        "file": "skills/PL Coding Skills Bundle/android-di-koin/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-android-data-layer",
        "file": "skills/PL Coding Skills Bundle/android-data-layer/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-android-error-handling",
        "file": "skills/PL Coding Skills Bundle/android-error-handling/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-android-unit-testing",
        "file": "skills/PL Coding Skills Bundle/android-unit-testing/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-android-ui-testing",
        "file": "skills/PL Coding Skills Bundle/android-ui-testing/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-design",
        "file": "skills/PL Coding Skills Bundle/design/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-kmp-module-structure",
        "file": "skills/PL Coding Skills Bundle/kmp-module-structure/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-kmp-compose-architecture",
        "file": "skills/PL Coding Skills Bundle/kmp-compose-architecture/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-kmp-compose-components",
        "file": "skills/PL Coding Skills Bundle/kmp-compose-components/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-kmp-presentation-mvi",
        "file": "skills/PL Coding Skills Bundle/kmp-presentation-mvi/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-kmp-navigation",
        "file": "skills/PL Coding Skills Bundle/kmp-navigation/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-kmp-di-koin",
        "file": "skills/PL Coding Skills Bundle/kmp-di-koin/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-kmp-data-layer",
        "file": "skills/PL Coding Skills Bundle/kmp-data-layer/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-kmp-error-handling",
        "file": "skills/PL Coding Skills Bundle/kmp-error-handling/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-kmp-unit-testing",
        "file": "skills/PL Coding Skills Bundle/kmp-unit-testing/SKILL.md",
        "command": None,
    },
    {
        "category": "Part 4: Philipp Lackner (PL) Architecture Bundle",
        "anchor": "pl-pr-quiz",
        "file": "skills/PL Coding Skills Bundle/pr-quiz/SKILL.md",
        "command": None,
    },
]

def parse_skill_file(filepath):
    """Parses a markdown skill file, extracting YAML frontmatter fields and body."""
    abs_path = os.path.join(REPO_ROOT, filepath)
    with open(abs_path, "r", encoding="utf-8") as f:
        text = f.read()

    name = None
    desc = None
    body = text

    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            frontmatter = parts[1].strip()
            body = parts[2].strip()

            desc_lines = []
            in_desc = False
            for line in frontmatter.split("\n"):
                if line.startswith("name:"):
                    name = line.split("name:", 1)[1].strip()
                    in_desc = False
                elif line.startswith("description:"):
                    in_desc = True
                    rest = line.split("description:", 1)[1].strip()
                    if rest and rest not in (">-", "|", ">"):
                        desc_lines.append(rest)
                elif in_desc:
                    if line.startswith("  ") or line.startswith("\t"):
                        desc_lines.append(line.strip())
                    elif not line.strip():
                        continue
                    else:
                        in_desc = False
            if desc_lines:
                desc = " ".join(desc_lines).strip()

    # Extract first heading from body
    first_heading = None
    for line in body.split("\n"):
        if line.startswith("#"):
            first_heading = line.lstrip("#").strip()
            break

    return name, desc, first_heading, body

def main():
    print("Collecting skills and parsing metadata...")
    parsed_entries = []
    for spec in SKILL_SPECS:
        name, desc, first_heading, body = parse_skill_file(spec["file"])
        entry = {
            "category": spec["category"],
            "anchor": spec["anchor"],
            "file": spec["file"],
            "name": spec.get("override_name") or name or spec["anchor"],
            "desc": spec.get("override_desc") or desc or "",
            "heading": first_heading or spec["anchor"],
            "command": spec.get("command"),
            "body": body,
        }
        parsed_entries.append(entry)

    print(f"Parsed {len(parsed_entries)} skill entries.")

    lines = []

    # Master YAML Frontmatter
    lines.append("---")
    lines.append("name: derek-agent-skills")
    lines.append("description: >-")
    lines.append("  Consolidated single-file edition of Derek's complete agent skills suite (derek-agent-skills).")
    lines.append("  Merges all 32 modular engineering, workflow, infrastructure, testing, and architecture skills")
    lines.append("  into one self-contained reference, including Worktrunk worktrees, release CI/CD, markdown conversion,")
    lines.append("  preferred skills, multi-agent orchestration, StageDroid remote device management, Android/KMP suite,")
    lines.append("  adaptive UI checklist, Android design gallery & signing, interaction-driven animation, Docker hosts,")
    lines.append("  and the complete 20-skill Philipp Lackner Android & KMP Architecture Bundle.")
    lines.append("---")
    lines.append("")

    # Master Document Header
    lines.append("# Derek's Agent Skills — Consolidated Edition (`SKILL.merged.md`)")
    lines.append("")
    lines.append("> **Single-File Consolidated Edition**  ")
    lines.append("> Merges all 32 engineering skills, infrastructure guides, and architecture references within the `derek-agent-skills` repository into one comprehensive document.  ")
    lines.append("> Every sub-skill is included **100% unabridged** with all rules, code templates, scripts, tables, and workflows fully preserved.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Master Table of Contents
    lines.append("## Master Table of Contents")
    lines.append("")

    current_cat = None
    cat_idx = 0
    sub_idx = 0
    for entry in parsed_entries:
        if entry["category"] != current_cat:
            current_cat = entry["category"]
            lines.append(f"### {current_cat}")
            lines.append("")
            sub_idx = 1
        else:
            sub_idx += 1

        cmd_badge = f" (`{entry['command']}`)" if entry["command"] else ""
        short_desc = entry["desc"]
        if len(short_desc) > 130:
            short_desc = short_desc[:127] + "..."
        desc_part = f" — {short_desc}" if short_desc else ""
        lines.append(f"- [{entry['heading']}](#{entry['anchor']}){cmd_badge}{desc_part}")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Skill Bodies
    current_cat = None
    for entry in parsed_entries:
        if entry["category"] != current_cat:
            current_cat = entry["category"]
            lines.append(f"# {current_cat}")
            lines.append("")

        lines.append(f'<a id="{entry["anchor"]}"></a>')
        lines.append("")
        lines.append(f"> **Sub-Skill Identity:** `{entry['name']}`  ")
        if entry["command"]:
            lines.append(f"> **Command:** `{entry['command']}`  ")
        lines.append(f"> **Source File:** [`{entry['file']}`]({entry['file']})  ")
        if entry["desc"]:
            lines.append(f"> **Description:** {entry['desc']}  ")
        lines.append("")

        lines.append(entry["body"])
        lines.append("")
        lines.append("---")
        lines.append("")

    content = "\n".join(lines)

    total_lines = content.count("\n") + 1
    print(f"Writing {len(content)} characters ({total_lines} lines) to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    file_size_kb = os.path.getsize(OUTPUT_FILE) / 1024
    print(f"Successfully generated {OUTPUT_FILE} ({file_size_kb:.1f} KB, {total_lines} lines)!")

if __name__ == "__main__":
    main()
