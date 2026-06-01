# Prompt Template: Create ROADMAP.md & STATUS.md for Existing Projects

**Purpose:** Generate ROADMAP.md and STATUS.md for projects that don't have them yet

---

## Copy-Paste Prompt (Use in Any Project)

```
@AGENTS.md 

I need you to create ROADMAP.md and STATUS.md for this project based on its current state.

**Context to analyze:**
1. Read @README.md to understand the project goal
2. Scan the codebase to see what's already built
3. Check git log to see recent activity
4. Look for any TODO comments in code
5. Check if there are any directive files

**ROADMAP.md Requirements:**
- Break the remaining work into 5-8 atomic steps
- Each step should be:
  - Specific (not vague like "improve performance")
  - Testable (include verification commands)
  - Completable in 1-4 hours of focused work
- Mark already-completed features as ✅
- Mark current work as 🔄
- Mark future work as ⏳
- Include verification commands for each step (npm test, pytest, etc.)

**STATUS.md Requirements:**
- ## Blockers - Current blockers (or "None currently")
- ## Decisions - Key technical/architectural decisions made so far
- ## Next Actions - Immediate next steps (this week)
- ## Tech Debt - Known issues to address later

**Project Context:**
[Optionally add specific context about this project, like:]
- This is a [type] project (web app, API, CLI tool, etc.)
- Tech stack: [languages/frameworks]
- Current version: [if known]
- Main blocker right now: [if any]

Please analyze the project and create both files.
```

---

## Example Usage

### Scenario 1: Web App Project

```
@AGENTS.md 

I need you to create ROADMAP.md and STATUS.md for this project based on its current state.

**Context to analyze:**
1. Read @README.md to understand the project goal
2. Scan the codebase to see what's already built
3. Check git log to see recent activity
4. Look for any TODO comments in code
5. Check if there are any directive files

**ROADMAP.md Requirements:**
- Break the remaining work into 5-8 atomic steps
- Each step should be:
  - Specific (not vague like "improve performance")
  - Testable (include verification commands)
  - Completable in 1-4 hours of focused work
- Mark already-completed features as ✅
- Mark current work as 🔄
- Mark future work as ⏳
- Include verification commands for each step (npm test, pytest, etc.)

**STATUS.md Requirements:**
- ## Blockers - Current blockers (or "None currently")
- ## Decisions - Key technical/architectural decisions made so far
- ## Next Actions - Immediate next steps (this week)
- ## Tech Debt - Known issues to address later

**Project Context:**
- This is a React web app with WordPress backend
- Tech stack: React, TypeScript, WordPress REST API, Airtable
- Currently working on user authentication
- Main blocker: Airtable field validation errors

Please analyze the project and create both files.
```

---

### Scenario 2: Python Script Project

```
@AGENTS.md 

I need you to create ROADMAP.md and STATUS.md for this project based on its current state.

**Context to analyze:**
1. Read @README.md to understand the project goal
2. Scan the codebase to see what's already built
3. Check git log to see recent activity
4. Look for any TODO comments in code
5. Check if there are any directive files

**ROADMAP.md Requirements:**
- Break the remaining work into 5-8 atomic steps
- Each step should be:
  - Specific (not vague like "improve performance")
  - Testable (include verification commands)
  - Completable in 1-4 hours of focused work
- Mark already-completed features as ✅
- Mark current work as 🔄
- Mark future work as ⏳
- Include verification commands for each step (npm test, pytest, etc.)

**STATUS.md Requirements:**
- ## Blockers - Current blockers (or "None currently")
- ## Decisions - Key technical/architectural decisions made so far
- ## Next Actions - Immediate next steps (this week)
- ## Tech Debt - Known issues to address later

**Project Context:**
- This is a Python automation script
- Tech stack: Python 3.11, Airtable API, Bunny.net API
- Migrates videos from Vimeo to Bunny
- Script works but needs error handling improvements

Please analyze the project and create both files.
```

---

## Tips for Better Results

### Before Running the Prompt

1. **Make sure AGENTS.md exists in the project**
   - If not: `cp /path/to/Templates/AGENTS_v2.7.1.md ./AGENTS.md`

2. **Have a clear README.md**
   - AI uses this to understand project goal
   - If missing, create a basic one first

3. **Commit current work**
   - AI looks at git log for context
   - Clean slate = clearer analysis

---

### Customizing the Prompt

**Add these sections if relevant:**

**For API Projects:**
```
**API Endpoints:**
- List current endpoints and which are complete
- Which endpoints still need implementation
```

**For Complex Projects:**
```
**Current Phase:**
- We're in [planning/development/testing/deployment] phase
- Focus should be on [specific area]
```

**For Multi-Developer Projects:**
```
**Team Context:**
- I'm working on [feature X]
- Teammate is handling [feature Y]
- Need to coordinate on [shared component]
```

---

## What AI Will Do

1. **Scan your codebase**
   - Identify completed features
   - Find TODO comments
   - Check package.json/requirements.txt for tech stack

2. **Analyze git history**
   - See what you've been working on
   - Understand project velocity

3. **Read directives (if present)**
   - Understand established workflows
   - Maintain consistency

4. **Generate ROADMAP.md**
   - 5-8 atomic steps
   - Verification commands for each
   - Realistic time estimates

5. **Generate STATUS.md**
   - Current blockers (real issues, not generic)
   - Actual decisions made (based on code)
   - Concrete next actions
   - Real tech debt (from TODOs and code comments)

---

## After Generation

### Review and Refine

**ROADMAP.md:**
- ✅ Are steps atomic? (Can each be done in 1 session?)
- ✅ Are verification commands correct for your stack?
- ✅ Is order logical? (Dependencies make sense?)
- ✅ Are completed steps accurately marked?

**STATUS.md:**
- ✅ Are blockers real? (Not generic "need to test more")
- ✅ Are decisions documented? (Why we chose X over Y)
- ✅ Are next actions specific? (Not "improve code")
- ✅ Is tech debt real? (Based on actual code issues)

### Update Immediately

After AI generates them:
1. Read through both files
2. Correct any misunderstandings
3. Add context AI couldn't infer
4. Commit them to git

---

## Common Issues & Solutions

### Issue: Generic Roadmap

**Bad:**
```markdown
## Step 1: ⏳ Improve Performance
## Step 2: ⏳ Add Features
## Step 3: ⏳ Fix Bugs
```

**Good:**
```markdown
## Step 1: ⏳ Add Caching Layer (Redis)
**Verification:** `ab -n 1000 -c 10 http://localhost:3000/api/users` shows <100ms avg

## Step 2: ⏳ Implement User Authentication (JWT)
**Verification:** `npm test -- auth.test.ts` passes all tests

## Step 3: ⏳ Fix Airtable Field Validation
**Verification:** `python3 execution/validate_airtable_fields.py` shows no errors
```

---

### Issue: Empty Status Sections

**Bad:**
```markdown
## Blockers
None

## Decisions
TBD

## Next Actions
Continue development
```

**Solution:** Add this to your prompt:
```
**Important:** 
- Don't use generic placeholders like "TBD" or "Continue development"
- If you can't find real blockers/decisions, state "None identified yet" and explain why
- Next actions should be specific tasks, not vague goals
```

---

### Issue: AI Can't Find Context

**Solution:** Provide more context in prompt:
```
**Additional Context:**
- We recently switched from MongoDB to Airtable (decision made last week)
- Current blocker: Airtable rate limiting on batch updates
- Next priority: Implement retry logic with exponential backoff
- Tech debt: No tests for API client (was rushed for demo)
```

---

## Version Control

After generating ROADMAP.md and STATUS.md:

```bash
# Review the files
cat ROADMAP.md
cat STATUS.md

# If satisfied, commit them
git add ROADMAP.md STATUS.md
git commit -m "Add ROADMAP.md and STATUS.md for project management

Generated from current project state using AGENTS.md framework.

- ROADMAP: 8 atomic steps with verification commands
- STATUS: Current blockers, decisions, next actions, tech debt"

# Push to GitHub
git push origin main
```

---

## When to Regenerate

**Regenerate ROADMAP.md when:**
- You complete a major milestone
- Project scope changes significantly
- You discover new requirements
- Steps are no longer relevant

**Update STATUS.md:**
- Every chat session (start and end)
- When blockers change
- When making key decisions
- When identifying new tech debt

---

**Last Updated:** 2026-01-13  
**Framework Version:** 2.7.1  
**Location:** `/Resources/PROMPT_CREATE_ROADMAP_STATUS.md`
