# 0x8h | NetDrain 🕸️

**NetDrain** is a minimalist, professional-grade terminal asset scraper designed for the **0x8h TUI** ecosystem by [0x1da49.com](https://0x1da49.com). It enables high-speed discovery and bulk collection of local files (images, scripts, documents) from any given domain through a native terminal interface.

![Version](https://img.shields.io/badge/version-1.2.1-blue?style=flat-square)
![Build](https://img.shields.io/badge/build-native-58a6ff?style=flat-square)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey?style=flat-square)

---

## 🚀 Installation & Setup

### 🐧 Linux & 🍎 macOS (Recommended)
The fastest way to install NetDrain is via the **Cloud One-Liner**. This script automatically detects **pipx** for a professional installation or falls back to a standalone environment.

```bash
curl -sSL https://raw.githubusercontent.com/abubakerx1da49/netdrain/main/install.sh | bash
```

### 🪟 Windows
1.  **Install Python**: Ensure [Python 3.8+](https://www.python.org/downloads/) is installed.
2.  **Clone the Repo**:
    ```powershell
    git clone https://github.com/abubakerx1da49/netdrain.git
    cd netdrain
    ```
3.  **Setup Environment**:
    ```powershell
    python -m venv env
    .\env\Scripts\activate
    pip install -r requirements.txt
    ```
4.  **Run**:
    ```powershell
    python netdrain.py
    ```

---

## ✨ Advanced Features

| Feature | Description |
| :--- | :--- |
| **Domain-Safe Logic** | Automatically filters and fetches only local assets belonging to the target domain to prevent external data leaks. |
| **Interactive TUI** | Powered by `Textual`, offering a responsive, full-screen native experience. |
| **Command System** | Built-in chat-style console with autocomplete. Type `/` for a full command suite. |
| **Batch Downloading** | High-concurrency downloading with a real-time progress bar. |
| **CLI Arguments** | Pass a URL directly as an argument for automated scraping tasks. |
| **Native Aesthetic** | Designed to blend perfectly with your terminal theme using zero-background rendering. |

---

## 🛠️ Usage Guide

### Launching the Tool
Once installed (Linux/macOS), simply type:
```bash
netdrain
```

### Direct Scraping
To skip the welcome screen and start scraping a domain immediately:
```bash
netdrain https://example.com/images/
```

### In-App Commands
Type these into the prompt:
- `/help` - View interactive manual
- `/version` - Show build version
- `/about` - 0x1da49 branding & mission
- `/clear` - Wipe history and refresh terminal
- `/quit` - Exit NetDrain

### Keyboard Shortcuts
| Key | Action |
| :--- | :--- |
| **Ctrl + Q** | Force Quit |
| **Ctrl + L** | Clear Log |
| **Ctrl + H** | Quick Help |

---

## 🗑️ Uninstallation

### Linux & macOS
To completely remove NetDrain and its environment from your system:
```bash
# Remove the command link
rm ~/.local/bin/netdrain

# Remove the application data & environment
rm -rf ~/.0x8h-apps/netdrain
```

### Windows
Essentially, you just need to delete the `netdrain` folder where you cloned it.

---

## 📄 License & Credits
Built for the **0x8h TUI Suite**.
Developed and Maintained by [0x1da49.com](https://0x1da49.com).

*Empowering terminal-first workflows.*
