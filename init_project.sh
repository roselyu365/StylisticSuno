#!/usr/bin/env bash
set -e

PROJECT_NAME="${1:-SonicPalette}"

echo "==> Creating project: ${PROJECT_NAME}"
mkdir -p "${PROJECT_NAME}"
cd "${PROJECT_NAME}"

# 1) Create virtual environment
echo "==> Creating virtual environment (.venv)"
python3 -m venv .venv

# 2) Activate venv for current script session
# Note: This only affects this script; you still need to 'source .venv/bin/activate' later in your shell if needed
source .venv/bin/activate

# 3) Create basic files
echo "==> Writing .gitignore"
cat > .gitignore << 'EOF'
# Virtual env
.venv/
# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd
# macOS
.DS_Store
# Editors
.vscode/
.idea/
# Logs
*.log
# Env files
.env
EOF

echo "==> Writing README.md"
cat > README.md << EOF
# ${PROJECT_NAME}

A minimal, zero-dependency terminal MVP to transform free-form music descriptions into structured prompts for Suno (styles, emotions, BPM, instruments, chords, references).

## Quick Start
- Python 3.9+
- Create venv and run:

\`python3 -m venv .venv\`  
\`source .venv/bin/activate\`  
\`python app.py\`

## Project Structure (suggested)
- app.py
- data/ (future styles/references JSON/CSV)
- tests/

## Notes
- No third-party dependencies for now.
- Use venv to keep the environment isolated.
- MIT license recommended.

EOF

# 4) Create a simple app.py stub if not exists
if [ ! -f "app.py" ]; then
  echo "==> Writing app.py stub"
  cat > app.py << 'EOF'
#!/usr/bin/env python3

def main():
    print("SonicPalette MVP is ready. Put your existing app.py logic here.")
    desc = input("请输入你的音乐描述：").strip()
    if not desc:
        print("未输入描述，程序结束。")
        return
    print(f"收到描述：{desc}")
    print("后续会输出风格、情绪、BPM、乐器、和弦与 Suno prompt。")

if __name__ == "__main__":
    main()
EOF
fi

# 5) Initialize git repo
echo "==> Initializing git repository"
git init -b main >/dev/null 2>&1 || git init >/dev/null 2>&1
git add .
git commit -m "chore: bootstrap ${PROJECT_NAME} with venv, .gitignore, README, and app.py stub" >/dev/null 2>&1 || true

echo "==> Done."

echo
echo "Next steps:"
echo "  1) Activate venv: source .venv/bin/activate"
echo "  2) Run app:       python app.py"
echo "  3) Create remote: git remote add origin <your_repo_url> && git push -u origin main"
