# Symlink Safety — Paste-Ready Prompts

## Prompt for WordPress Plugin Projects (z2w-eventleap, z2w-testimonials, etc.)

Copy and paste this into the Cursor chat for each WordPress plugin project:

---

**CRITICAL SAFETY TASK: Install symlink deletion protection.**

On 2026-02-27 the z2w-admin-suite workspace was destroyed for the second time because WordPress's `delete_plugins()` followed a symlink and recursively deleted the entire development workspace — source code, .git/ history, .specstory/, everything.

We've implemented a technical fix. You need to install it in this project. Read the full guide at:
`/Users/kerrykriger/Desktop/Zero2Webmaster/AI/Templates/Resources/SYMLINK-SAFETY-GUIDE.md`

Then do the following:

1. **Check if this project is symlinked into any Local Sites.** Look for symlinks pointing to this workspace in `/Users/kerrykriger/Local Sites/*/app/public/wp-content/plugins/`. Report what you find.

2. **For each Local Site that has a symlink to this project**, check if `wp-content/mu-plugins/symlink-deletion-guard.php` exists. If not, create the `mu-plugins/` directory and copy the mu-plugin from the guide.

3. **Add `tools/protect-git.sh`** to this project (copy the script from the guide), make it executable, and run `./tools/protect-git.sh install` to set up the auto-push hook.

4. **Update `.cursorrules`** to add a "Symlink Safety" section documenting:
   - The danger (WordPress delete_plugins follows symlinks)
   - The active safeguards (mu-plugin, auto-push hook)
   - Which Local Site(s) this plugin is symlinked into
   - Safe removal instructions (deactivate only, rm the symlink via terminal)

5. **Run `./tools/protect-git.sh status`** and show me the output to confirm everything is active.

6. **Commit and push** these changes.

---

## Prompt for the Templates Project

Copy and paste this into the Cursor chat for `/Users/kerrykriger/Desktop/Zero2Webmaster/AI/Templates`:

---

**TASK: Update AGENTS template and project setup script for symlink safety.**

On 2026-02-27 the z2w-admin-suite workspace was destroyed for the second time by WordPress's `delete_plugins()` following a symlink. Written warnings weren't enough — we've now implemented technical safeguards. The full guide is at:
`/Users/kerrykriger/Desktop/Zero2Webmaster/AI/Templates/Resources/SYMLINK-SAFETY-GUIDE.md`

Please make these updates:

1. **Update `AGENTS_v2.12.0.md`** (or create v2.13.0 per your versioning rules):
   - In the "Symlink Safety (Plugin Development)" section, add the technical safeguards:
     - mu-plugin (`symlink-deletion-guard.php`) that blocks deletion of symlinked plugins
     - Auto-push git hook (`tools/protect-git.sh`) that pushes after every commit
     - Reference `Resources/SYMLINK-SAFETY-GUIDE.md` for full details and the mu-plugin code
   - Update the incident history: the problem occurred TWICE (2026-02-16 and 2026-02-27) despite written warnings, proving technical safeguards are required
   - In the File Deletion Policy cross-reference, note that the mu-plugin now provides automated protection

2. **Update `Resources/copy_to_new_project.sh`**:
   - It currently references `AGENTS_v2.11.0.md` — update to the current version
   - Add a step that copies `tools/protect-git.sh` to new projects
   - Add a post-setup message reminding the user to install the mu-plugin if the project will be symlinked into a Local Site

3. **Update `Resources/FRAMEWORK_HISTORY_NOTION.md`**:
   - Update entry #22 to note the second incident and the technical fix
   - Or add a new entry if your versioning approach prefers it

4. **Verify** that `Resources/SYMLINK-SAFETY-GUIDE.md` exists (I've already created it). Read it and confirm it's complete and accurate.

---
