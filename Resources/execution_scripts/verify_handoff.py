#!/usr/bin/env python3
"""
Verify HANDOFF.md is ready and project state is clean.

This script checks:
- Git status is clean (or only safe untracked files)
- All commits pushed to remote
- VERSION file exists and valid
- ROADMAP.md exists
- STATUS.md exists  
- HANDOFF.md exists and has no [TODO] placeholders
- No uncommitted changes (except safe files)

Usage:
    python3 execution/verify_handoff.py
    python3 execution/verify_handoff.py --strict  # Fail on warnings
"""

import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


class Colors:
    """ANSI color codes."""
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def print_success(msg: str):
    """Print success message."""
    print(f"{Colors.GREEN}✅ {msg}{Colors.RESET}")


def print_warning(msg: str):
    """Print warning message."""
    print(f"{Colors.YELLOW}⚠️  {msg}{Colors.RESET}")


def print_error(msg: str):
    """Print error message."""
    print(f"{Colors.RED}❌ {msg}{Colors.RESET}")


def print_info(msg: str):
    """Print info message."""
    print(f"{Colors.BLUE}ℹ️  {msg}{Colors.RESET}")


def run_git_command(cmd: List[str]) -> Tuple[bool, str]:
    """Run git command and return (success, output)."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, e.stderr.strip()


def check_git_status() -> Tuple[bool, List[str]]:
    """Check if git status is clean."""
    success, output = run_git_command(['git', 'status', '--short'])
    if not success:
        return False, ["Git command failed"]
    
    if not output:
        return True, []
    
    # Parse git status
    issues = []
    safe_files = {
        '.cursorindexingignore',
        '.specstory/',
        'node_modules/',
        '__pycache__/',
        '.pytest_cache/',
        '.venv/',
        'venv/',
        '.DS_Store'
    }
    
    for line in output.split('\n'):
        if not line.strip():
            continue
        
        # Check if it's a safe untracked file
        status = line[:2]
        filename = line[3:].strip()
        
        is_safe = any(filename.startswith(safe) or filename == safe 
                     for safe in safe_files)
        
        if status == '??':  # Untracked
            if not is_safe:
                issues.append(f"Untracked file: {filename}")
        else:  # Modified, staged, etc.
            issues.append(f"Uncommitted change: {filename} ({status})")
    
    return len(issues) == 0, issues


def check_git_push_status() -> Tuple[bool, str]:
    """Check if all commits are pushed."""
    # Get current branch
    success, branch = run_git_command(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
    if not success:
        return False, "Could not determine current branch"
    
    # Check if branch has upstream
    success, upstream = run_git_command(['git', 'rev-parse', '--abbrev-ref', '@{u}'])
    if not success:
        return False, f"Branch '{branch}' has no upstream set"
    
    # Check for unpushed commits
    success, unpushed = run_git_command(['git', 'log', '@{u}..', '--oneline'])
    if not success:
        return False, "Could not check for unpushed commits"
    
    if unpushed:
        return False, f"Unpushed commits:\n{unpushed}"
    
    return True, ""


def check_file_exists(filepath: Path, required: bool = True) -> Tuple[bool, str]:
    """Check if file exists."""
    if filepath.exists():
        return True, ""
    
    if required:
        return False, f"Required file missing: {filepath.name}"
    else:
        return True, f"Optional file missing: {filepath.name} (recommended)"


def check_handoff_complete(handoff_path: Path) -> Tuple[bool, List[str]]:
    """Check if HANDOFF.md has been completed."""
    if not handoff_path.exists():
        return False, ["HANDOFF.md does not exist"]
    
    content = handoff_path.read_text()
    issues = []
    
    # Check for TODO placeholders
    lines = content.split('\n')
    todo_lines = []
    for i, line in enumerate(lines, 1):
        if '[TODO:' in line or '[TODO]' in line:
            todo_lines.append(f"Line {i}: {line.strip()}")
    
    if todo_lines:
        issues.append(f"Found {len(todo_lines)} incomplete TODO items:")
        issues.extend(f"  {line}" for line in todo_lines[:5])
        if len(todo_lines) > 5:
            issues.append(f"  ... and {len(todo_lines) - 5} more")
    
    # Check for draft status
    if '**Handoff Status:** 🚧 DRAFT' in content:
        issues.append("Handoff status is still DRAFT (should be ✅ CLEAN)")
    
    if '**Ready for Next Session:** ❌ NO' in content:
        issues.append("Not marked as ready for next session")
    
    return len(issues) == 0, issues


def check_version_file(version_path: Path) -> Tuple[bool, str]:
    """Check if VERSION file exists and is valid."""
    if not version_path.exists():
        return False, "VERSION file does not exist"
    
    content = version_path.read_text().strip()
    if not content:
        return False, "VERSION file is empty"
    
    # Check if it has reasonable content
    lines = [l.strip() for l in content.split('\n') if l.strip()]
    if len(lines) < 1:
        return False, "VERSION file has no valid content"
    
    return True, ""


def main():
    """Main verification logic."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Verify handoff readiness'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Treat warnings as errors'
    )
    
    args = parser.parse_args()
    
    project_root = Path.cwd()
    errors = []
    warnings = []
    
    print(f"\n{Colors.BOLD}🔍 Verifying Handoff Readiness{Colors.RESET}\n")
    
    # 1. Check git status
    print("Checking git status...")
    clean, issues = check_git_status()
    if clean:
        print_success("Git working directory is clean")
    else:
        for issue in issues:
            print_error(issue)
        errors.append("Git working directory has uncommitted changes")
    
    # 2. Check if commits are pushed
    print("\nChecking git push status...")
    pushed, msg = check_git_push_status()
    if pushed:
        print_success("All commits pushed to remote")
    else:
        print_warning(msg)
        warnings.append("Unpushed commits")
    
    # 3. Check VERSION file
    print("\nChecking VERSION file...")
    valid, msg = check_version_file(project_root / 'VERSION')
    if valid:
        print_success("VERSION file exists and is valid")
    else:
        print_warning(msg)
        warnings.append("VERSION file issue")
    
    # 4. Check ROADMAP.md
    print("\nChecking ROADMAP.md...")
    exists, msg = check_file_exists(project_root / 'ROADMAP.md', required=False)
    if exists and not msg:
        print_success("ROADMAP.md exists")
    else:
        print_warning(msg)
        warnings.append(msg)
    
    # 5. Check STATUS.md
    print("\nChecking STATUS.md...")
    exists, msg = check_file_exists(project_root / 'STATUS.md', required=False)
    if exists and not msg:
        print_success("STATUS.md exists")
    else:
        print_warning(msg)
        warnings.append(msg)
    
    # 6. Check HANDOFF.md completeness
    print("\nChecking HANDOFF.md...")
    complete, issues = check_handoff_complete(project_root / 'HANDOFF.md')
    if complete:
        print_success("HANDOFF.md exists and is complete")
    else:
        for issue in issues:
            print_error(issue)
        errors.append("HANDOFF.md incomplete")
    
    # 7. Check for orphaned temp files
    print("\nChecking for temporary files...")
    temp_patterns = ['temp_*.py', 'test_*.tmp', '*.pyc', '.DS_Store']
    found_temp = []
    for pattern in temp_patterns:
        found_temp.extend(project_root.glob(pattern))
    
    if not found_temp:
        print_success("No temporary files found")
    else:
        for temp_file in found_temp:
            print_warning(f"Temp file: {temp_file.name}")
        warnings.append("Temporary files present")
    
    # Summary
    print(f"\n{Colors.BOLD}{'='*50}{Colors.RESET}")
    print(f"{Colors.BOLD}Summary{Colors.RESET}\n")
    
    if errors:
        print_error(f"Found {len(errors)} error(s):")
        for error in errors:
            print(f"  • {error}")
        print()
    
    if warnings:
        print_warning(f"Found {len(warnings)} warning(s):")
        for warning in warnings:
            print(f"  • {warning}")
        print()
    
    # Final verdict
    if errors:
        print_error("Handoff NOT ready - fix errors above")
        sys.exit(1)
    elif warnings and args.strict:
        print_warning("Handoff has warnings (strict mode)")
        sys.exit(1)
    elif warnings:
        print_warning("Handoff ready with warnings")
        print_info("Consider addressing warnings before ending session")
        sys.exit(0)
    else:
        print_success("Handoff ready! All checks passed ✨")
        print()
        print_info("Ready to end session and hand off to next agent")
        sys.exit(0)


if __name__ == '__main__':
    main()
