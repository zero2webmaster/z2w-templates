#!/usr/bin/env python3
"""
Generate HANDOFF.md automatically from project state.

This script reads:
- Git log for recent commits
- STATUS.md for current state
- ROADMAP.md for progress
- VERSION file (if exists)

And generates a HANDOFF.md with all critical context for next session.

Usage:
    python3 execution/generate_handoff.py
    python3 execution/generate_handoff.py --output custom_handoff.md
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


def run_git_command(cmd: list[str]) -> str:
    """Run a git command and return output."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"


def get_git_info() -> dict:
    """Extract git information."""
    return {
        'branch': run_git_command(['git', 'rev-parse', '--abbrev-ref', 'HEAD']),
        'last_commit': run_git_command(['git', 'log', '-1', '--format=%h - "%s"']),
        'last_commit_hash': run_git_command(['git', 'rev-parse', '--short', 'HEAD']),
        'remote': run_git_command(['git', 'remote', 'get-url', 'origin']),
        'status': run_git_command(['git', 'status', '--short'])
    }


def read_file_safe(filepath: Path) -> Optional[str]:
    """Read file safely, return None if doesn't exist."""
    try:
        return filepath.read_text()
    except FileNotFoundError:
        return None


def get_project_info() -> dict:
    """Extract project information from various files."""
    project_root = Path.cwd()
    
    # Try to get project name from directory or git remote
    project_name = project_root.name
    
    # Try to get version from VERSION file
    version_file = project_root / 'VERSION'
    version = read_file_safe(version_file)
    if version:
        version = version.strip().split('\n')[0]  # First line only
    else:
        version = 'Unknown'
    
    # Check if STATUS.md exists
    status_exists = (project_root / 'STATUS.md').exists()
    roadmap_exists = (project_root / 'ROADMAP.md').exists()
    
    return {
        'name': project_name,
        'version': version,
        'status_exists': status_exists,
        'roadmap_exists': roadmap_exists
    }


def generate_handoff(output_path: Path = None) -> str:
    """Generate HANDOFF.md content."""
    if output_path is None:
        output_path = Path.cwd() / 'HANDOFF.md'
    
    git_info = get_git_info()
    project_info = get_project_info()
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Parse framework version from VERSION file if exists
    framework_version = "Unknown"
    version_content = read_file_safe(Path.cwd() / 'VERSION')
    if version_content:
        lines = version_content.strip().split('\n')
        for line in lines:
            if line.startswith('Framework:'):
                framework_version = line.split('Framework:')[1].strip()
                break
    
    # Determine git status
    if not git_info['status']:
        git_status = "Clean (no uncommitted changes)"
    else:
        git_status = "Uncommitted changes present"
    
    content = f"""# Session Handoff - {today}

**Session End:** {today}  
**Duration:** [TODO: Fill in ~X hours]  
**Framework Version:** {framework_version}  
**Last Commit:** {git_info['last_commit_hash']}

---

## ✅ What Was Accomplished This Session

### Major Deliverables
- [TODO: Fill in - what features/components were completed]

### Key Updates
- **[Component]:** [TODO: What changed and why]

### Tests/Verification
- [TODO: What was tested and results]

---

## 🎯 Key Decisions Made

### Decision 1: [TODO: Decision Title]
**Decision:** [TODO: What was decided]

**Rationale:** [TODO: Why this approach was chosen]

**Impact:** [TODO: How this affects the project]

---

## 📋 Outstanding Work Items

### Immediate (Next Session)
- [ ] [TODO: Next priority tasks]

### From ROADMAP
"""

    # Add ROADMAP reference if it exists
    if project_info['roadmap_exists']:
        content += "- See ROADMAP.md for full progress tracking\n"
    else:
        content += "- [ ] No ROADMAP.md found - consider creating one\n"
    
    content += f"""
---

## 🚧 Known Issues / Blockers

"""

    # Reference STATUS.md if it exists
    if project_info['status_exists']:
        content += "See STATUS.md for current blockers and tech debt.\n\n**Quick Summary:**\n- [TODO: Add critical blockers here]\n"
    else:
        content += "[TODO: Document any blockers or known issues]\n"
    
    content += f"""
---

## 📦 Git Status

**Current Branch:** {git_info['branch']}  
**Last Commit:** {git_info['last_commit']}  
**Remote:** {git_info['remote']}  
**Status:** {git_status}

"""

    if git_info['status']:
        content += f"""**Uncommitted Changes:**
```
{git_info['status']}
```
"""
    else:
        content += "**Uncommitted Changes:** None\n"

    content += f"""
---

## 🔑 Critical Context for Next Agent

### Project Architecture
- **Type:** [TODO: Web app/CLI tool/API/etc.]
- **Tech Stack:** [TODO: Languages, frameworks, libraries]
- **Structure:** [TODO: Key folders and their purposes]

### Key Files to Understand
- [TODO: List 3-5 most important files to read]

### Environment & Setup
- **Runtime:** [TODO: Python 3.x, Node 18, etc.]
- **Dependencies:** [TODO: How to install]
- **Environment Variables:** [TODO: Critical .env variables]

---

## 📚 Files to Read First (In Order)

### Essential Context (< 5 minutes)
"""

    if project_info['roadmap_exists']:
        content += "1. **ROADMAP.md** - Current progress and next steps (~2 min)\n"
    if project_info['status_exists']:
        content += "2. **STATUS.md** - Current state, blockers, decisions (~2 min)\n"
    
    content += """3. **This file** (HANDOFF.md) - What just happened (~1 min)

### Technical Context (5-15 minutes)
4. **README.md** - Project overview (~3 min)
5. [TODO: Add other key files to read]

---

## ⚠️ Warnings & Important Notes

### DO NOT
- ❌ [TODO: Critical things to avoid]

### ALWAYS
- ✅ [TODO: Important practices to follow]

### GOOD TO KNOW
- 💡 [TODO: Helpful tips about the project]

---

## ✅ Session Verification Checklist

Before ending session, verify:
- [ ] All code changes committed
- [ ] Tests passing (if applicable)
"""

    if project_info['status_exists']:
        content += "- [ ] STATUS.md updated with latest decisions/blockers\n"
    if project_info['roadmap_exists']:
        content += "- [ ] ROADMAP.md progress updated\n"
    
    content += """- [ ] This HANDOFF.md completed with real information
- [ ] Git pushed to remote (or reason documented)
- [ ] No orphaned temp files left behind

---

## 🚀 Starting Prompt for Next Session

**Copy/paste this to start next session:**

```
I'm picking up from the last session. Let me get up to speed:

@HANDOFF.md - What happened last session
"""

    if project_info['status_exists']:
        content += "@STATUS.md - Current state and blockers\n"
    if project_info['roadmap_exists']:
        content += "@ROADMAP.md - Progress and next steps\n"
    
    content += """
Ready to continue from where we left off!
```

**Context Load Time:** < 2 minutes  
**Priority Focus:** [TODO: What should be worked on next]

---

## 💡 Suggested Improvements

### To This Handoff Process
- [TODO: How can future handoffs be improved?]

### To Project Structure
- [TODO: Any organizational improvements?]

### To Workflow
- [TODO: Any workflow improvements?]

---

## 🎓 Session Learnings

### What Worked Well
- ✅ [TODO: What was effective this session?]

### What Could Improve
- 🔄 [TODO: What could be better?]

### Patterns to Replicate
- 🎯 [TODO: What patterns should be used again?]

---

**Handoff Status:** 🚧 DRAFT (needs completion)  
**Ready for Next Session:** ❌ NO (complete TODO items first)  
**Estimated Context Load Time:** < 2 minutes (once completed)

---

## 📝 Notes for Completing This Handoff

This is an **auto-generated draft**. Please:

1. Replace all [TODO] placeholders with real information
2. Fill in session duration and accomplishments
3. Document key decisions made
4. Update git status if changes were made after generation
5. Complete the verification checklist
6. Change status to ✅ CLEAN when done

**Generated by:** execution/generate_handoff.py  
**Generated at:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

    return content


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Generate HANDOFF.md from current project state'
    )
    parser.add_argument(
        '--output', '-o',
        type=Path,
        default=Path.cwd() / 'HANDOFF.md',
        help='Output file path (default: ./HANDOFF.md)'
    )
    
    args = parser.parse_args()
    
    print(f"🔄 Generating handoff document...")
    
    # Generate content
    content = generate_handoff(args.output)
    
    # Write to file
    args.output.write_text(content)
    
    print(f"✅ Generated: {args.output}")
    print(f"📝 Please complete all [TODO] items before ending session!")
    print(f"")
    print(f"Next steps:")
    print(f"  1. Open {args.output}")
    print(f"  2. Replace all [TODO] placeholders")
    print(f"  3. Run: python3 execution/verify_handoff.py")


if __name__ == '__main__':
    main()
