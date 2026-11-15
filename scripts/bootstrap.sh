#!/usr/bin/env bash
#
# bootstrap.sh
# Initializes derek-agent-skills submodules, configures agent symlinks,
# and optionally installs preferred skills (OpenSpec, Android CLI, Android skills).
#
# Usage:
#   ./scripts/bootstrap.sh                    # Setup submodules & canonical symlinks
#   ./scripts/bootstrap.sh --with-preferred   # Also install all preferred skills
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
INSTALL_PREFERRED=false

for arg in "$@"; do
    case "$arg" in
        --with-preferred|--all|-a)
            INSTALL_PREFERRED=true
            ;;
        --help|-h)
            echo "Usage: $0 [--with-preferred|--all]"
            echo "  --with-preferred, --all  Also install all curated preferred skills (OpenSpec, Android skills, Android CLI)"
            exit 0
            ;;
    esac
done

echo "============================================================"
echo "Bootstrapping derek-agent-skills"
echo "Repo root: $REPO_ROOT"
echo "============================================================"

# 1. Initialize and update submodules
echo "--> Initializing and updating Git submodules..."
git -C "$REPO_ROOT" submodule update --init --recursive
echo "✓ Submodules up-to-date."

# 2. Setup ~/.agents/skills/derek-skills symlink
AGENTS_SKILLS_DIR="$HOME/.agents/skills"
mkdir -p "$AGENTS_SKILLS_DIR"

TARGET_LINK="$AGENTS_SKILLS_DIR/derek-skills"
if [[ -L "$TARGET_LINK" && "$(readlink "$TARGET_LINK")" == "$REPO_ROOT" ]]; then
    echo "✓ Canonical symlink already exists: $TARGET_LINK -> $REPO_ROOT"
else
    ln -sfn "$REPO_ROOT" "$TARGET_LINK"
    echo "✓ Created/updated canonical symlink: $TARGET_LINK -> $REPO_ROOT"
fi

# 3. Optional: Ensure ~/agents compatibility symlink if ~/.agents exists
if [[ -d "$HOME/.agents" && ! -e "$HOME/agents" && ! -L "$HOME/agents" ]]; then
    ln -s "$HOME/.agents" "$HOME/agents" 2>/dev/null || true
    echo "✓ Created compatibility symlink: ~/agents -> ~/.agents"
fi

# 4. Optional: Install preferred skills if requested
if [[ "$INSTALL_PREFERRED" == true ]]; then
    echo ""
    echo "--> Installing all preferred skills from catalog..."
    "${REPO_ROOT}/skills/preferred-skills/scripts/manage_skills.sh" install --all
fi

echo "============================================================"
echo "Bootstrap complete!"
echo "Derek's agent skills are ready to use."
echo "============================================================"
