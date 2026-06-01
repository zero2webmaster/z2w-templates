# Terminal & Shell Commands Guide for Non-Technical Users

**For:** Zero2Webmaster / Kerry Kriger  
**Purpose:** Reference guide for common terminal/shell operations  
**Platform:** macOS (zsh shell)

---

## 📖 Table of Contents

1. [What is the Terminal?](#what-is-the-terminal)
2. [Opening Terminal](#opening-terminal)
3. [Where to Enter Commands](#where-to-enter-commands)
4. [Basic Navigation](#basic-navigation)
5. [GitHub Account Switching](#github-account-switching)
6. [Git Commands](#git-commands)
7. [File Operations](#file-operations)
8. [Common Patterns](#common-patterns)
9. [Troubleshooting](#troubleshooting)

---

## What is the Terminal?

**Terminal** (also called "shell" or "command line") is a text-based interface for controlling your Mac.

**Think of it like:**
- **Finder** = Visual file browser (clicking, dragging)
- **Terminal** = Text-based file browser (typing commands)

**Why use it?**
- Faster for repetitive tasks
- Required for git operations
- More powerful than clicking around
- AI agents can guide you with commands

**Common names (all mean the same thing):**
- Terminal
- Shell
- Command Line
- CLI (Command-Line Interface)
- zsh (the shell program macOS uses)

---

## Opening Terminal

### Method 1: Spotlight Search (Fastest)
1. Press `Cmd + Space`
2. Type: `terminal`
3. Press `Enter`

### Method 2: Applications Folder
1. Open Finder
2. Go to: Applications → Utilities → Terminal
3. Double-click Terminal

### Method 3: From Cursor IDE
- Cursor has built-in terminals
- Bottom panel → Terminal tab
- Same as standalone Terminal app

---

## Where to Enter Commands

### The Prompt

When you open Terminal, you see something like:

```
kerrykriger@MacBook-Pro-14-2023Nov ~ %
```

**This is called the "prompt"** - it means Terminal is ready for your command.

**Parts of the prompt:**
- `kerrykriger` = Your username
- `MacBook-Pro-14-2023Nov` = Your computer name
- `~` = Current directory (~ means "home folder")
- `%` = Ready for command (in zsh)

**You type commands AFTER the `%`**

---

## Basic Navigation

### Where Am I? (Print Working Directory)

```bash
pwd
```

**Output example:**
```
/Users/kerrykriger/Desktop/Zero2Webmaster/AI/Templates
```

**Translation:** "You are currently in the Templates folder"

---

### Change Directory

```bash
cd /path/to/folder
```

**Examples:**

```bash
# Go to Templates project
cd /Users/kerrykriger/Desktop/Zero2Webmaster/AI/Templates

# Go to Desktop
cd ~/Desktop

# Go to home folder
cd ~

# Go up one level
cd ..

# Go to previous directory
cd -
```

**Shortcuts:**
- `~` = Your home folder (`/Users/kerrykriger`)
- `.` = Current directory
- `..` = Parent directory (one level up)

---

### List Files

```bash
ls
```

**Output example:**
```
AGENTS_v2.7.1.md
README.md
Archives/
Resources/
```

**Useful variations:**

```bash
# List with details (file sizes, dates)
ls -la

# List only markdown files
ls *.md

# List sorted by modification date
ls -lt
```

---

## GitHub Account Switching

### Why You Need This

You have 3 GitHub accounts:
- **zero2webmaster** - Main business account
- **kerrykriger** - Personal account
- **savethefrogs** - Nonprofit account

When you `git push`, it needs to know WHICH account to use.

---

### One-Time Setup (Already Done!)

You already ran:

```bash
gh auth login
```

And logged into **zero2webmaster** account.

**To add other accounts later:**

```bash
# Login to kerrykriger
gh auth login
# Follow prompts, choose kerrykriger

# Login to savethefrogs
gh auth login
# Follow prompts, choose savethefrogs
```

**You only need to do this ONCE per account** - credentials are saved.

---

### Switching Accounts (Daily Use)

**Use the aliases we created:**

```bash
# Switch to zero2webmaster
gh-zero

# Switch to kerrykriger
gh-kerry

# Switch to savethefrogs
gh-frogs

# Check current account
gh-whoami
```

**What happens when you run `gh-zero`:**

```bash
kerrykriger@MacBook ~ % gh-zero
✓ Switched active account for github.com to zero2webmaster
github.com
  ✓ Logged in to github.com account zero2webmaster (keyring)
  - Active account: true
  - Git operations protocol: https
  - Token: gho_************************************
```

**Translation:** "You're now using zero2webmaster account. Any `git push` will use these credentials."

---

### Real-World Example

**Scenario:** You're working on cursor-project-templates (zero2webmaster account):

```bash
# 1. Navigate to project
cd /Users/kerrykriger/Desktop/Zero2Webmaster/AI/Templates

# 2. Switch to correct account
gh-zero

# 3. Make changes, commit
git add -A
git commit -m "Updated README"

# 4. Push to GitHub
git push origin main
```

**Scenario:** Switch to personal project (kerrykriger account):

```bash
# 1. Navigate to personal project
cd ~/Projects/my-personal-project

# 2. Switch to personal account
gh-kerry

# 3. Push changes
git push origin main
```

---

## Git Commands

### Basic Git Workflow

```bash
# 1. Check status (what changed?)
git status

# 2. Add files to staging
git add -A              # Add ALL changes
git add README.md       # Add specific file
git add *.md            # Add all markdown files

# 3. Commit changes
git commit -m "Your commit message here"

# 4. Push to GitHub
git push origin main
```

---

### Checking Your Work

```bash
# See what changed
git status

# See recent commits
git log --oneline -5

# See what files changed in last commit
git show --name-only

# See remote URL
git remote -v
```

---

### Branches

```bash
# See current branch
git branch

# Create new branch
git branch feature-name

# Switch to branch
git checkout feature-name

# Create and switch in one command
git checkout -b feature-name

# Switch back to main
git checkout main
```

---

## File Operations

### Creating Files

```bash
# Create empty file
touch filename.txt

# Create file with content
echo "Hello world" > filename.txt

# Append to file
echo "More content" >> filename.txt
```

---

### Creating Folders

```bash
# Create folder
mkdir foldername

# Create nested folders
mkdir -p path/to/nested/folder
```

---

### Copying Files

```bash
# Copy file
cp source.txt destination.txt

# Copy folder
cp -r source_folder destination_folder
```

---

### Moving/Renaming Files

```bash
# Rename file
mv oldname.txt newname.txt

# Move file to folder
mv file.txt /path/to/folder/

# Move and rename
mv old.txt /path/to/new.txt
```

---

### Deleting Files

```bash
# Delete file
rm filename.txt

# Delete folder
rm -r foldername

# Delete with confirmation
rm -i filename.txt
```

**⚠️ WARNING:** Terminal deletion is permanent (no Trash)!

---

## Common Patterns

### Running Python Scripts

```bash
# Run script
python3 script.py

# Run script with virtual environment
source venv/bin/activate
python3 script.py
deactivate
```

---

### Opening Files

```bash
# Open file in default app
open filename.txt

# Open in specific app
open -a "TextEdit" filename.txt

# Open current folder in Finder
open .

# Open URL in browser
open https://google.com
```

---

### Finding Files

```bash
# Find files by name
find . -name "*.md"

# Find files modified in last 7 days
find . -mtime -7

# Find large files (>100MB)
find . -size +100M
```

---

### Searching in Files

```bash
# Search for text in files
grep "search term" filename.txt

# Search recursively in all files
grep -r "search term" .

# Search case-insensitive
grep -i "search term" filename.txt
```

---

## Troubleshooting

### Command Not Found

**Error:**
```
zsh: command not found: gh
```

**Solution:** The program isn't installed. Install it:
```bash
brew install gh
```

---

### Permission Denied

**Error:**
```
Permission denied
```

**Solutions:**

```bash
# Make script executable
chmod +x script.sh

# Run with sudo (use carefully!)
sudo command
```

---

### Git Push Failed

**Error:**
```
remote: Repository not found.
fatal: repository 'https://github.com/...' not found
```

**Solution:** Wrong GitHub account or not logged in:

```bash
# Check current account
gh-whoami

# Switch to correct account
gh-zero   # or gh-kerry or gh-frogs

# Try push again
git push origin main
```

---

### Can't Remember Command

**Use tab completion:**

```bash
cd ~/Des[TAB]
# Autocompletes to: cd ~/Desktop
```

**Use history:**

```bash
# See recent commands
history

# Search history (type and press Ctrl+R)
# Then start typing - it finds matching commands
```

---

## Quick Reference Card

### Navigation
- `pwd` - Where am I?
- `ls` - What's here?
- `cd folder` - Go to folder
- `cd ..` - Go up one level
- `cd ~` - Go home

### GitHub Accounts
- `gh-zero` - Switch to zero2webmaster
- `gh-kerry` - Switch to kerrykriger
- `gh-frogs` - Switch to savethefrogs
- `gh-whoami` - Check current account

### Git Basics
- `git status` - What changed?
- `git add -A` - Stage all changes
- `git commit -m "message"` - Commit changes
- `git push origin main` - Push to GitHub
- `git log --oneline -5` - See recent commits

### Files
- `open .` - Open folder in Finder
- `open file.txt` - Open file
- `mkdir folder` - Create folder
- `rm file.txt` - Delete file (careful!)

### Getting Help
- `command --help` - Show command help
- `man command` - Show manual (press Q to quit)
- Google: "how to [task] in terminal mac"

---

## Copy This to Notion

**To copy this guide:**

1. Open Notion
2. Create new page: "Terminal Command Reference"
3. Copy ALL text from this file
4. Paste into Notion page
5. Notion will preserve formatting

**Or save as PDF:**

```bash
# If you have pandoc installed
pandoc TERMINAL_GUIDE.md -o TERMINAL_GUIDE.pdf
open TERMINAL_GUIDE.pdf
```

---

## Practice Exercises

### Exercise 1: Navigate and Explore

```bash
# Go to Desktop
cd ~/Desktop

# List files
ls

# Create test folder
mkdir test-folder

# Go into it
cd test-folder

# Where am I?
pwd

# Go back to Desktop
cd ..

# Delete test folder
rm -r test-folder
```

---

### Exercise 2: Git Account Switching

```bash
# Check current account
gh-whoami

# Switch to zero2webmaster
gh-zero

# Switch to kerrykriger
gh-kerry

# Switch back to zero2webmaster
gh-zero

# Verify
gh-whoami
```

---

### Exercise 3: Full Git Workflow

```bash
# Navigate to project
cd /Users/kerrykriger/Desktop/Zero2Webmaster/AI/Templates

# Check status
git status

# Make a change (create test file)
echo "Test content" > test.txt

# Check status again
git status

# Stage change
git add test.txt

# Commit
git commit -m "Test commit"

# Check log
git log --oneline -1

# Remove test file
git rm test.txt
git commit -m "Remove test file"

# Push (if you want)
# git push origin main
```

---

**Last Updated:** 2026-01-13  
**Maintained by:** Zero2Webmaster  
**Questions?** Ask in your next Cursor session!
