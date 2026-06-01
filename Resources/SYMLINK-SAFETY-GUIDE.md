# WordPress Symlink Safety Guide

## The Problem

When a WordPress plugin is developed via a **symlink** from `wp-content/plugins/plugin-name` to a development workspace, WordPress's `delete_plugins()` function follows the symlink and **recursively deletes the entire workspace** — source code, `.git/` history, `.specstory/`, `.cursor/`, and all project files.

This has happened **twice** to the z2w-admin-suite project:
- **2026-02-16:** Workspace destroyed. Recovered from zip backup but git history (v1.0–v1.19) lost permanently.
- **2026-02-27:** Workspace destroyed again despite written warnings in `.cursorrules`. Git history recovered from GitHub, but `.specstory/` history lost permanently.

**Written warnings alone do not prevent this.** Technical safeguards are required.

## The Solution: Three Layers of Protection

### Layer 1: WordPress mu-plugin (PRIMARY — blocks deletion at WordPress level)

A must-use plugin that hooks into WordPress's `delete_plugin` action and **blocks deletion of any symlinked plugin** before it happens.

**Key features:**
- Intercepts `delete_plugin` and calls `wp_die()` with a full error page explaining the danger
- Removes the "Delete" action link from symlinked plugins on the Plugins page
- Shows a warning banner on the Plugins page listing all symlinked plugins
- Cannot be deactivated through WP admin (mu-plugins are always active)
- Protects ALL symlinked plugins on the site, not just one

**Installation:** Copy `symlink-deletion-guard.php` to `wp-content/mu-plugins/` on each Local Site that has symlinked plugins. Create the `mu-plugins/` directory if it doesn't exist.

**File: `symlink-deletion-guard.php`**

```php
<?php
/**
 * Plugin Name: Symlink Deletion Guard
 * Description: Blocks WordPress from deleting symlinked plugins, which would destroy development workspaces.
 * Version: 1.0.0
 * Author: Zero2Webmaster
 *
 * WHY THIS EXISTS:
 * WordPress's delete_plugins() follows symlinks and recursively deletes the TARGET directory.
 * When a plugin is symlinked to a dev workspace, this destroys source code, .git/ history,
 * .specstory/, .cursor/, and all project files. This mu-plugin makes that impossible.
 *
 * This is a must-use plugin (mu-plugins/) so it cannot be accidentally deactivated or deleted
 * through the WordPress admin interface.
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Block deletion of any plugin whose directory is a symlink.
 *
 * Hooks into 'delete_plugin' which fires BEFORE WordPress performs the recursive delete.
 * Calling wp_die() here halts the deletion process entirely.
 */
add_action( 'delete_plugin', function ( $plugin_file ) {
    $plugin_slug = dirname( $plugin_file );

    if ( '.' === $plugin_slug ) {
        return;
    }

    $plugin_path = WP_PLUGIN_DIR . '/' . $plugin_slug;

    if ( ! is_link( $plugin_path ) ) {
        return;
    }

    $target = readlink( $plugin_path );

    $message  = '<div style="max-width:700px;margin:40px auto;font-family:-apple-system,BlinkMacSystemFont,sans-serif">';
    $message .= '<h1 style="color:#dc3232;border-bottom:3px solid #dc3232;padding-bottom:12px">';
    $message .= '&#9940; SYMLINK DELETION BLOCKED</h1>';
    $message .= '<p style="font-size:16px"><strong>' . esc_html( $plugin_slug ) . '</strong> ';
    $message .= 'is symlinked to a development workspace:</p>';
    $message .= '<pre style="background:#f0f0f0;padding:12px;border-radius:4px;overflow-x:auto">';
    $message .= esc_html( $plugin_path ) . "\n&rarr; " . esc_html( $target ) . '</pre>';
    $message .= '<p style="font-size:15px;color:#dc3232"><strong>Deleting through WordPress would ';
    $message .= 'recursively destroy your entire workspace</strong> &mdash; source code, .git/ history, ';
    $message .= '.specstory/, .cursor/, and all project files.</p>';
    $message .= '<h2>Safe removal steps:</h2>';
    $message .= '<ol style="font-size:15px;line-height:1.8">';
    $message .= '<li><strong>Deactivate only</strong> in WP admin (safe &mdash; does not delete files)</li>';
    $message .= '<li><strong>Remove the symlink via terminal:</strong><br>';
    $message .= '<code style="background:#f0f0f0;padding:4px 8px;border-radius:3px">';
    $message .= 'rm &quot;' . esc_html( $plugin_path ) . '&quot;</code><br>';
    $message .= '<small>This removes only the symlink, not the workspace files.</small></li></ol>';
    $message .= '<p style="margin-top:20px"><a href="' . esc_url( admin_url( 'plugins.php' ) ) . '">';
    $message .= '&larr; Back to Plugins</a></p></div>';

    wp_die(
        $message,
        'Symlink Deletion Blocked',
        array(
            'response'  => 403,
            'back_link' => false,
        )
    );
});

/**
 * Add a visual warning badge next to symlinked plugins on the Plugins page.
 */
add_filter( 'plugin_action_links', function ( $actions, $plugin_file ) {
    $plugin_slug = dirname( $plugin_file );

    if ( '.' === $plugin_slug ) {
        return $actions;
    }

    $plugin_path = WP_PLUGIN_DIR . '/' . $plugin_slug;

    if ( is_link( $plugin_path ) ) {
        $target  = readlink( $plugin_path );
        $warning = '<span style="color:#dc3232;font-weight:bold" title="Symlinked to: '
                 . esc_attr( $target )
                 . '">&#9888; SYMLINKED (dev)</span>';

        array_unshift( $actions, $warning );

        unset( $actions['delete'] );
    }

    return $actions;
}, 10, 2 );

/**
 * Add admin notice on the Plugins page listing all symlinked plugins.
 */
add_action( 'admin_notices', function () {
    $screen = get_current_screen();
    if ( ! $screen || 'plugins' !== $screen->id ) {
        return;
    }

    $symlinked = array();
    $plugins   = get_plugins();

    foreach ( $plugins as $plugin_file => $data ) {
        $slug = dirname( $plugin_file );
        if ( '.' === $slug ) {
            continue;
        }
        $path = WP_PLUGIN_DIR . '/' . $slug;
        if ( is_link( $path ) ) {
            $symlinked[] = $data['Name'] . ' &rarr; ' . esc_html( readlink( $path ) );
        }
    }

    if ( empty( $symlinked ) ) {
        return;
    }

    echo '<div class="notice notice-warning" style="border-left-color:#dc3232">';
    echo '<p><strong>&#9888; Symlink Deletion Guard:</strong> ';
    echo count( $symlinked ) . ' plugin(s) are symlinked to development workspaces. ';
    echo 'The Delete button has been removed for these plugins. ';
    echo 'Use terminal <code>rm</code> to safely remove symlinks.</p>';
    echo '<ul style="margin:4px 0 8px 20px;list-style:disc">';
    foreach ( $symlinked as $info ) {
        echo '<li><code>' . $info . '</code></li>';
    }
    echo '</ul></div>';
});
```

### Layer 2: Auto-push git hook

A post-commit hook that pushes to GitHub after every commit, ensuring the remote always has the latest code for disaster recovery.

**File: `tools/protect-git.sh`**

```bash
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
```

### Layer 3: rsync deployment alternative (optional)

A script that copies workspace files to the WP plugins directory instead of using a symlink. Use this if you want to eliminate symlinks entirely.

**File: `tools/dev-deploy.sh`**

See the z2w-admin-suite repository for a working example. Adapt the `WP_PLUGIN_DIR` path for your plugin.

## Installation Checklist for Any WordPress Plugin Project

1. **mu-plugin (one-time per Local Site):**
   - Copy `symlink-deletion-guard.php` to each Local Site's `wp-content/mu-plugins/`
   - Create the `mu-plugins/` directory if needed: `mkdir -p "...wp-content/mu-plugins"`

2. **Auto-push hook (per project):**
   - Add `tools/protect-git.sh` to the project
   - Run `./tools/protect-git.sh install`

3. **`.cursorrules` update (per project):**
   - Add the symlink safety section documenting the danger and active safeguards
   - Document which Local Site(s) the plugin is symlinked into

4. **Verify:** Run `./tools/protect-git.sh status` to confirm everything is active

## Currently Symlinked Plugins (as of 2026-02-28)

All on `z2w-complete-suite` Local Site:

| Plugin | Symlink Target |
|--------|---------------|
| z2w-admin-suite | `Cursor Projects/z2w-admin-suite` |
| z2w-eventleap | `Cursor Projects/z2w-eventleap/z2w-eventleap` |
| z2w-testimonials | `Cursor Projects/z2w-testimonials` |

## Local Sites That Need the mu-plugin

| Local Site | Has mu-plugin? | Has symlinks? |
|-----------|---------------|--------------|
| z2w-complete-suite | ✅ Yes (installed 2026-02-28) | Yes (3 plugins) |
| z2w-admin-commander | ❌ No | Check for symlinks |
| z2w-science-content-creator | ❌ No | Check for symlinks |
