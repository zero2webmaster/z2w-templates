# Zero2Webmaster Cursor Framework - What's Actually Different?

**Version:** v1.0.0 → v2.13.0 (Python) / v3.0.0 (WordPress)  
**Last Updated:** 2026-03-05

> **Purpose:** This file contains Notion-optimized formatting for the sales page. Copy and paste sections directly into Notion when releasing new versions. Entries are in chronological order (oldest to newest). New entries always go at the bottom.

---

## 🎯 What's Actually Different? (v1.0.0 → v2.13.0 / v3.0.0)

### 1. 3-Layer Architecture (v1.0.0)

**Transforms AI from "sometimes works" to "production reliable"**

✅ Layer 1: Directives (what to do - natural language SOPs)

✅ Layer 2: Orchestration (AI decision-making)

✅ Layer 3: Execution (deterministic Python scripts)

**Problem Solved:** AI models are probabilistic (90% accuracy per step), but business logic requires 100% consistency. This layered architecture pushes complexity into deterministic code so AI focuses on decisions while scripts do the work reliably — eliminating compounding errors across multi-step workflows.

---

### 2. Directive Maintenance System (v2.0.0)

**Prevents 80% of "system broke after 2 weeks" scenarios**

✅ Real-time directive updates (not after-the-fact)

✅ Directive/code synchronization checklist

✅ Pre-commit verification

✅ Self-annealing improvements

**Problem Solved:** The #1 reason AI automation systems fail is documentation drift — code changes but directives don't, and the system silently becomes unmaintainable. Mandatory synchronization ensures directives always match code so the system self-heals instead of breaking.

---

### 3. WordPress & Airtable Production Patterns (v2.2.0)

**10x faster development**

✅ WordPress Application Password security (never use login passwords)

✅ Form-to-Airtable multi-table patterns

✅ Gutenberg block syntax for modern WordPress

✅ Relational database patterns (4-table architectures)

✅ API client design (rate limiting with sliding window)

**Problem Solved:** Developers waste weeks figuring out WordPress automation and Airtable integrations through trial and error. These production-tested patterns are copy-paste-done — no reinventing the wheel, no rate limit surprises, no security gaps.

---

### 4. Initial Git Setup & Repository Best Practices (v2.3.0)

**Prevents "lost 2 weeks of work" disasters**

✅ GitHub repository setup checklist (exact steps)

✅ Common error fixes documented

✅ .env file creation workarounds (IDE security restrictions)

✅ "Version control from day one" mandate

**Problem Solved:** 30% of projects started without proper version control, leading to lost work and no audit trail. Version control is now mandatory step 1, preventing data loss disasters from day one.

---

### 5. Cloud Storage & Email Services (v2.3.0, updated v2.4.0)

**Production-ready infrastructure**

✅ Cloudflare R2 setup (free egress, S3-compatible)

✅ Bunny CDN (region-specific hostname gotchas documented)

✅ Amazon SES email delivery (production-grade, $0.10/1,000 emails)

✅ SMTP configuration guidance

**Problem Solved:** Developers waste days with trial and error across different providers, hitting unexpected costs. These production-tested patterns provide reliable, cost-effective file hosting and email delivery infrastructure out of the box.

---

### 6. Standard Development Tools (v2.4.0)

**Setup time: 4 hours → 30 minutes**

✅ Homebrew (macOS package manager)

✅ Pandoc (Markdown → Rich Text for Airtable)

✅ Python dependency management

✅ check_dependencies.py automated verification

**Problem Solved:** Every project started with hours spent figuring out which tools to install and how. A standard toolkit with automated verification means a consistent environment every time — no more missing dependencies discovered mid-project.

---

### 7. MCP Servers & Browser Automation (v2.4.1)

**Test 10x faster, catch bugs before deployment**

✅ Chrome DevTools MCP setup

✅ Playwright integration

✅ Browser automation for testing

✅ Automated screenshot capture

✅ Form testing workflows

**Problem Solved:** Manual testing is slow, error-prone, and doesn't catch issues until users report them. Automated browser testing catches issues in seconds and makes regression testing automatic — hours of manual clicking replaced by instant verification.

---

### 8. Airtable Best Practices & API Security (v2.4.2)

**Saves 8+ hours debugging API failures**

✅ Always use table IDs (not table names)

✅ Personal Access Tokens (PATs), not deprecated API keys

✅ Field naming conventions

✅ Authentication best practices

**Problem Solved:** API calls silently break when tables are renamed or authentication methods are deprecated. Using stable table IDs and modern auth prevents these failures — rename a table and everything still works.

---

### 9. Common Name & Terminology Glossary (v2.6.0)

**Prevents 50+ hours of debugging**

✅ Standardized spellings (prevents database mismatches)

✅ Technical term glossary

✅ Brand consistency guidelines

**Problem Solved:** AI models introduce spelling variations ("Kerry Krieger" vs "Kerry Kriger") that silently break database lookups and API calls. A standardized glossary prevents inconsistent naming from cascading into hours of debugging — one project lost 8 hours to this exact issue.

---

### 10. File Deletion Policy (v2.6.2)

**Prevents accidental data loss**

✅ Never delete without explicit permission

✅ Files don't go to Trash when deleted via code

✅ Archive-first approach

**Problem Solved:** AI agents deleted files thinking they were helping optimize storage — but files deleted via code bypass the Trash and are gone permanently. A mandatory permission policy with archive-first approach prevents data loss disasters.

---

### 11. Version Management & Documentation Drift Prevention (v2.6.3)

**GitHub always displays correct version**

✅ VERSION file format guidelines

✅ Version Update Checklist (prevents drift)

✅ grep-based verification workflow

✅ README.md synchronization

**Problem Solved:** Projects had VERSION at v1.3.1 but README.md showed v1.0.0 — GitHub displayed the wrong version and users lost trust. A checklist and grep-based verification workflow ensures all version references stay synchronized across every file.

---

### 12. Virtual Environment Best Practices (v2.6.4)

**macOS PEP 668 compliance + universal best practice**

✅ Complete venv setup workflow (create, activate, install, deactivate)

✅ IDE configuration (Cursor/VS Code interpreter selection)

✅ Troubleshooting "externally-managed-environment" error

✅ check_dependencies.py detects venv status

✅ .gitignore patterns for venv folders

**Problem Solved:** macOS now enforces PEP 668, preventing system-wide pip installs. Developers hit confusing "externally-managed-environment" errors during setup. A clear venv workflow from day one works on all platforms and eliminates this blocker.

---

### 13. Project Kickoff Process & Verification Standards (v2.6.5)

**Ensures projects finish, not drift**

✅ Mandatory ROADMAP.md creation (AI breaks goal into 5-8 atomic steps)

✅ Mandatory STATUS.md tracking (Blockers | Decisions | Next Actions | Tech Debt)

✅ Auto-generated verification commands (scans package.json/requirements.txt)

✅ Tests MUST pass before marking steps complete

✅ Step completion protocol (no "done but broken" code)

**Problem Solved:** Projects without structure experience scope creep and never finish, and "done but broken" code ships without testing. Structured roadmaps with testable verification ensure provably working code at every milestone — no more vague goals or unclear progress.

---

### 14. Airtable Field Validation & 422 Error Prevention (v2.7.0)

**Debugging time: Hours → Seconds**

✅ Complete AirtableFieldValidator class (validates against Meta API)

✅ Fuzzy matching suggestions for typos

✅ Auto-diagnostic mode (validates on error)

✅ Single select exact matching verification

✅ Table ID validation (stable vs changeable names)

**Problem Solved:** Airtable 422 errors give no indication which field is wrong — small typos like a leading space in `' Success'` cause production failures with misleading error messages. The field validator catches these instantly instead of requiring hours of manual trial-and-error debugging.

---

### 15. Date Verification Operating Principle (v2.7.1)

**Prevents scheduling miscommunication**

✅ Operating Principle #5: Always verify dates from system info

✅ Check `Current Date:` field before date-related statements

✅ Prevents "thinking Monday when it's Tuesday" errors

✅ Verification checklist for time-sensitive statements

✅ Recurring cross-project issue now documented

**Problem Solved:** AI models incorrectly assume the current day of week despite system info showing the correct date, causing scheduling confusion like saying "tomorrow's run" when it's actually today. Mandatory date verification is a simple fix that prevents major communication errors across all projects.

---

### 16. TROUBLESHOOTING.md Standard File (v2.8.0)

**Debugging time: Saves 2-4 hours per project**

✅ TROUBLESHOOTING.md as standard file in all new projects

✅ Template structure with common categories (API issues, environment setup, MCP tools)

✅ Real-world examples (FluentCart, Python venv, MCP configuration)

✅ When to add entries: 15+ minute problems, workarounds, best practices

✅ Living document that grows with project

✅ Self-annealing: Project gets easier to work on over time

**Problem Solved:** Solutions to project-specific issues get lost in chat history or commit messages, and developers waste hours re-solving known problems weeks later. Systematic troubleshooting documentation captures solutions once and makes them referenceable forever — projects get easier to work on over time.

---

### 17. Session Handoff & Continuity System (v2.9.0)

**Context loading time: 30 minutes → <2 minutes (93% reduction)**

✅ HANDOFF.md template for session transition documents

✅ Automation scripts (generate_handoff.py, verify_handoff.py)

✅ Starting prompt with @-references for instant context loading

✅ Session verification checklist before handoff

✅ Integration with ROADMAP.md and STATUS.md

✅ Zero context loss between AI agents

**Problem Solved:** Multi-session projects lose context between AI agents, and ever-growing context windows make single-session approaches financially and environmentally wasteful. Starting prompts with @-references now load full context in under 2 minutes — new agents are productive immediately with all architectural decisions preserved.

---

### 18. Version Header Update Process (v2.9.1)

**Prevents distributed files with wrong version numbers**

✅ Explicit Step 2a: Update version header immediately after file copy

✅ Step 2b: Draft & approve Problem Solved section

✅ Step 7: Pre-commit verification checklist

**Problem Solved:** Version headers weren't getting updated when copying files for new releases (e.g., file showed v2.8.0 when it was v2.9.0). A mandatory first-step header update with pre-commit verification ensures distributed files always display the correct version number.

---

### 19. Version Update Workflow with Grep Verification (v2.9.2)

**Prevents VERSION/README.md drift - keeps GitHub homepage accurate**

✅ Pre-commit grep verification (REQUIRED step)

✅ README.md dual-location check (header AND footer)

✅ 9-step mandatory workflow with verification at step 7

✅ Complete example showing grep -n, update, verify

✅ Links to Operating Principle #4 (documentation drift)

**Problem Solved:** WP AI Commander project had VERSION at 1.1.0 but README.md still showed 1.0.0 on GitHub's homepage — users saw the wrong version, breaking trust. Mandatory grep-based verification now catches ALL old version references before committing, ensuring every file stays synchronized.

---

### 20. Single-Goal Focus Operating Principle (v2.10.0)

**Token savings: ~32% reduction (200K+ → 135K tokens)**

✅ Operating Principle #6: Focus on ONE primary goal per chat session

✅ Session start/end templates with goal definition

✅ Token budgets: 50-150K single-goal vs 200K+ multi-goal

✅ Handoff triggers: goal complete, >75% tokens, scope change

✅ Good vs bad examples (one bug vs multiple unrelated tasks)

✅ Exception handling for blocking bugs discovered during primary goal

**Problem Solved:** Multi-goal chat sessions waste significant tokens and produce unclear handoffs — a WP AI Commander session tackling four unrelated tasks consumed 250K+ tokens with unclear completion status. Breaking work into single-goal sessions reduced token usage by ~32% (to ~135K) with clear completion, easy handoffs, and fewer context-switching errors.

---

### 21. Token Optimization & Context Reduction (v2.11.0)

**Per-message token cost reduced ~60% across all projects**

✅ `.cursorignore` bootstrapping in every new project (blocks node_modules/, venv/, build artifacts)

✅ AGENTS.md trimmed from 2,548 to ~830 lines (67% reduction)

✅ STATUS.md growth limits (max 3-4 sessions in Recent Updates)

✅ Reference material relocated to SETUP_GUIDE.md (not auto-loaded)

✅ FluentMCP section removed (tool no longer used)

✅ Version History removed from distributed AGENTS.md

✅ copy_to_new_project.sh updated to include `.cursorignore` template

**Problem Solved:** AGENTS.md is loaded on every AI message and carried ~1,750 lines of setup guides, code templates, and version history that the AI never needs during active coding — plus missing `.cursorignore` let large generated files (170MB+ node_modules/) flood the context window. Relocating reference material to SETUP_GUIDE.md and adding standard `.cursorignore` patterns reduces per-message token cost by ~60%.

---

### 22. WordPress Symlink Safety Warning (v2.12.0)

**Prevents catastrophic workspace destruction during plugin development**

✅ DANGER callout: WordPress `delete_plugins()` follows symlinks and deletes the target workspace

✅ Safe removal instructions (deactivate only, remove symlink via terminal)

✅ Git safety net reminder (commit and push before deletion/reinstall testing)

✅ `.cursorrules` reminder for symlinked plugin projects

✅ Cross-reference in File Deletion Policy section

**Problem Solved:** When a WordPress plugin is developed via a symlink, deleting the plugin through WP admin causes WordPress to follow the symlink and recursively destroy the entire workspace -- source code, `.git/` history, and all project files. One project lost its entire git history (v1.0 through v1.19) to this. A concise DANGER warning with safe removal instructions prevents this catastrophic data loss.

---

### 23. WordPress Symlink Safety — Technical Safeguards (v2.13.0)

**Written warnings failed twice — now enforced with code**

✅ mu-plugin (`symlink-deletion-guard.php`) blocks WordPress from deleting symlinked plugins

✅ Auto-push git hook (`tools/protect-git.sh`) pushes to GitHub after every commit

✅ Full guide with code: `Resources/SYMLINK-SAFETY-GUIDE.md`

✅ Paste-ready setup prompt for WordPress projects: `Resources/SYMLINK-SAFETY-PROMPT.md`

✅ `copy_to_new_project.sh` distributes `protect-git.sh` to all new projects

**Problem Solved:** Despite v2.12.0's written warnings, the z2w-admin-suite workspace was destroyed a second time (2026-02-27) by WordPress's `delete_plugins()` following a symlink. Written warnings in `.cursorrules` are not sufficient because AI agents can bypass or ignore them. Technical safeguards — a mu-plugin that blocks deletion at the WordPress level and an auto-push hook that ensures code is always on GitHub — make this class of data loss impossible.

---

### 24. WordPress Plugin Framework Edition (v3.0.0)

**Complete framework rewrite for WordPress plugin development — zero Python, all PHP**

✅ `AGENTS_WP.md` and `SETUP_GUIDE_WP.md` — self-contained replacements for WP plugin projects

✅ Layer 3 redefined: PHP plugin code in `includes/`, `admin/`, `public/` (not Python scripts)

✅ WordPress coding standards, hook patterns, HPOS compatibility, module singleton pattern

✅ Plugin scaffold structure with `directives/`, `execution/` (build tooling only), `includes/`, `admin/`, `public/`

✅ Symlink safety warnings, WP-specific verification (php -l, WP_DEBUG log, browser testing)

✅ Credentials in WP Admin → Settings → `wp_options` (not `.env`)

✅ WordPress-specific Project Instantiation Prompt template

✅ Common WP gotchas documented (hook timing, nonce expiry, HPOS, option autoloading)

✅ `copy_to_new_project.sh --wordpress` for one-command WP project setup

**Problem Solved:** The generic framework was built for Python automation (venv, pip, pytest, .env credentials) — loading it in WordPress plugin projects wasted tokens on irrelevant content every message and provided no guidance on PHP hooks, HPOS, WP coding standards, or plugin architecture. A parallel WordPress edition provides complete, token-efficient instructions purpose-built for plugin development.

---

### 25. Local Site Credential Protection (v3.1.0)

**Agents may not change WordPress admin credentials without explicit user request**

✅ New operating rule in `AGENTS_WP`: do not reset or change local site passwords/usernames unless explicitly asked

✅ Applies generically to any WordPress local development environment — no site-specific names in the template

✅ Agents who need browser access to the local site must ask the user for login assistance rather than resetting credentials

**Problem Solved:** AI agents with browser access could inadvertently reset WordPress admin passwords to gain convenience access during testing, locking the user out of their own local site. A clear, generic rule prevents this without requiring per-project customization.

---

## 📊 Framework Stats

**Current Version:** 2.13.0 (Python) / 3.1.0 (WordPress)  
**Total Updates:** 25 major improvements  
**Time Saved:** 100+ hours per project (cumulative across all improvements)  
**Self-Annealing Contributions:** 10+ production projects

---

**Last Updated:** 2026-03-10  
**Repository:** https://github.com/zero2webmaster/cursor-project-templates
