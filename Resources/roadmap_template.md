# Project Roadmap

**Project:** [Project Name]  
**Goal:** [High-level objective in 1-2 sentences]  
**Created:** [Date]  
**Last Updated:** [Date]

---

## Overview

This roadmap breaks the project into atomic, testable steps. Each step should be completable in a single focused chat session.

**Progress:** [X] of [Y] steps complete

---

## Step 1: [Feature/Task Name]

**Goal:** [Specific, measurable objective]

**Tasks:**
- [ ] [Subtask 1]
- [ ] [Subtask 2]
- [ ] [Subtask 3]

**Verification (✅ Criteria):**
- [ ] Tests pass: `npm test` (or `pytest` for Python)
- [ ] Build succeeds: `npm run build`
- [ ] Linter clean: `npm run lint` (or `ruff check` for Python)
- [ ] Manual verification: [Specific action/screenshot]

**Status:** ⏳ In Progress / ✅ Complete / 🚫 Blocked  
**Completed:** [Date if complete]  
**Notes:** [Any blockers, decisions, or context]

---

## Step 2: [Feature/Task Name]

**Goal:** [Specific, measurable objective]

**Tasks:**
- [ ] [Subtask 1]
- [ ] [Subtask 2]
- [ ] [Subtask 3]

**Verification (✅ Criteria):**
- [ ] Tests pass: `npm test`
- [ ] Integration test: [Specific scenario]
- [ ] Performance benchmark: [Metric, e.g., "API responds <500ms"]

**Status:** 📋 Pending  
**Depends On:** Step 1 must be complete  
**Notes:** [Pre-planning notes, design decisions]

---

## Step 3: [Feature/Task Name]

**Goal:** [Specific, measurable objective]

**Tasks:**
- [ ] [Subtask 1]
- [ ] [Subtask 2]

**Verification (✅ Criteria):**
- [ ] Unit tests: `npm test -- component.test.js`
- [ ] E2E test: `npm run cypress` (or `playwright test`)
- [ ] Accessibility: `npm run a11y-check`

**Status:** 📋 Pending  
**Depends On:** Step 2 must be complete

---

## Step 4: [Feature/Task Name]

**Goal:** [Specific, measurable objective]

**Tasks:**
- [ ] [Subtask 1]
- [ ] [Subtask 2]

**Verification (✅ Criteria):**
- [ ] All tests pass: `npm test`
- [ ] Security audit: `npm audit`
- [ ] Documentation updated

**Status:** 📋 Pending  
**Depends On:** Step 3 must be complete

---

## Step 5: [Feature/Task Name]

**Goal:** [Specific, measurable objective]

**Tasks:**
- [ ] [Subtask 1]
- [ ] [Subtask 2]

**Verification (✅ Criteria):**
- [ ] Full test suite passes
- [ ] Staging deployment successful
- [ ] Stakeholder approval

**Status:** 📋 Pending  
**Depends On:** Step 4 must be complete

---

## Completed Steps Archive

### ✅ Step 1: [Name] - Completed [Date]
- [Brief summary of what was accomplished]
- [Link to commit or PR if applicable]

---

## Notes & Decisions

**Key Decisions:**
- [Date]: Decision about [X] - [Rationale]
- [Date]: Chose [Y] over [Z] because [reason]

**Dependencies:**
- [External API/service needed]
- [Third-party library version requirements]

**Future Enhancements (Post-MVP):**
- [Feature idea for later]
- [Performance optimization to revisit]

---

## Status Indicators

- 📋 **Pending** - Not started yet
- ⏳ **In Progress** - Currently working on
- ✅ **Complete** - Verified and working
- 🚫 **Blocked** - Cannot proceed (see STATUS.md for details)
- 🔄 **Needs Revision** - Complete but needs changes

---

**How to Use This Roadmap:**

1. **At Start of Each Session:** "@ROADMAP.md, what's next?"
2. **During Work:** Update task checkboxes as you complete them
3. **Before Marking ✅:** Run ALL verification commands
4. **After Step Complete:** Update status, add completion date, archive if desired
5. **Track Blockers:** If stuck, update status to 🚫 and document in STATUS.md

---

*This roadmap is a living document. Update it as the project evolves and scope changes.*
