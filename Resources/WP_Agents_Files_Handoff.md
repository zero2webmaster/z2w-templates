# Templates Agent Handoff

**From:** Z2W Seller Suite project session, 2026-03-05
**To:** Templates project agent

---

## What to Do

Add two new files to the master templates folder:

1. **`AGENTS_WP.md`** — Copy from this project's `AGENTS_WP.md`
2. **`SETUP_GUIDE_WP.md`** — Copy from this project's `SETUP_GUIDE_WP.md`

These are WordPress plugin-specific replacements for the generic `AGENTS.md` (v2.13.0) and `SETUP_GUIDE.md` (v2.5.0).

---

## Why These Exist

The original `AGENTS.md` was built for Python automation pipelines (video migration, data scraping, etc.) — it contains extensive content about `venv`, `requirements.txt`, `.env` credentials, `pytest`, `mypy`, and Python execution scripts.

For WordPress plugin projects, all of that is irrelevant and wastes tokens on every single message. WordPress plugins have a fundamentally different execution layer: the plugin PHP code IS the execution layer. The `execution/` folder holds build tooling (zip scripts, git hooks) only.

`AGENTS_WP.md` and `SETUP_GUIDE_WP.md` are complete, self-contained replacements that:
- Remove all Python-specific content (venv, pip, pytest, mypy, requirements.txt)
- Replace Layer 3 "Python scripts" with "PHP plugin code in includes/"
- Add WordPress coding standards, hook patterns, HPOS compatibility
- Add symlink safety warnings (critical — has destroyed workspaces twice)
- Add WP-specific verification (php -l, WP_DEBUG log, browser testing)
- Add plugin scaffold structure and module singleton pattern
- Clarify that API credentials go in WP Admin settings → wp_options, NOT .env
- Include a WordPress-specific Project Instantiation Prompt template
- Add common WordPress gotchas (hook timing, nonce expiry, HPOS, autoloading)

---

## How to Use in New WP Plugin Projects

When starting a new WordPress plugin project:

1. Use `AGENTS_WP.md` as the project's `AGENTS.md` (rename or instruct agent to read it)
2. Use `SETUP_GUIDE_WP.md` as the project's `SETUP_GUIDE.md`
3. In `.cursorrules`, header should say:
   > **Global Instructions:** See AGENTS.md for the WordPress plugin architecture and operating principles.

The Project Instantiation Prompt template is in `SETUP_GUIDE_WP.md` under "The Project Instantiation Prompt — WordPress Plugin Version."

---

## Version Info

- `AGENTS_WP.md` — Version 3.0.0 (new file; supersedes AGENTS.md v2.x for WP projects)
- `SETUP_GUIDE_WP.md` — Version 3.0.0 (new file; supersedes SETUP_GUIDE.md v2.x for WP projects)
- Based on: AGENTS.md v2.13.0 and SETUP_GUIDE.md v2.5.0

---

## No Changes Needed to Generic Files

The original `AGENTS.md` (v2.13.0) and `SETUP_GUIDE.md` (v2.5.0) remain valid for Python automation projects. Do not modify them. The WP versions are additive — new files alongside the originals.
