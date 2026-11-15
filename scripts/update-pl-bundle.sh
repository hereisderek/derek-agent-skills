#!/usr/bin/env bash
#
# update-pl-bundle.sh
# Safely updates the Philipp Lackner (PL) Coding Skills Bundle from an upstream Google Drive zip.
#
# Upstream Google Drive link:
# https://drive.google.com/file/d/1ymCdsrztthwg2OsfEwWpKhS0e3TpOvGG/view
#
# Usage:
#   ./scripts/update-pl-bundle.sh /path/to/downloaded-bundle.zip
#   ./scripts/update-pl-bundle.sh --url-only
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

SUBMODULE_DIR="${REPO_ROOT}/skills/PL Coding Skills Bundle"
STANDALONE_DIR="/Volumes/private/workspace/my-skills/PL Coding Skills Bundle"
DRIVE_URL="https://drive.google.com/file/d/1ymCdsrztthwg2OsfEwWpKhS0e3TpOvGG/view"

# Target directory preference: standalone workspace directory if it exists, otherwise submodule directory
if [[ -d "$STANDALONE_DIR/.git" ]]; then
    TARGET_DIR="$STANDALONE_DIR"
else
    TARGET_DIR="$SUBMODULE_DIR"
fi

show_help() {
    cat <<EOF
Usage: $0 [OPTIONS] [PATH_TO_ZIP]

Updates the Philipp Lackner Coding Skills Bundle from an upstream zip archive.

Options:
  -u, --url       Print the upstream Google Drive download link and exit.
  -h, --help      Show this help message and exit.

Arguments:
  PATH_TO_ZIP     Path to the downloaded Google Drive zip archive.

Upstream Link:
  ${DRIVE_URL}
EOF
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
    show_help
    exit 0
fi

if [[ "${1:-}" == "--url" || "${1:-}" == "-u" || "${1:-}" == "--url-only" ]]; then
    echo "$DRIVE_URL"
    exit 0
fi

ZIP_PATH="${1:-}"

if [[ -z "$ZIP_PATH" ]]; then
    echo "Error: No zip file specified." >&2
    echo "" >&2
    echo "1. Download the latest bundle from Google Drive:" >&2
    echo "   $DRIVE_URL" >&2
    echo "2. Run this script pointing to the downloaded zip file:" >&2
    echo "   $0 ~/Downloads/<bundle-filename>.zip" >&2
    exit 1
fi

if [[ ! -f "$ZIP_PATH" ]]; then
    echo "Error: Specified file does not exist: $ZIP_PATH" >&2
    exit 1
fi

if [[ ! -d "$TARGET_DIR" ]]; then
    echo "Error: Target directory does not exist: $TARGET_DIR" >&2
    exit 1
fi

echo "============================================================"
echo "Updating Philipp Lackner Coding Skills Bundle"
echo "Target: $TARGET_DIR"
echo "Source: $ZIP_PATH"
echo "============================================================"

TMP_EXTRACT=$(mktemp -d "/tmp/pl-bundle-update.XXXXXX")
trap 'rm -rf "$TMP_EXTRACT"' EXIT

echo "--> Unpacking zip to temporary folder..."
unzip -q "$ZIP_PATH" -d "$TMP_EXTRACT"

# Detect if the zip extracted into a single top-level directory or directly into root
SOURCE_CONTENT="$TMP_EXTRACT"
shopt -s nullglob
TOP_LEVEL_ITEMS=("$TMP_EXTRACT"/*)
if [[ ${#TOP_LEVEL_ITEMS[@]} -eq 1 && -d "${TOP_LEVEL_ITEMS[0]}" ]]; then
    # e.g. zip had a folder inside like "PL Coding Skills Bundle"
    SOURCE_CONTENT="${TOP_LEVEL_ITEMS[0]}"
fi

# Sanity check: verify expected directories exist in the extracted contents
MATCH_COUNT=0
for expected in "android-compose-components" "android-data-layer" "kmp-data-layer" "android-presentation-mvi"; do
    if [[ -d "$SOURCE_CONTENT/$expected" ]]; then
        MATCH_COUNT=$((MATCH_COUNT + 1))
    fi
done

if [[ $MATCH_COUNT -eq 0 ]]; then
    echo "Warning: Did not find standard PL skill directories in the extracted root." >&2
    echo "Contents found:" >&2
    ls -la "$SOURCE_CONTENT" >&2
    read -r -p "Continue sync anyway? [y/N] " CONFIRM
    if [[ "$CONFIRM" != [yY]* ]]; then
        echo "Aborted."
        exit 1
    fi
fi

echo "--> Syncing updated skill directories into $TARGET_DIR..."
# Preserve .git, .gitignore, root SKILL.md, and root README.md
rsync -av \
    --exclude='.git' \
    --exclude='.gitignore' \
    --exclude='SKILL.md' \
    --exclude='README.md' \
    --exclude='.DS_Store' \
    --delete \
    "$SOURCE_CONTENT/" "$TARGET_DIR/"

# Remove any stray .DS_Store files
find "$TARGET_DIR" -name ".DS_Store" -delete 2>/dev/null || true

echo "--> Checking git status in $TARGET_DIR..."
if git -C "$TARGET_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    STATUS_OUT=$(git -C "$TARGET_DIR" status --short)
    if [[ -z "$STATUS_OUT" ]]; then
        echo "✓ No changes detected; target is already up-to-date with this archive."
    else
        echo "Changes detected in $TARGET_DIR:"
        echo "$STATUS_OUT"
        echo ""
        read -r -p "Commit and push changes to pl-coding-skills-bundle repo? [y/N] " COMMIT_CONFIRM
        if [[ "$COMMIT_CONFIRM" == [yY]* ]]; then
            git -C "$TARGET_DIR" add -A
            git -C "$TARGET_DIR" commit -m "chore(pl-bundle): update skills from upstream Google Drive snapshot"
            git -C "$TARGET_DIR" push origin master
            echo "✓ Pushed changes to pl-coding-skills-bundle repository."

            # If target was standalone, also pull changes into derek-agent-skills submodule
            if [[ "$TARGET_DIR" != "$SUBMODULE_DIR" && -d "$SUBMODULE_DIR" ]]; then
                echo "--> Updating submodule in derek-agent-skills..."
                git -C "$REPO_ROOT" submodule update --remote "skills/PL Coding Skills Bundle"
                echo "Submodule updated. You can commit the submodule pointer update in derek-agent-skills when ready."
            fi
        else
            echo "Skipped commit. Changes remain uncommitted in $TARGET_DIR."
        fi
    fi
fi

echo "============================================================"
echo "Update complete!"
echo "============================================================"
