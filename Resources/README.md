# Cursor Project Templates - Resources Folder

**Version:** 2.9.2  
**Last Updated:** 2026-01-27

---

## 📁 What's in This Folder

This folder contains **reference templates** that AI uses to structure project files. You do **NOT** copy these to new projects—AI creates them automatically.

### Template Files (AI Uses These as Guides)

| File | Purpose | How AI Uses It |
|------|---------|----------------|
| **roadmap_template.md** | ROADMAP.md structure | AI reads this to create ROADMAP.md in new projects (5-8 atomic steps with verification criteria) |
| **status_template.md** | STATUS.md structure | AI reads this to create STATUS.md in new projects (Blockers / Decisions / Next Actions / Tech Debt) |
| **handoff_template.md** | HANDOFF.md structure | AI reads this to create HANDOFF.md at end of each session (session summary with starting prompt) |
| **lessons_learned_template.md** | Lessons learned structure | Create manually when you want to contribute improvements back to master template |

**New in v2.7.1-2.9.0:**

| File | Purpose | Use |
|------|---------|-----|
| **FRAMEWORK_HISTORY.md** | Complete version history (technical) | See all 17 major improvements (v1.0.0 → v2.9.0) with real-world impact |
| **FRAMEWORK_HISTORY_NOTION.md** | Version history (Notion-optimized) | Copy-paste sections into Notion sales page when releasing new versions |
| **TERMINAL_GUIDE.md** | Terminal/shell commands guide | Comprehensive guide for non-technical users (copy to Notion) |
| **PROMPT_CREATE_ROADMAP_STATUS.md** | Prompt template | Detailed prompt for generating ROADMAP/STATUS in existing projects |
| **execution_scripts/generate_handoff.py** | Auto-generate HANDOFF.md | Creates draft handoff from git/STATUS/ROADMAP state |
| **execution_scripts/verify_handoff.py** | Verify handoff readiness | Checks git status, file completeness before ending session |

**Key Point:** These templates are **reference-only**. AI auto-creates `ROADMAP.md`, `STATUS.md`, and `HANDOFF.md` during/after sessions. You never copy them manually.

### Session Continuity Scripts

| File | Purpose | Use |
|------|---------|-----|
| **execution_scripts/generate_handoff.py** | Auto-generate HANDOFF.md | Run at end of session: `python3 execution/generate_handoff.py` |
| **execution_scripts/verify_handoff.py** | Verify handoff readiness | Verify before ending: `python3 execution/verify_handoff.py` |

**Benefits:**
- Context loading: 30 min → <2 min (93% reduction)
- Auto-generated session summaries with TODOs
- Clean handoffs with starting prompts
- Verified git/file completeness

### Other Reference Files

| File | Purpose | Use |
|------|---------|-----|
| **README.md** | This file | Documentation for this folder |
| **CHANGELOG_v2.4.2.md** | Historical changelog | Reference only |
| **CURSORRULES_EXAMPLE.md** | Full project example | Reference for creating custom .cursorrules |
| **copy_to_new_project.sh** | Helper script | Run from parent directory to copy framework files |

---

## 🚀 Quick Start: How Files Get Into Projects

### Files You Copy (From Parent Directory)

```bash
# Navigate to your new project
cd /path/to/your/new/project

# Copy these 3 files from parent directory:
cp /path/to/Templates/AGENTS_v2.9.0.md ./AGENTS.md
cp /path/to/Templates/SETUP_GUIDE_v2.4.0.md ./SETUP_GUIDE.md
cp /path/to/Templates/.cursorrules ./.cursorrules

# Create VERSION file (single line)
echo "1.0.0" > VERSION

# Create README.md with both versions
cat > README.md << 'EOF'
# My Project Name

**Version:** 1.0.0 | **Framework:** 2.9.0

[Project description here...]
EOF
```

### Files AI Creates Automatically

On your first chat in the new project, AI will:
1. **Read your goal** from your prompt
2. **Create `ROADMAP.md`** (using roadmap_template.md as guide)
   - Breaks goal into 5-8 atomic, testable steps
   - Each step has verification criteria
3. **Create `STATUS.md`** (using status_template.md as guide)
   - Sections: Blockers | Decisions | Next Actions | Tech Debt
4. **Output:** "ROADMAP.md & STATUS.md created. Current step: 1. Ready."

**At end of each session:**
- AI creates `HANDOFF.md` (using handoff_template.md as guide)
- Or use automation: `python3 execution/generate_handoff.py`
- Includes session summary and starting prompt for next agent

**You never manually copy these template files.**

---

## 📊 Quick Stats

**Current Framework Version:** 2.9.2  
**Last Updated:** 2026-01-27  
**Total Major Improvements:** 18 (v1.0.0 → v2.9.2)

**Want to see the full version history?**  
→ [See FRAMEWORK_HISTORY.md](FRAMEWORK_HISTORY.md) for detailed technical breakdown of all 18 major updates  
→ [See FRAMEWORK_HISTORY_NOTION.md](FRAMEWORK_HISTORY_NOTION.md) for Notion-optimized version (sales page ready)

---

## ❓ FAQ

**Q: Do I copy roadmap_template.md to my project?**  
A: **No!** AI reads it and creates `ROADMAP.md` automatically. You never copy it.

**Q: When does AI create ROADMAP.md?**  
A: On your first chat after project setup. AI reads your goal and generates ROADMAP.md with 5-8 atomic steps.

**Q: What about HANDOFF.md?**  
A: Created at end of each session (manually or with `python3 execution/generate_handoff.py`). Contains session summary and starting prompt for next agent.

**Q: What if I want to update the master template?**  
A: Create `lessons_learned.md` in your project (using lessons_learned_template.md as guide), document discoveries, then contribute back to master template in a separate session.

**Q: Why are templates in Resources/ instead of root?**  
A: Cleaner organization. Root folder = files you copy. Resources/ = reference files AI uses.

---

**Maintained by:** Dr. Kerry Kriger | [Zero2Webmaster](https://zero2webmaster.com/)  
**Original Architecture:** Nick Saraev (v1.0.0)  
**Current Framework:** v2.9.2 (2026-01-27)
