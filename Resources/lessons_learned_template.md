# Lessons Learned

**Project:** [Project Name]  
**Created:** [Date]

> This file tracks insights from this project that should be contributed back to the master AGENTS.md template.

---

## Template Updates Needed

### Issue: [Brief Description]

**Found in:** [This Project Name]  
**Date Discovered:** [Date]  
**Impact:** [Low/Medium/High]

**Problem:**
- Describe the issue encountered
- What went wrong or was unclear
- What error messages appeared

**Root Cause:**
- Why did this happen?
- What was missing from the template?
- What assumption was incorrect?

**Solution:**
- What fixed the issue?
- What should be added to AGENTS.md?
- What section of AGENTS.md needs updating?

**Template Update:**
- **Section:** [e.g., "Standard Development Tools"]
- **Type:** [MAJOR/MINOR/PATCH]
- **Proposed Version:** [e.g., 2.6.3 → 2.6.4]
- **Specific Changes:** 
  - [Bullet list of exact changes needed]

**Verification:**
- [ ] Solution tested and works
- [ ] Documentation written
- [ ] Examples provided
- [ ] Ready to contribute back to template

---

## Example Entry

### Issue: macOS PEP 668 Virtual Environment Requirement

**Found in:** SAVE THE FROGS! Event Automation  
**Date Discovered:** 2026-01-12  
**Impact:** High (blocks project setup on macOS)

**Problem:**
- `pip3 install -r requirements.txt` failed with "externally-managed-environment" error
- New macOS versions enforce PEP 668 (Python package isolation)
- Template documentation didn't mention virtual environments as required
- Setup guide led users directly to pip install without venv setup

**Root Cause:**
- AGENTS.md assumed pip install works globally
- macOS security changes (PEP 668) now prevent system-wide package installs
- Virtual environments weren't emphasized as mandatory for macOS
- IDE interpreter configuration not documented

**Solution:**
- Create virtual environment: `python3 -m venv venv`
- Activate before installing: `source venv/bin/activate`
- Configure IDE to use venv interpreter
- Add venv detection to check_dependencies.py

**Template Update:**
- **Section:** Standard Development Tools (after Pandoc, before Playwright)
- **Type:** PATCH
- **Proposed Version:** 2.6.3 → 2.6.4
- **Specific Changes:**
  - Add "Python Virtual Environments (REQUIRED)" section
  - Document macOS PEP 668 enforcement
  - Provide setup instructions (create, activate, deactivate)
  - Add IDE configuration steps (Cursor/VS Code)
  - Include .gitignore entries for venv folders
  - Add troubleshooting for "externally-managed-environment" error
  - Update check_dependencies.py to detect venv status
  - Emphasize venv is NOT optional for macOS

**Verification:**
- [x] Solution tested on macOS (Sonoma 14.5)
- [x] Documentation written with code examples
- [x] IDE configuration steps verified in Cursor
- [x] Ready to contribute back to template

---

## Quick Capture Format

For rapid documentation during development:

```markdown
### [Issue Title]
- **Problem:** [One-line description]
- **Solution:** [One-line fix]
- **Template Section:** [Where this should go]
- **Version Impact:** [MAJOR/MINOR/PATCH]
```

---

## Usage Notes

**When to Add an Entry:**
1. You encounter an error not covered in AGENTS.md
2. You discover a better pattern/practice
3. You find unclear or outdated documentation
4. You implement a workaround that should be standard

**How to Contribute Back:**
1. Document the lesson here as you solve it
2. When ready, open the master template project
3. Copy this entry to that project's chat
4. AI will update AGENTS.md with your lesson
5. Version bump and push to GitHub

**Benefits:**
- Future projects avoid the same issue
- Template improves with real-world experience
- Self-annealing loop in action
- Knowledge compounds across projects

---

*This template creates a feedback loop: project → lessons → template → future projects*
