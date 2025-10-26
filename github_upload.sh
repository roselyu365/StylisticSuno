#!/bin/bash
# Quick script to upload SonicPalette to GitHub

echo "🚀 Preparing SonicPalette for GitHub..."
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
fi

# Add core files
echo "📁 Adding core files..."
git add README.md
git add app.py
git add gradio_ui.py
git add requirements.txt
git add .gitignore
git add LICENSE

# Add data directory
echo "📊 Adding data files..."
git add data/
git add data_loader.py
git add data_importer.py
git add expand_data.py
git add manage_data.py

# Add demo and tests
echo "🧪 Adding demos and tests..."
git add demo.py
git add test_project.py
git add test_emotion_fix.py

# Add main documentation
echo "📚 Adding documentation..."
git add START_HERE.md
git add DATA_GUIDE.md
git add GRADIO_USAGE.md
git add DEPLOYMENT.md

# Optional: Add other docs to docs/ folder
echo "📖 Organizing extra documentation..."
mkdir -p docs
mv CHANGES.md docs/ 2>/dev/null
mv DATA_EXPANSION_*.md docs/ 2>/dev/null
mv TEST_RESULTS.md docs/ 2>/dev/null
mv *_SUMMARY.md docs/ 2>/dev/null
mv QUICK_*.md docs/ 2>/dev/null
mv *_CHANGE*.md docs/ 2>/dev/null
mv SHARE_LINK*.md docs/ 2>/dev/null
mv EXTERNAL_DATA*.md docs/ 2>/dev/null
mv EMOTION_FIX*.md docs/ 2>/dev/null
mv REFERENCE_*.md docs/ 2>/dev/null
git add docs/

# Show status
echo ""
echo "✅ Files staged for commit"
echo ""
git status --short

# Commit
echo ""
echo "📝 Ready to commit!"
echo ""
echo "Run these commands:"
echo "  git commit -m 'Initial commit: SonicPalette - Suno Prompt Builder'"
echo "  git remote add origin https://github.com/YOUR_USERNAME/SonicPalette.git"
echo "  git branch -M main"
echo "  git push -u origin main"
echo ""
echo "Or run git add -A followed by git commit"

