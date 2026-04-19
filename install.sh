#!/bin/bash

# 0x8h | NetDrain - Pro Cloud Installer
# This script installs NetDrain using pipx (preferred) or venv (fallback).

REPO_URL="https://raw.githubusercontent.com/abubakerx1da49/netdrain/main"
GIT_REPO="https://github.com/abubakerx1da49/netdrain.git"
INSTALL_DIR="$HOME/.0x8h-apps/netdrain"
BIN_DIR="$HOME/.local/bin"

echo "🕸️  0x8h | NetDrain - Starting Installation..."

# --- METHOD 1: pipx (Professional Standard) ---
if command -v pipx &> /dev/null; then
    echo "💎  Found pipx! Installing natively..."
    pipx install "git+$GIT_REPO" --force
    echo "----------------------------------------------------"
    echo "✅  Success! NetDrain installed via pipx."
    echo "🚀  Type 'netdrain' to start."
    exit 0
fi

# --- METHOD 2: VENV (Reliable Fallback) ---
echo "📦  pipx not found. Using isolated environment method..."

mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"

echo "📥  Downloading code..."
curl -sSL "$REPO_URL/netdrain.py" -o "$INSTALL_DIR/netdrain.py"
chmod +x "$INSTALL_DIR/netdrain.py"

echo "🐍  Configuring environment..."
python3 -m venv "$INSTALL_DIR/env"
"$INSTALL_DIR/env/bin/python3" -m pip install httpx beautifulsoup4 textual > /dev/null

echo "🔗  Linking command..."
cat > "$BIN_DIR/netdrain" <<EOF
#!/bin/bash
"$INSTALL_DIR/env/bin/python3" "$INSTALL_DIR/netdrain.py" "\$@"
EOF
chmod +x "$BIN_DIR/netdrain"

echo "----------------------------------------------------"
echo "✅  Success! NetDrain is now installed (Fallback mode)."
echo "🚀  Type 'netdrain' to start."
echo "💡  Pro Tip: Install 'pipx' for better CLI management."
echo "----------------------------------------------------"
