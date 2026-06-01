# Agent Instructions — WordPress Plugin Projects

**Version:** 3.1.0 | **Last Updated:** 2026-03-10

> This file is mirrored across CLAUDE.md, AGENTS.md, and GEMINI.md so the same instructions load in any AI environment.
>
> **Reference Material:** For setup instructions, templates, troubleshooting guides, and detailed examples, see `SETUP_GUIDE.md` (use `@SETUP_GUIDE.md` to load when needed).
>
> **Scope:** This version is WordPress plugin-specific. For Python automation projects, use the generic AGENTS.md (v2.x).

You operate within a 3-layer architecture that separates concerns to maximize reliability. LLMs are probabilistic, whereas most business logic is deterministic and requires consistency. This system fixes that mismatch.

## The 3-Layer Architecture

**Layer 1: Directive (What to do)**
- SOPs written in Markdown, live in `directives/`
- Define the goals, inputs, hooks/APIs to use, outputs, and edge cases
- Natural language instructions, like you'd give a mid-level employee

**Layer 2: Orchestration (Decision making)**
- This is you. Your job: intelligent routing.
- Read directives, implement features in the right order, handle errors, ask for clarification, update directives with learnings
- You're the glue between intent and execution. E.g. you don't try to implement analytics by memory—you read `directives/metorik-dashboard.md`, understand the data model, then write `includes/metorik/class-z2w-dashboard.php`

**Layer 3: Execution (Doing the work)**
- **PHP plugin code** in `includes/`, `admin/`, `public/`
- WordPress hooks, WooCommerce APIs, custom DB queries, REST endpoints, shortcodes
- Reliable, testable, deterministic. Escape output, sanitize input, use nonces.
- `execution/` holds **build tooling only** (zip builder, git hooks) — not plugin runtime logic

**Why this works:** if you do everything yourself, errors compound. 90% accuracy per step = 59% success over 5 steps. The solution is push complexity into deterministic PHP. That way you just focus on decision-making.

### WordPress Layer Mapping

| Generic Layer | WordPress Plugin Equivalent |
|---|---|
| Directive | `directives/` — feature SOPs, same as always |
| Orchestration | AI agent coordinating development |
| Execution | PHP plugin files in `includes/`, `admin/`, `public/` |
| `execution/` scripts | Build tooling only (zip, git hooks) — not plugin logic |
| `.env` credentials | NOT used for plugin config — goes in WP Admin → plugin Settings → stored in `wp_options` |

---

## Operating Principles

**1. Check for tools first**
Before writing a PHP class, check `includes/` per your directive. Only create new classes/files if none exist. When a WooCommerce API covers the need, use it instead of direct DB queries.

**2. Self-anneal when things break**
- Read the PHP error / WP debug log entry and stack trace
- Fix the code and verify again (check WP_DEBUG log + browser test)
- Update the directive with what you learned (API quirks, hook timing, edge cases)
- Example: a hook fires too early → research correct hook → fix → test → update directive

**3. Update directives as you learn**
Directives are living documents. When you discover WP/WC API constraints, better hook placements, timing issues, or edge cases—update the directive. Don't create or overwrite directives without asking unless explicitly told to.

**4. Update directives as you code (not after)**
Directives document the system's current state. As you make code changes:
- Update affected directives in real-time
- Search for hook names, option keys, meta keys that need updating
- Commit code + directive updates together
- If you can't update the directive to explain the new behavior, maybe the code isn't ready yet

**5. Always verify dates from system info**
When referencing dates, days of the week, or time-sensitive information:
- **Check `Current Date:` field in system info** (provided at start of each conversation)
- **Don't assume what day it is** — verify before making statements like "tomorrow" or "next week"
- **Core issue:** AI models can incorrectly assume the current day
- Especially important for: scheduling, date calculations, cron setups, planning discussions

**6. Focus on ONE primary goal per chat session**
Each chat session should tackle ONE clearly defined objective. Multi-goal sessions waste tokens and produce unclear handoffs.

**Why This Matters:**
- Multi-goal sessions use 200K+ tokens; single-goal sessions use 50-150K tokens (~32% savings)
- Context switching between tasks increases error rate and reduces focus
- Hard to verify completion when mixing bugs, features, and enhancements

**Session Start Template:**
- State the ONE goal clearly: "This session: [specific objective]"
- Load only relevant context (`@ROADMAP.md`, `@STATUS.md`, relevant directives)
- Set success criteria: "Done when: [measurable outcome]"

**Session End Template:**
- Summarize what was accomplished
- Update STATUS.md and ROADMAP.md
- Create clear handoff for next session

**Good Single-Goal Examples:**
- ✅ "Implement the Products & Inventory admin page"
- ✅ "Build the [z2w-checkout] shortcode layout"
- ✅ "Fix AJAX fee calculation precision"

**Bad Multi-Goal Examples:**
- ❌ "Build dashboard, fix checkout, update settings"
- ❌ "Polish Phase 4 items" (too vague)
- ❌ "Work on whatever needs doing"

**Token Budgets:**
- **Single-goal session:** 50-150K tokens (optimal)
- **Multi-goal session:** 200K+ tokens (wasteful)

**Handoff Triggers** (start a new session when):
- Primary goal is complete
- Token usage exceeds ~75% of budget
- A scope change surfaces (new, unrelated task)
- A blocking bug requires a different investigation approach

---

## Project Kickoff Process

**MANDATORY FIRST STEP FOR ALL NEW PROJECTS/CHATS:**

### Initial Project Setup

1. **If no `ROADMAP.md` exists, immediately create one:**
   - Analyze project goal (README, user prompt, `.cursorrules`, directives)
   - Break into 5-12 atomic, sequential steps (one feature per step)
   - Each step must be: **specific, testable, with verification commands**
   - See `SETUP_GUIDE.md` for WordPress plugin ROADMAP structure

2. **ALWAYS check/update `STATUS.md`** (create if missing):
   - Required sections: `## Blockers` | `## Decisions` | `## Next Actions` | `## Tech Debt`
   - Keep concise, actionable items only
   - Update at start and end of every session

3. **Create `TROUBLESHOOTING.md`** (if it doesn't exist):
   - Captures issues and solutions as they're discovered
   - Living document: Add entries whenever you solve a problem that took >15 minutes
   - Documents WP/WC API quirks, hook timing issues, Stripe edge cases

4. **Create `.cursorignore`** (if it doesn't exist):
   - Prevents large generated files from flooding AI context
   - See `SETUP_GUIDE.md` for WordPress template

5. **For WordPress plugin projects — also verify:**
   - Plugin main file exists with correct header (Name, Version, Author, Text Domain)
   - Activation hook creates custom tables and default options
   - Admin menu registered with all planned sub-pages (stubs are fine)
   - Symlink from Local site to workspace root exists and is working
   - WP_DEBUG is enabled on Local site (`define('WP_DEBUG', true)`)
   - Plugin activates without PHP errors or warnings

6. **Confirm readiness:**
   - Output: "`ROADMAP.md`, `STATUS.md`, `TROUBLESHOOTING.md`, and `.cursorignore` confirmed. Plugin activates cleanly. Current step: [X]. Ready."

7. **For existing projects:**
   - Always start with: "`@ROADMAP.md` `@STATUS.md` `@TROUBLESHOOTING.md`, confirm next step?"
   - Review blockers and decisions before proceeding

### STATUS.md Maintenance Rules

**Prevent unbounded growth** — STATUS.md is loaded frequently and must stay concise:
- **Recent Updates section:** Keep last 3-4 sessions maximum
- **Archive older entries:** Delete session entries older than the last 4
- **Rule of thumb:** If STATUS.md exceeds ~150 lines, trim it

### Step Completion Protocol

**After each goal/step completion:**

1. ✅ **Run verification** (see Verification Standards) — MANDATORY before marking complete
2. ✅ **Mark step complete** in `ROADMAP.md` with completion date
3. ✅ **Log in `STATUS.md`:** recent update, decisions, new tech debt, next actions
4. ✅ **Output confirmation:** "Step [X] ✅ complete. `ROADMAP.md` & `STATUS.md` updated. Ready for Step [Y]?"

### Key Principles

**Atomic Steps:** One feature or refactor per step. Completable in single focused session. Clear acceptance criteria.

**Testable Acceptance Criteria:** Every step MUST include verification commands. Cannot mark ✅ without running them.

**Resumability:** `ROADMAP.md` + `STATUS.md` provide complete context. Any developer (or AI in new chat) can resume work.

---

## Common Name & Terminology Glossary

**Always use these exact spellings and capitalizations:**

### People & Organizations

- **Kerry Kriger** ✅ (not "Carrie Krieger", "Kerry Krieger", "Carrie Kriger")
- **Zero2Webmaster** ✅ (not "0-2 Webmaster", "Zero to Webmaster", "Zero 2 Webmaster")
- **Bansuri Bliss** ✅ (not "Bonseri Bliss", "Bansuri Bliss Academy")
- **SAVE THE FROGS!** ✅ (all caps with exclamation mark)
  - Exception: "Save The Frogs Day" (title case for the event name)

### Technical Terms

- **WordPress** ✅ (not "Wordpress", "Word Press")
  - Use Application Passwords for API access, never login passwords
  - Always use Gutenberg block syntax for content creation

- **WooCommerce** ✅ (not "Woo Commerce", "woocommerce")
  - Use CRUD classes (`WC_Order`, `WC_Product`, etc.) over direct DB queries
  - Use table IDs in custom queries, not table names

- **Stripe:**
  - Always use restricted keys (`rk_live_...` pattern)
  - Pin `Stripe-Version` header to account's detected version
  - Handle all events idempotently by `event_id`

- **Bunny.net:**
  - "Bunny.net" or "Bunny" (not "BunnyCDN")
  - Storage hostname is region-specific (e.g., `la.storage.bunnycdn.com`)

- **Airtable:**
  - Always use table IDs (`tblXXXXXXXXXXXXXX`) in code, never table names
  - Always use Personal Access Tokens (PATs), not deprecated API keys

### Why This Matters

Consistent spelling prevents database mismatches, documentation confusion, brand inconsistency, and failed API calls.

---

## Self-Annealing Loop

Errors are learning opportunities. When something breaks:
1. Fix the PHP / fix the hook timing / fix the query
2. Test it (browser + debug log)
3. Update the directive with what you learned
4. System is now stronger

---

## Directive Maintenance

**Directives are the source of truth.** When PHP code changes, directives MUST be updated.

### When to Update Directives

Update directives whenever you:
1. **Change hook names or priority** (e.g., `woocommerce_checkout_update_order_meta` priority changed)
2. **Add new features or shortcodes**
3. **Modify data types** (e.g., meta key renamed, option key changed)
4. **Update performance characteristics** (e.g., added index, changed query approach)
5. **Discover edge cases** not previously documented
6. **Change admin page slugs or settings keys**

### Directive Update Checklist

When modifying PHP code, always:
- [ ] Update the directive that covers this functionality
- [ ] Update any related directives that reference this feature
- [ ] Update hook/filter names in directives if changed
- [ ] Update option key names if changed
- [ ] Check other directives for references that need updating

### Finding All References

Before finalizing code changes, search all directives:
```bash
rg "old_hook_name" directives/
rg "old_option_key" directives/
```

---

## File Organization

**Directory structure for WordPress plugins:**

```
plugin-name/
├── directives/              # Layer 1: Feature SOPs and workflows
├── execution/               # Build tooling only (not plugin runtime)
│   ├── build_plugin.py      # Creates distribution zip
│   └── install_git_hooks.py # Pre-commit directive reminders
├── plugin-name.php          # Main plugin file (header + boot)
├── uninstall.php            # Clean removal of all plugin data
├── readme.txt               # WordPress plugin readme
├── includes/                # Layer 3: All PHP classes
│   ├── class-{plugin}-activator.php
│   ├── class-{plugin}-admin-menu.php
│   ├── stripe/              # Module subdirectories
│   ├── metorik/
│   ├── launchflows/
│   └── settings/
├── admin/                   # Admin-facing assets
│   ├── css/
│   ├── js/
│   └── views/               # PHP templates for admin pages
├── public/                  # Frontend assets
│   ├── css/
│   └── js/
└── languages/               # Translation .pot files
```

**Key rules:**
- `execution/` = build tools only. Never put plugin runtime code here.
- `admin/views/` = PHP templates loaded by admin menu class. One file per admin page.
- `includes/` subdirectories = one per module (stripe, metorik, launchflows, etc.)
- `.tmp/` = generated zips and temporary files. Never commit.

---

## Standard Development Tools

### PHP (Required)

```bash
# Check PHP version (7.4+ required)
php --version

# Syntax check any PHP file
php -l includes/class-my-module.php

# Batch syntax check
for f in includes/**/*.php; do php -l "$f"; done
```

### Local by Flywheel (Required for Testing)

All plugin development uses Local by Flywheel for the test WordPress site.

**Symlink setup (one-time per plugin):**
```bash
ln -s "/path/to/workspace" \
  "/Users/USERNAME/Local Sites/site-name/app/public/wp-content/plugins/plugin-name"
```

**Enable WP_DEBUG on Local site** — edit `wp-config.php`:
```php
define('WP_DEBUG', true);
define('WP_DEBUG_LOG', true);
define('WP_DEBUG_DISPLAY', false);
```

**Monitor debug log:**
```bash
tail -f "/Users/USERNAME/Local Sites/site-name/app/public/wp-content/debug.log"
```

**⚠️ CRITICAL — Symlink Safety:**
NEVER delete a symlinked plugin from WP Admin → Plugins → Delete. WordPress follows the symlink and **recursively deletes your entire workspace**. This has happened twice and is catastrophic.
- ✅ **Safe:** Deactivate only in WP admin
- ✅ **Safe removal of symlink:** `rm "/path/to/wp-content/plugins/plugin-name"` (removes symlink, not source)
- ❌ **NEVER:** WP Admin → Plugins → Delete

**⚠️ Local Site Credentials:**
Do not change WordPress admin credentials (passwords, usernames) on the local development site unless the user explicitly requests it. The existing admin account is sufficient for all browser testing. Do not temporarily reset passwords for convenience or testing access. If you need browser access to the local site and cannot log in, ask the user for assistance.

### Python (Build Tooling Only)

Python is used exclusively for build scripts (`execution/build_plugin.py`, `execution/install_git_hooks.py`). It is NOT used for plugin runtime logic.

```bash
python3 --version  # Should be 3.8+
python3 execution/build_plugin.py   # Build distribution zip
python3 execution/install_git_hooks.py  # Install pre-commit hook
```

No virtual environment or `requirements.txt` needed unless build scripts have dependencies beyond the standard library.

### Plugin Credentials

**API keys and credentials go in WP Admin → plugin Settings page → stored in `wp_options`.** They do NOT go in a `.env` file. The plugin's Settings page provides the UI; `get_option()` / `update_option()` handles storage.

`.env` files may exist for external build/test scripts that call WordPress REST API, but this is rarely needed when the AI has browser access to the Local site.

---

## WordPress Plugin Development

### Coding Standards

- Follow **WordPress Coding Standards** (PHP, JS, CSS)
- Use PHP 7.4+ features (typed properties, arrow functions where clear)
- **Prefix everything:** functions → `pluginslug_`, classes → `Plugin_Class_Name`, constants → `PLUGIN_CONSTANT`
- Use **WooCommerce CRUD classes** (`WC_Order`, `WC_Product`) over direct DB queries
- **Escape all output:** `esc_html()`, `esc_attr()`, `esc_url()`, `wp_kses_post()`
- **Sanitize all input:** `sanitize_text_field()`, `absint()`, `wp_unslash()`
- **Nonces** for all forms and AJAX handlers
- **Translatable strings** via `__()` / `_e()` with plugin text domain
- Custom DB tables prefixed with `{$wpdb->prefix}pluginslug_`

### Plugin Main File Structure

```php
<?php
/**
 * Plugin Name:       My Plugin
 * Version:           1.0.0
 * Requires at least: 6.0
 * Requires PHP:      7.4
 * Author:            Dr. Kerry Kriger
 * Author URI:        https://zero2webmaster.com/kerry-kriger
 * Text Domain:       my-plugin
 * WC requires at least: 8.0
 * WC tested up to:   9.x
 */

define( 'MY_PLUGIN_VERSION', '1.0.0' );
define( 'MY_PLUGIN_PATH', plugin_dir_path( __FILE__ ) );
define( 'MY_PLUGIN_URL', plugin_dir_url( __FILE__ ) );
define( 'MY_PLUGIN_BASENAME', plugin_basename( __FILE__ ) );

// WooCommerce dependency check
// Activation / deactivation hooks
// HPOS compatibility declaration
// Boot on plugins_loaded
```

### Module Singleton Pattern

Every module class should be a singleton:
```php
class My_Module {
    private static ?My_Module $instance = null;

    public static function get_instance(): My_Module {
        if ( null === self::$instance ) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    private function __construct() {
        // Register hooks here
        add_action( 'init', array( $this, 'register_hooks' ) );
    }
}
```

### Custom Database Tables

- Use `dbDelta()` in the activator for `CREATE TABLE IF NOT EXISTS`
- Always add `$wpdb->get_charset_collate()` to table definitions
- Index columns used in `WHERE` clauses
- Store DB version in `wp_options` for future migration checks

### HPOS Compatibility

Always declare High-Performance Order Storage compatibility:
```php
add_action( 'before_woocommerce_init', function () {
    if ( class_exists( \Automattic\WooCommerce\Utilities\FeaturesUtil::class ) ) {
        \Automattic\WooCommerce\Utilities\FeaturesUtil::declare_compatibility(
            'custom_order_tables', __FILE__, true
        );
    }
} );
```

### Admin Plugin Action Links

Add a Settings link on the Plugins page under each plugin:
```php
add_filter( 'plugin_action_links_' . PLUGIN_BASENAME, function( $links ) {
    array_unshift( $links, sprintf(
        '<a href="%s">%s</a>',
        admin_url( 'admin.php?page=plugin-settings' ),
        __( 'Settings', 'text-domain' )
    ) );
    return $links;
} );
```

### Version Updates for WP Plugins

When incrementing version, update ALL of these in the same commit:
1. `VERSION` file
2. `plugin-name.php` header (`Version:` line)
3. `plugin-name.php` version constant
4. `readme.txt` (`Stable tag:`)
5. `README.md` (header and footer)
6. `CHANGELOG.md`
7. `directives/` (any affected files)

---

## WordPress & Gutenberg Best Practices

**Always use Gutenberg blocks** when creating WordPress content (not Classic Editor):
```
"content": "<!-- wp:paragraph -->\n<p>Your content here</p>\n<!-- /wp:paragraph -->"
```

**WordPress REST API:** Use Application Passwords for authentication, never login passwords.

**WooCommerce:** Use CRUD classes over `$wpdb` direct queries. Handle HPOS. Test with WC_DEBUG if available.

**WooCommerce Subscriptions:** Check `class_exists('WC_Subscriptions')` before using subscription APIs. Graceful disable with admin notice if not active.

---

## Airtable Best Practices

*(Relevant when WP plugins integrate with Airtable)*

1. Always use table IDs (`tblXXXXXXXXXXXXXX`), never table names
2. Use Personal Access Tokens (PATs), not deprecated API keys
3. Single select options must match EXACTLY (including whitespace)
4. Auto-diagnose on errors — validate field names with suggestions for typos

**For the complete `AirtableFieldValidator` class, see `@SETUP_GUIDE.md`.**

---

## Verification Standards

**WordPress Plugin Verification — run before marking any ROADMAP step ✅:**

### Primary Checks (Every Step)

```bash
# 1. PHP syntax check all modified files
php -l includes/class-my-module.php

# 2. Batch syntax check entire plugin
for f in includes/**/*.php admin/**/*.php public/**/*.php; do php -l "$f"; done

# 3. Check WP debug log is clean
cat "/Users/USERNAME/Local Sites/site-name/app/public/wp-content/debug.log"
```

### Browser Verification (Every Step)

1. Plugin page loads without white screen or PHP errors
2. Relevant admin page loads and displays correctly
3. No JavaScript console errors
4. Any AJAX operations return expected responses
5. WP Debug log clean after page loads

### Step-Specific Checks

| Changed | Check |
|---------|-------|
| Activation hook | Deactivate → Reactivate → verify tables/options created |
| Admin page | Navigate to page → verify loads without errors |
| Shortcode | Place `[shortcode]` on test page → verify renders |
| AJAX handler | Trigger action → check Network tab → verify response |
| WooCommerce hook | Place test order → verify hook fired correctly |
| Stripe webhook | Use Stripe CLI or test event → verify processed |
| Custom DB table | `SHOW TABLES LIKE '%prefix%'` in WP phpMyAdmin |

### Completion Criteria

- ✅ Zero PHP errors or warnings in WP debug log
- ✅ Plugin activates/deactivates cleanly
- ✅ All modified admin pages load without errors
- ✅ No JavaScript console errors on affected pages
- ✅ Verified in browser on Local test site
- ✅ Relevant directives updated

---

## Version Control & Git Practices

### Semantic Versioning

**Format:** `MAJOR.MINOR.PATCH` (e.g., 1.0.3)

- **MAJOR**: Breaking changes, renamed hooks/options that break existing installs
- **MINOR**: New features, new admin pages, new shortcodes (backward compatible)
- **PATCH**: Bug fixes, documentation updates, code comments

### Version Management Files

Every project must include:
1. `VERSION` — single line, project version only (e.g., `1.3.1`)
2. `CHANGELOG.md` — chronological record of all changes
3. `README.md` header — project version AND framework version
4. `plugin-name.php` — `Version:` header line and version constant

**Framework Version in README:**
```markdown
# My Plugin Name
**Version:** 1.0.0 | **Framework:** 3.1.0
```

### Commit Message Format

```
v{VERSION} - Brief description

Category:
- Detailed change 1
- Detailed change 2

Version: {VERSION}
```

### Version Update Workflow

Every version increment — update ALL in the same commit:

```bash
# Find all old version references first
grep -r "1.0.0" . --exclude-dir=.git --exclude-dir=.tmp
# Update every result before committing
```

**Files to update:** `VERSION`, `plugin-name.php` (header + constant), `readme.txt`, `README.md` (header + footer), `CHANGELOG.md`

### Initial Git Setup

```bash
git init
git branch -M main
# Create GitHub repo at github.com/new (Private, leave all options unchecked)
git remote add origin https://github.com/USERNAME/repo-name.git
git push -u origin main
```

### File Deletion Policy

**CRITICAL:** Never delete files without explicit user permission. Deleted files via AI tools do NOT go to Trash and cannot be recovered easily.

**Process:** Ask user before deleting. Wait for explicit approval. Exception: `.tmp/` files documented as regenerable.

**WordPress:** NEVER delete a symlinked plugin from WP Admin. See Symlink Safety above.

---

## Session Handoff & Continuity

For multi-session projects, maintain these files for seamless continuity:

1. **ROADMAP.md** — Atomic steps with verification criteria
2. **STATUS.md** — Current state, blockers, decisions
3. **HANDOFF.md** — Session transition document with starting prompt

**At End of Session:**
1. Update STATUS.md with decisions and blockers
2. Update ROADMAP.md with progress
3. Commit and push

**At Start of Next Session:**
```
I'm picking up from the last session.

@HANDOFF.md - What happened last session
@STATUS.md - Current state and blockers
@ROADMAP.md - Progress and next steps

Ready to continue!
```

---

## .cursorrules File Structure

**Every WordPress plugin project must have a .cursorrules file with this header:**

```markdown
# Project-Specific Rules

> **Global Instructions:** See AGENTS.md for the WordPress plugin architecture and operating principles.

## This Project

**Project:** [Plugin Name]
**Plugin type:** [WooCommerce extension | Standalone plugin | etc.]
**Requires:** WordPress X.X+, WooCommerce X.X+, PHP X.X+

**Plugin Metadata:**
- Plugin Name (sidebar): [Name]
- Author: Dr. Kerry Kriger — https://zero2webmaster.com/kerry-kriger
- Text Domain: [text-domain]
- Prefix: [prefix_] (functions), [PREFIX_] (constants)

**Local Development:**
- Test Site: [site-name].local — http://[site-name].local/wp-admin
- Site Path: /Users/USERNAME/Local Sites/[site-name]
- Plugin Path: ...wp-content/plugins/[plugin-folder]
- Symlink: Workspace root → plugin path
- DANGER: NEVER delete via WP admin. Deactivate only.

**Zip Distribution:**
- Delivery Folder: [path]
- Naming: [plugin-slug]-vX.Y.Z.zip
- Build Command: `python3 execution/build_plugin.py`

**Plugin Credentials:**
- [Stripe RAK, API keys, etc.] → Stored in WP Admin → [Plugin] → Settings → [Tab]
- NOT stored in .env

[Project-specific requirements, APIs, data sources, edge cases...]
```

---

## Summary

You sit between human intent (directives) and deterministic execution (PHP plugin code). Read directives, implement features, handle errors, continuously improve the system.

Be pragmatic. Be reliable. Self-anneal.

---

*The original 3-layer architecture (v1.0.0) was created by Nick Saraev. This WordPress plugin edition is maintained by [Zero2Webmaster](https://zero2webmaster.com/) Founder Dr. Kerry Kriger.*
*For AI automation training, consulting, and website development, visit [zero2webmaster.com](https://zero2webmaster.com/).*

*Version: 3.1.0 | Last Updated: 2026-03-10*
