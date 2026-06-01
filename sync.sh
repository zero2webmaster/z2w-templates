#!/usr/bin/env bash
# sync.sh — Sync the public-safe subset of ~/Desktop/Zero2Webmaster/AI/Templates/
# into this repo, then commit + push so Cloudflare Pages redeploys templates.z2w.us.
#
# Usage:
#   ./sync.sh              # sync, commit, push
#   ./sync.sh --no-push    # sync + commit but skip push
#   ./sync.sh --dry-run    # show what would change without writing
#
# What it copies (public-safe):
#   AGENTS_v2.13.0.md, AGENTS_WP_v3.1.0.md, Resources/**
# What it deliberately excludes:
#   .cursor/, .specstory/, .meta/, Archives/, SETUP_GUIDE_*.md (Kerry's local-only docs)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_ROOT="$HOME/Desktop/Zero2Webmaster/AI/Templates"

if [ ! -d "$SOURCE_ROOT" ]; then
  echo "❌ Source Templates folder not found at: $SOURCE_ROOT" >&2
  exit 1
fi

DRY_RUN=""
PUSH=1
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN="--dry-run" ;;
    --no-push) PUSH=0 ;;
    *) echo "Unknown flag: $arg" >&2; exit 1 ;;
  esac
done

echo "📥 Syncing public-safe Templates subset..."
echo "  from: $SOURCE_ROOT"
echo "  to:   $REPO_ROOT"

cp $DRY_RUN -v "$SOURCE_ROOT/AGENTS_v2.13.0.md" "$REPO_ROOT/" 2>/dev/null || true
cp $DRY_RUN -v "$SOURCE_ROOT/AGENTS_WP_v3.1.0.md" "$REPO_ROOT/" 2>/dev/null || true
rsync -a $DRY_RUN --delete --exclude=".DS_Store" "$SOURCE_ROOT/Resources/" "$REPO_ROOT/Resources/"

if [ -n "$DRY_RUN" ]; then
  echo "✅ Dry run complete. No changes written."
  exit 0
fi

cd "$REPO_ROOT"

if git diff --quiet && git diff --cached --quiet; then
  echo "✅ Already in sync — no changes."
  exit 0
fi

echo "📝 Changes detected. Committing..."
git add AGENTS_v2.13.0.md AGENTS_WP_v3.1.0.md Resources/
git commit -m "sync: $(date +%Y-%m-%d) — refresh from working copy"

if [ "$PUSH" -eq 1 ]; then
  echo "📤 Pushing to origin/main..."
  git push origin main
  echo "✅ Synced. Cloudflare Pages will redeploy templates.z2w.us within ~1 min."
else
  echo "✅ Committed. Skipped push (--no-push). Run 'git push origin main' when ready."
fi
