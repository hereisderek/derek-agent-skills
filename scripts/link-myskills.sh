#!/usr/bin/env bash

# Link the derek-skills package intact into every installed agent's skill folder.
# Keeps the internal folder structure intact (does not break into flat sub-skills).
# Run without arguments to preview (dry-run). Pass --apply to create/update symlinks.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_SOURCE="$(cd "${SCRIPT_DIR}/.." && pwd)"
SOURCE_DIR="${MY_SKILLS_DIR:-${DEFAULT_SOURCE}}"
MODE="dry-run"

case "${1:-}" in
    "") ;;
    --apply) MODE="apply" ;;
    --help|-h)
        printf 'Usage: %s [--apply]\n' "$0"
        printf 'Source: %s (override with MY_SKILLS_DIR)\n' "$SOURCE_DIR"
        exit 0
        ;;
    *)
        printf 'Unknown option: %s\n' "$1" >&2
        exit 2
        ;;
esac

if [[ ! -d "$SOURCE_DIR" || ! -f "$SOURCE_DIR/SKILL.md" ]]; then
    printf 'Valid skill package root not found at: %s\n' "$SOURCE_DIR" >&2
    exit 1
fi

DESTINATIONS=(
    "$HOME/.agents/skills"
    "$HOME/.claude/skills"
    "$HOME/.codex/skills"
    "$HOME/.gemini/skills"
    "$HOME/.config/opencode/skills"
    "$HOME/.pi/agent/skills"
)

for destination in "${DESTINATIONS[@]}"; do
    if [[ ! -d "$destination" ]]; then
        continue
    fi

    printf '\n%s\n' "$destination"

    # 1. Clean up legacy sub-skill symlinks that point into subdirectories or old agent-kit
    shopt -s nullglob
    for legacy in "$destination"/*; do
        if [[ -L "$legacy" ]]; then
            target="$(readlink "$legacy" 2>/dev/null || true)"
            if [[ "$target" == "$SOURCE_DIR/skills/"* || "$target" == *"/agent-kit/skills/"* || "$target" == *"/machine-kit-skill/skills/"* ]]; then
                if [[ "$MODE" == "apply" ]]; then
                    rm "$legacy"
                    printf '  removed sub-skill symlink: %s\n' "${legacy##*/}"
                else
                    printf '  would remove sub-skill symlink: %s\n' "${legacy##*/}"
                fi
            fi
        fi
    done
    shopt -u nullglob

    # 2. Link the unified package intact as derek-skills
    target="$destination/derek-skills"
    if [[ -L "$target" && "$(readlink "$target")" == "$SOURCE_DIR" ]]; then
        printf '  exists (intact): %s -> %s\n' "$target" "$SOURCE_DIR"
    elif [[ -e "$target" && ! -L "$target" ]]; then
        printf '  conflict (real directory/file, unchanged): %s\n' "$target" >&2
    elif [[ "$MODE" == "apply" ]]; then
        ln -sfn "$SOURCE_DIR" "$target"
        printf '  linked intact: %s -> %s\n' "$target" "$SOURCE_DIR"
    else
        printf '  would link intact: %s -> %s\n' "$target" "$SOURCE_DIR"
    fi
done

if [[ "$MODE" == "dry-run" ]]; then
    printf '\nDry run only. Re-run with --apply to apply changes.\n'
fi
