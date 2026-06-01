#!/bin/bash
#
# protect-git.sh — Install git hooks that auto-push after every commit
#
# USAGE:
#   ./tools/protect-git.sh install    # Install the auto-push hook
#   ./tools/protect-git.sh status     # Check if protections are active
#

WORKSPACE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
GIT_DIR="$WORKSPACE_ROOT/.git"
HOOKS_DIR="$GIT_DIR/hooks"

if [ ! -d "$GIT_DIR" ]; then
    echo "ERROR: No .git directory found at $GIT_DIR"
    exit 1
fi

case "$1" in
    install)
        mkdir -p "$HOOKS_DIR"

        cat > "$HOOKS_DIR/post-commit" << 'HOOK'
#!/bin/bash
# Auto-push to GitHub after every commit (safety net against workspace destruction)
BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
if [ -n "$BRANCH" ] && git remote get-url origin &>/dev/null; then
    git push origin "$BRANCH" --quiet 2>/dev/null &
    echo "→ Auto-pushing to origin/$BRANCH (background)"
fi
HOOK
        chmod +x "$HOOKS_DIR/post-commit"
        echo "✓ Installed post-commit auto-push hook."
        ;;

    status)
        echo "=== Symlink Safety Status ==="
        echo ""

        # Check post-commit hook
        if [ -x "$HOOKS_DIR/post-commit" ] && grep -q "Auto-push" "$HOOKS_DIR/post-commit" 2>/dev/null; then
            echo "✓ auto-push:    ACTIVE (post-commit hook installed)"
        else
            echo "✗ auto-push:    MISSING — run './tools/protect-git.sh install'"
        fi

        # Check GitHub remote
        REMOTE_URL=$(cd "$WORKSPACE_ROOT" && git remote get-url origin 2>/dev/null)
        if [ -n "$REMOTE_URL" ]; then
            echo "✓ origin: $REMOTE_URL"
        else
            echo "✗ No remote configured"
        fi
        ;;

    *)
        echo "Usage: $0 {install|status}"
        exit 1
        ;;
esac
