#!/bin/bash
#
# Copy Framework Templates to New Project
#
# Usage:
#   ./copy_to_new_project.sh /path/to/your/new/project [--wordpress] [--with-session-mgmt]
#
# What it does:
#   1. Copies AGENTS.md and SETUP_GUIDE.md (generic or WordPress variant)
#   2. Copies .cursorrules → .cursorrules (minimal template)
#   3. Copies cursorignore_template → .cursorignore (token cost control)
#   4. Copies tools/protect-git.sh → tools/protect-git.sh (auto-push safety hook)
#   5. Creates VERSION file with project version (1.0.0)
#   6. Optional: --wordpress copies WP plugin framework + creates plugin dirs
#   7. Optional: --with-session-mgmt copies ROADMAP/STATUS templates + handoff scripts
#

if [ -z "$1" ]; then
    echo "❌ Error: No project path provided"
    echo ""
    echo "Usage:"
    echo "  ./copy_to_new_project.sh /path/to/your/new/project [--wordpress] [--with-session-mgmt]"
    echo ""
    echo "Flags:"
    echo "  --wordpress          Use WordPress plugin framework (AGENTS_WP, SETUP_GUIDE_WP)"
    echo "  --with-session-mgmt  Copy session management templates (ROADMAP, STATUS)"
    echo ""
    echo "Examples:"
    echo "  ./copy_to_new_project.sh ~/Desktop/MyPythonProject"
    echo "  ./copy_to_new_project.sh ~/Desktop/MyPlugin --wordpress"
    echo "  ./copy_to_new_project.sh ~/Desktop/LongProject --with-session-mgmt"
    echo "  ./copy_to_new_project.sh ~/Desktop/MyPlugin --wordpress --with-session-mgmt"
    exit 1
fi

PROJECT_PATH="$1"
INCLUDE_SESSION_MGMT=false
WORDPRESS_MODE=false

# Parse flags (any order after the path)
shift
for arg in "$@"; do
    case "$arg" in
        --with-session-mgmt) INCLUDE_SESSION_MGMT=true ;;
        --wordpress)         WORDPRESS_MODE=true ;;
        *) echo "⚠️  Unknown flag: $arg" ;;
    esac
done

# Script is now in Resources/ folder, so go up one level to Templates/
TEMPLATE_DIR="$(cd "$(dirname "$0")/.." && pwd)"

# Check if project directory exists
if [ ! -d "$PROJECT_PATH" ]; then
    echo "❌ Error: Project directory does not exist: $PROJECT_PATH"
    echo "Create it first with: mkdir -p \"$PROJECT_PATH\""
    exit 1
fi

if [ "$WORDPRESS_MODE" = true ]; then
    echo "📦 Copying WordPress plugin framework templates to new project..."
else
    echo "📦 Copying framework templates to new project..."
fi
echo ""

# Copy AGENTS.md — WordPress or generic variant
if [ "$WORDPRESS_MODE" = true ]; then
    if [ -f "$TEMPLATE_DIR/AGENTS_WP_v3.1.0.md" ]; then
        cp "$TEMPLATE_DIR/AGENTS_WP_v3.1.0.md" "$PROJECT_PATH/AGENTS.md"
        echo "✅ Copied: AGENTS.md (WordPress Plugin Edition v3.1.0)"
    else
        echo "❌ Error: AGENTS_WP_v3.1.0.md not found in templates"
        exit 1
    fi
else
    if [ -f "$TEMPLATE_DIR/AGENTS_v2.13.0.md" ]; then
        cp "$TEMPLATE_DIR/AGENTS_v2.13.0.md" "$PROJECT_PATH/AGENTS.md"
        echo "✅ Copied: AGENTS.md (Framework v2.13.0)"
    else
        echo "❌ Error: AGENTS_v2.13.0.md not found in templates"
        exit 1
    fi
fi

# Copy SETUP_GUIDE.md — WordPress or generic variant
if [ "$WORDPRESS_MODE" = true ]; then
    if [ -f "$TEMPLATE_DIR/SETUP_GUIDE_WP_v3.0.0.md" ]; then
        cp "$TEMPLATE_DIR/SETUP_GUIDE_WP_v3.0.0.md" "$PROJECT_PATH/SETUP_GUIDE.md"
        echo "✅ Copied: SETUP_GUIDE.md (WordPress Plugin Edition v3.0.0)"
    else
        echo "❌ Error: SETUP_GUIDE_WP_v3.0.0.md not found in templates"
        exit 1
    fi
else
    if [ -f "$TEMPLATE_DIR/SETUP_GUIDE_v2.5.0.md" ]; then
        cp "$TEMPLATE_DIR/SETUP_GUIDE_v2.5.0.md" "$PROJECT_PATH/SETUP_GUIDE.md"
        echo "✅ Copied: SETUP_GUIDE.md (v2.5.0)"
    else
        echo "❌ Error: SETUP_GUIDE_v2.5.0.md not found in templates"
        exit 1
    fi
fi

# Copy .cursorrules (minimal template)
if [ -f "$TEMPLATE_DIR/.cursorrules" ]; then
    cp "$TEMPLATE_DIR/.cursorrules" "$PROJECT_PATH/.cursorrules"
    echo "✅ Copied: .cursorrules"
else
    echo "❌ Error: .cursorrules not found in templates"
    exit 1
fi

# Copy .cursorignore (token cost control)
if [ -f "$TEMPLATE_DIR/Resources/cursorignore_template" ]; then
    cp "$TEMPLATE_DIR/Resources/cursorignore_template" "$PROJECT_PATH/.cursorignore"
    echo "✅ Copied: .cursorignore"
else
    echo "⚠️  Warning: cursorignore_template not found - skipping .cursorignore"
fi

# Create VERSION file (single line with project version only)
echo "1.0.0" > "$PROJECT_PATH/VERSION"
echo "✅ Created: VERSION (1.0.0)"

# Copy protect-git.sh (auto-push safety hook)
if [ -f "$TEMPLATE_DIR/Resources/tools/protect-git.sh" ]; then
    mkdir -p "$PROJECT_PATH/tools"
    cp "$TEMPLATE_DIR/Resources/tools/protect-git.sh" "$PROJECT_PATH/tools/protect-git.sh"
    chmod +x "$PROJECT_PATH/tools/protect-git.sh"
    echo "✅ Copied: tools/protect-git.sh"
else
    echo "⚠️  Warning: protect-git.sh not found - skipping"
fi

# WordPress-specific: create plugin directory scaffold
if [ "$WORDPRESS_MODE" = true ]; then
    mkdir -p "$PROJECT_PATH/directives"
    echo "✅ Created: directives/ (feature SOPs)"

    mkdir -p "$PROJECT_PATH/execution"
    echo "✅ Created: execution/ (build tooling)"

    mkdir -p "$PROJECT_PATH/includes"
    echo "✅ Created: includes/ (PHP classes)"

    mkdir -p "$PROJECT_PATH/admin/css" "$PROJECT_PATH/admin/js" "$PROJECT_PATH/admin/views"
    echo "✅ Created: admin/ (admin assets + views)"

    mkdir -p "$PROJECT_PATH/public/css" "$PROJECT_PATH/public/js"
    echo "✅ Created: public/ (frontend assets)"
fi

# Optional: Copy session management templates
if [ "$INCLUDE_SESSION_MGMT" = true ]; then
    if [ -f "$TEMPLATE_DIR/Resources/roadmap_template.md" ]; then
        cp "$TEMPLATE_DIR/Resources/roadmap_template.md" "$PROJECT_PATH/ROADMAP.md"
        echo "✅ Copied: ROADMAP.md (from template)"
    fi

    if [ -f "$TEMPLATE_DIR/Resources/status_template.md" ]; then
        cp "$TEMPLATE_DIR/Resources/status_template.md" "$PROJECT_PATH/STATUS.md"
        echo "✅ Copied: STATUS.md (from template)"
    fi

    # Handoff scripts only for non-WordPress projects (Python-specific)
    if [ "$WORDPRESS_MODE" = false ]; then
        mkdir -p "$PROJECT_PATH/execution"

        if [ -f "$TEMPLATE_DIR/Resources/execution_scripts/generate_handoff.py" ]; then
            cp "$TEMPLATE_DIR/Resources/execution_scripts/generate_handoff.py" "$PROJECT_PATH/execution/"
            echo "✅ Copied: execution/generate_handoff.py"
        fi

        if [ -f "$TEMPLATE_DIR/Resources/execution_scripts/verify_handoff.py" ]; then
            cp "$TEMPLATE_DIR/Resources/execution_scripts/verify_handoff.py" "$PROJECT_PATH/execution/"
            echo "✅ Copied: execution/verify_handoff.py"
        fi

        chmod +x "$PROJECT_PATH/execution/"*.py 2>/dev/null
    fi
fi

echo ""
echo "🎉 Templates copied successfully!"
echo ""
echo "📍 Location: $PROJECT_PATH"
echo ""
echo "📋 Files Created:"

if [ "$WORDPRESS_MODE" = true ]; then
    echo "   - AGENTS.md (WordPress Plugin Edition v3.1.0)"
    echo "   - SETUP_GUIDE.md (WordPress Plugin Edition v3.0.0)"
else
    echo "   - AGENTS.md (Framework v2.13.0)"
    echo "   - SETUP_GUIDE.md (v2.5.0)"
fi

echo "   - .cursorrules (Minimal template)"
echo "   - .cursorignore (Token cost control)"
echo "   - tools/protect-git.sh (Auto-push safety hook)"
echo "   - VERSION (1.0.0)"

if [ "$WORDPRESS_MODE" = true ]; then
    echo "   - directives/ (feature SOPs)"
    echo "   - execution/ (build tooling)"
    echo "   - includes/ (PHP classes)"
    echo "   - admin/ (admin assets + views)"
    echo "   - public/ (frontend assets)"
fi

if [ "$INCLUDE_SESSION_MGMT" = true ]; then
    echo "   - ROADMAP.md (template)"
    echo "   - STATUS.md (template)"
    if [ "$WORDPRESS_MODE" = false ]; then
        echo "   - execution/generate_handoff.py"
        echo "   - execution/verify_handoff.py"
    fi
fi

echo ""
echo "🚀 Next Steps:"
echo "   1. cd \"$PROJECT_PATH\""
echo "   2. Open folder in Cursor"
echo "   3. Paste your Project Instantiation Prompt (see SETUP_GUIDE.md)"
echo "   4. AI will customize .cursorrules and create project structure"

if [ "$WORDPRESS_MODE" = true ]; then
    echo "   5. Create symlink from Local Site to workspace root"
    echo "   6. Enable WP_DEBUG on Local site"
    echo "   7. Install mu-plugin: see Resources/SYMLINK-SAFETY-GUIDE.md in the templates repo"
    echo "   8. Run: ./tools/protect-git.sh install"
elif [ "$INCLUDE_SESSION_MGMT" = true ]; then
    echo "   5. AI will customize ROADMAP.md and STATUS.md for your project"
    echo "   6. At end of sessions: python3 execution/generate_handoff.py"
fi

if [ "$WORDPRESS_MODE" = false ]; then
    echo ""
    echo "⚠️  WordPress plugin project? Use the --wordpress flag instead:"
    echo "   ./copy_to_new_project.sh \"$PROJECT_PATH\" --wordpress"
fi

echo ""
