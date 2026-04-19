#!/bin/bash

# 0x8h | NetDrain - Cloud Installer
# This script installs NetDrain directly from the cloud.

# --- CONFIGURATION (Update these after creating your repo) ---
REPO_URL="https://raw.githubusercontent.com/abubakerx1da49/netdrain/main"
INSTALL_DIR="$HOME/.0x8h-apps/netdrain"
BIN_DIR="$HOME/.local/bin"

echo "🕸️  0x8h | NetDrain - Starting Cloud Installation..."

# 1. Create directory structure
mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"

# 2. Download the main script
echo "📥  Downloading NetDrain..."
curl -sSL "$REPO_URL/netdrain.py" -o "$INSTALL_DIR/netdrain.py"
chmod +x "$INSTALL_DIR/netdrain.py"

# 3. Setup Virtual Environment
echo "🐍  Setting up Python environment..."
python3 -m venv "$INSTALL_DIR/env"
"$INSTALL_DIR/env/bin/python3" -m pip install --upgrade pip > /dev/null

# 4. Install Dependencies
echo "📦  Installing dependencies (httpx, beautifulsoup4, textual)..."
"$INSTALL_DIR/env/bin/python3" -m pip install httpx beautifulsoup4 textual > /dev/null

# 5. Create System Command Wrapper
echo "🔗  Linking command to system..."
cat > "$BIN_DIR/netdrain" <<EOF
#!/bin/bash
"$INSTALL_DIR/env/bin/python3" "$INSTALL_DIR/netdrain.py" "\$@"
EOF
chmod +x "$BIN_DIR/netdrain"

echo "----------------------------------------------------"
echo "✅  Success! NetDrain is now installed."
echo "🚀  Type 'netdrain' to start."
echo "----------------------------------------------------"
