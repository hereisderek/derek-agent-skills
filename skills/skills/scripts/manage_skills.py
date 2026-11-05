#!/usr/bin/env python3
"""Preferred skills manager for Derek's AI agents.

Manages, inspects, and installs preferred skills with automatic symlinking
into universal and agent-specific skill directories (~/.agents/skills, ~/.claude/skills, etc.).
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CATALOG_PATH = BASE_DIR / "skills.json"

UNIVERSAL_SKILLS_DIR = Path(os.path.expanduser("~/.agents/skills"))
ALT_AGENTS_DIR = Path(os.path.expanduser("~/agents"))
DOT_AGENTS_DIR = Path(os.path.expanduser("~/.agents"))

AGENT_DIRS = [
    Path(os.path.expanduser("~/.claude/skills")),
    Path(os.path.expanduser("~/.codex/skills")),
    Path(os.path.expanduser("~/.gemini/skills")),
    Path(os.path.expanduser("~/.config/opencode/skills")),
    Path(os.path.expanduser("~/.continue/skills")),
    Path(os.path.expanduser("~/.copilot/skills")),
]


def load_catalog() -> list[dict]:
    if not CATALOG_PATH.exists():
        return []
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def ensure_agents_symlinks():
    """Ensure ~/agents points to ~/.agents for compatibility."""
    if not DOT_AGENTS_DIR.exists():
        DOT_AGENTS_DIR.mkdir(parents=True, exist_ok=True)
    UNIVERSAL_SKILLS_DIR.mkdir(parents=True, exist_ok=True)

    if not ALT_AGENTS_DIR.exists() and not ALT_AGENTS_DIR.is_symlink():
        try:
            ALT_AGENTS_DIR.symlink_to(DOT_AGENTS_DIR)
            print(f"Created symlink: {ALT_AGENTS_DIR} -> {DOT_AGENTS_DIR}")
        except Exception as e:
            # Ignore failure if permissions disallow writing to ~
            pass


def is_installed(item: dict) -> bool:
    check_cmd = item.get("checkCommand")
    if check_cmd:
        ret = subprocess.run(check_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if ret.returncode == 0:
            return True

    check_path_str = item.get("checkPath")
    if check_path_str:
        p = Path(os.path.expanduser(check_path_str))
        if p.exists() or p.is_symlink():
            return True

    # Fallback: check ~/.agents/skills/<id>
    local_path = UNIVERSAL_SKILLS_DIR / item["id"]
    return local_path.exists() or local_path.is_symlink()


def link_skills_to_agents():
    """Ensure all skills in ~/.agents/skills are linked into active agent skill directories."""
    UNIVERSAL_SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    installed_skills = [p for p in UNIVERSAL_SKILLS_DIR.iterdir() if p.is_dir() or p.is_symlink()]

    linked_count = 0
    for agent_dir in AGENT_DIRS:
        if not agent_dir.parent.exists():
            continue
        agent_dir.mkdir(parents=True, exist_ok=True)
        for skill in installed_skills:
            target_link = agent_dir / skill.name
            if not target_link.exists() and not target_link.is_symlink():
                try:
                    target_link.symlink_to(skill)
                    linked_count += 1
                except Exception as e:
                    print(f"Warning: could not link {skill.name} to {target_link}: {e}", file=sys.stderr)

    if linked_count > 0:
        print(f"Linked {linked_count} skill symlink(s) into agent directories.")


def cmd_list(args):
    catalog = load_catalog()
    if args.json:
        results = []
        for item in catalog:
            copy = dict(item)
            copy["installed"] = is_installed(item)
            results.append(copy)
        print(json.dumps(results, indent=2))
        return

    print("=" * 80)
    print("Derek's Preferred Skills Catalog")
    print("=" * 80)
    for idx, item in enumerate(catalog, 1):
        status = "✓ [Installed]" if is_installed(item) else "✗ [Not Installed]"
        print(f"\n{idx}. {item['name']} ({item['id']})  {status}")
        print(f"   Description : {item.get('description', '')}")
        print(f"   Repository  : {item.get('repo', '')}")
        if item.get("npm"):
            print(f"   NPM / NPX   : {item['npm']}")
        print(f"   Install Cmd : {item.get('installCommand', '')}")
    print("\n" + "=" * 80)


def install_item(item: dict) -> bool:
    print(f"\n---> Installing {item['name']}...")
    install_cmd = item.get("installCommand")
    if not install_cmd:
        print(f"Error: No install command specified for {item['id']}", file=sys.stderr)
        return False

    print(f"Running: {install_cmd}")
    ret = subprocess.run(install_cmd, shell=True)
    if ret.returncode != 0:
        print(f"Failed to install {item['name']} (exit code {ret.returncode})", file=sys.stderr)
        return False

    link_skills_to_agents()
    print(f"Successfully installed and linked {item['name']}.")
    return True


def cmd_install(args):
    catalog = load_catalog()
    by_id = {item["id"]: item for item in catalog}
    targets = []

    if args.all:
        targets = catalog
    else:
        for name in args.skills:
            if name in by_id:
                targets.append(by_id[name])
            else:
                print(f"Unknown skill '{name}'. Available: {', '.join(by_id.keys())}", file=sys.stderr)

    if not targets:
        print("No skills specified to install. Use --all or provide skill IDs.")
        return

    ensure_agents_symlinks()
    success = 0
    for item in targets:
        if install_item(item):
            success += 1

    print(f"\nInstalled {success}/{len(targets)} skill(s).")


def cmd_interactive(args):
    catalog = load_catalog()
    ensure_agents_symlinks()

    print("=" * 80)
    print("Select skills to install:")
    print("=" * 80)
    for idx, item in enumerate(catalog, 1):
        status = "✓ [Installed]" if is_installed(item) else "  [Available]"
        print(f"[{idx}] {item['name']} - {status}")
        print(f"    Repo: {item.get('repo', '')}")

    print("\nOptions:")
    print("  Enter numbers separated by space (e.g. '1 2')")
    print("  'all' to install everything")
    print("  'q' to cancel")

    try:
        choice = input("\nEnter selection: ").strip()
    except EOFError:
        print("No input received. Exiting.")
        return

    if choice.lower() == 'q' or not choice:
        print("Aborted.")
        return

    if choice.lower() == 'all':
        selected = catalog
    else:
        indices = []
        for part in choice.split():
            try:
                idx = int(part)
                if 1 <= idx <= len(catalog):
                    indices.append(idx - 1)
            except ValueError:
                pass
        selected = [catalog[i] for i in indices]

    if not selected:
        print("No valid selection.")
        return

    for item in selected:
        install_item(item)


def main():
    parser = argparse.ArgumentParser(description="Derek's Preferred Skills Manager")
    subparsers = parser.add_subparsers(dest="command")

    # list
    p_list = subparsers.add_parser("list", help="List preferred skills and installation status")
    p_list.add_argument("--json", action="store_true", help="Output as JSON")

    # install
    p_inst = subparsers.add_parser("install", help="Install preferred skills")
    p_inst.add_argument("--all", action="store_true", help="Install all skills in catalog")
    p_inst.add_argument("skills", nargs="*", help="Skill IDs to install")

    # interactive
    subparsers.add_parser("select", help="Interactively select skills to install")
    subparsers.add_parser("interactive", help="Interactively select skills to install")

    # sync
    subparsers.add_parser("sync", help="Symlink ~/.agents/skills into agent skill directories")

    args = parser.parse_args()

    if args.command == "list":
        cmd_list(args)
    elif args.command == "install":
        cmd_install(args)
    elif args.command in ("select", "interactive"):
        cmd_interactive(args)
    elif args.command == "sync":
        ensure_agents_symlinks()
        link_skills_to_agents()
    else:
        # Default behavior: show list
        cmd_list(argparse.Namespace(json=False))


if __name__ == "__main__":
    main()
