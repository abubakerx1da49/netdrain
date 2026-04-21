# 0x8h | NetSense 🕸️

**NetSense** is a professional-grade, recursive web scraper designed to build high-quality text datasets for training AI models. It crawls domains, extracts clean text content, and organizes it into structured `.txt` files while maintaining a minimalist, high-fidelity terminal interface.

![Version](https://img.shields.io/badge/version-1.1.0-blue?style=flat-square)
![Build](https://img.shields.io/badge/build-native-58a6ff?style=flat-square)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey?style=flat-square)

---

## 🚀 Installation & Setup

### 🐧 Linux & 🍎 macOS (Recommended)
The fastest way to install NetSense is via the **Cloud One-Liner**. This script automatically detects **pipx** for a professional installation or falls back to a standalone environment.

```bash
curl -sSL https://raw.githubusercontent.com/abubakerx1da49/netsense/main/install.sh | bash
```

### 🪟 Windows
1.  **Install Python**: Ensure [Python 3.8+](https://www.python.org/downloads/) is installed.
2.  **Clone the Repo**:
    ```powershell
    git clone https://github.com/abubakerx1da49/netsense.git
    cd netsense
    ```
3.  **Setup Environment**:
    ```powershell
    python -m venv env
    .\env\Scripts\activate
    pip install -r requirements.txt
    ```
4.  **Run**:
    ```powershell
    python netsense.py
    ```

---

## ✨ Advanced Features

| Feature | Description |
| :--- | :--- |
| **Recursive Scraping** | Automatically crawls internal links to build a comprehensive text dataset of the entire domain. |
| **AI-Ready Text** | Strips code, styles, and boilerplate to extract pure, semantic text suitable for LLM fine-tuning. |
| **Live activity log** | High-fidelity scrolling log that records every HTTP request and extraction event in real-time. |
| **Control Suite** | Full support for Pausing, Resuming, and Stopping tasks mid-execution with state preservation. |
| **Native Aesthetic** | Designed to blend perfectly with your terminal theme using zero-background rendering. |
| **Dataset Organization** | Saves resources with source URL and timestamp metadata for easy training integration. |

---

## 🛠️ Usage Guide

### Launching the Tool
Once installed (Linux/macOS), simply type:
```bash
netsense
```

### Direct Crawling
To skip the welcome screen and start scraping a domain immediately:
```bash
netsense https://example.com
```

### In-App Commands
Type these into the prompt:
- `/help` - View interactive manual
- `/pause` - Temporarily suspend current task
- `/resume` - Continue a paused scraping task
- `/stop` - Immediately halt and save current progress
- `/clear` - Wipe log history
- `/quit` - Exit NetSense

### Keyboard Shortcuts
| Key | Action |
| :--- | :--- |
| **Ctrl + Q** | Force Quit |
| **Ctrl + L** | Clear Log |
| **Ctrl + P** | Pause / Resume |
| **Ctrl + S** | Emergency Stop |
| **Ctrl + H** | Quick Help |

---

## 🗑️ Uninstallation

### Linux & macOS
To completely remove NetSense and its environment from your system:
```bash
# Remove the command link
rm ~/.local/bin/netsense

# Remove the application data & environment
rm -rf ~/.0x8h-apps/netsense
```

---

## 📄 License & Credits
Built for the **0x8h TUI Suite**.
Developed and Maintained by [0x1da49.com](https://0x1da49.com).

*Empowering terminal-first workflows.*
