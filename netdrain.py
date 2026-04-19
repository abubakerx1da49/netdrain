#!/usr/bin/env python3
import asyncio
import os
import re
import argparse
import sys
from datetime import datetime
from typing import Set, List
from urllib.parse import urljoin, urlparse

import httpx
from bs4 import BeautifulSoup
from textual import on, work
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal, VerticalScroll
from textual.widgets import (
    Input,
    Label,
    Static,
    ProgressBar,
    Footer,
    Header,
)
from textual.suggester import SuggestFromList
from textual.binding import Binding

VERSION = "1.2.1"

CSS = """
Screen {
    background: transparent;
}

#chat-area {
    height: 1fr;
    padding: 1 2;
}

#input-area {
    height: auto;
    padding: 1 1 0 1;
    border-top: solid #30363d;
}

Input {
    background: transparent;
    border: none;
    color: #f0f6fc;
}

#progress-bar {
    width: 100%;
    height: 1;
    margin: 1 2;
    background: transparent;
    display: none;
}

#progress-bar.active {
    display: block;
}

.user-text { color: #58a6ff; }
.bot-text { color: #c9d1d9; }
.status-text { color: #8b949e; text-style: italic; }
.file-text { color: #3fb950; }
.cmd-text { color: #d2a8ff; text-style: bold; }
"""

class NetDrain(App):
    CSS = CSS
    
    BINDINGS = [
        Binding("ctrl+q", "quit", "Quit", show=True),
        Binding("ctrl+l", "clear_chat", "Clear", show=True),
        Binding("ctrl+h", "show_help", "Help", show=True),
    ]
    
    def __init__(self, initial_url: str = None):
        super().__init__()
        self.initial_url = initial_url
        self.commands = ["/help", "/version", "/about", "/clear", "/quit"]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Vertical():
            yield VerticalScroll(id="chat-area")
            yield ProgressBar(id="progress-bar", show_percentage=True)
            with Horizontal(id="input-area"):
                yield Label("Domain > ", id="prompt")
                yield Input(
                    placeholder="Enter URL or / for commands...", 
                    id="url-input",
                    suggester=SuggestFromList(self.commands)
                )
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#url-input").focus()
        self.chat_append(f"0x8h | NetDrain v{VERSION}", "bot-text")
        self.chat_append("Type a URL to scrape files, or '/' for commands.", "status-text")
        self.chat_append("Shortcuts: Ctrl+Q: Quit | Ctrl+L: Clear | Ctrl+H: Help", "status-text")
        
        if self.initial_url:
            self.handle_submission(self.initial_url)

    def action_clear_chat(self) -> None:
        self.handle_command("/clear")

    def action_show_help(self) -> None:
        self.handle_command("/help")

    def chat_append(self, text: str, classes: str = ""):
        chat = self.query_one("#chat-area")
        chat.mount(Static(text, classes=classes))
        self.call_after_refresh(chat.scroll_end)

    @on(Input.Submitted, "#url-input")
    def on_input_submitted(self, event: Input.Submitted) -> None:
        value = event.value.strip()
        if not value: return
        self.handle_submission(value)

    def handle_submission(self, value: str):
        input_widget = self.query_one("#url-input")
        input_widget.value = ""

        if value.startswith("/"):
            self.handle_command(value)
        else:
            self.chat_append(f"You: {value}", "user-text")
            self.scrape_domain(value)

    def handle_command(self, cmd: str):
        cmd = cmd.lower()
        if cmd == "/help":
            self.chat_append("--- Available Commands ---", "cmd-text")
            self.chat_append("/help    - Show this help message")
            self.chat_append("/version - Show current version")
            self.chat_append("/about   - About NetDrain")
            self.chat_append("/clear   - Clear the screen")
            self.chat_append("/quit    - Exit the application")
        elif cmd == "/version":
            self.chat_append(f"NetDrain Version: {VERSION}", "cmd-text")
        elif cmd == "/about":
            self.chat_append("NetDrain is a minimalist terminal scraper designed by 0x1da49.com as an 0x8h TUI.", "bot-text")
            self.chat_append("Efficient, native, and built for bulk asset collection.", "status-text")
        elif cmd == "/clear":
            chat = self.query_one("#chat-area")
            chat.query("*").remove()
        elif cmd == "/quit":
            self.exit()
        else:
            self.chat_append(f"Unknown command: {cmd}. Type /help for list.", "status-text")

    @work(exclusive=True)
    async def scrape_domain(self, base_url: str) -> None:
        if not base_url.startswith(("http://", "https://")): base_url = "https://" + base_url
        
        parsed_base = urlparse(base_url)
        domain = parsed_base.netloc
        
        folder_name = f"scraped_{domain.replace('.', '_')}_{datetime.now().strftime('%H%M%S')}"
        
        pb = self.query_one("#progress-bar")
        pb.add_class("active")
        
        self.chat_append(f"Analyzing {base_url}...", "status-text")
        
        try:
            async with httpx.AsyncClient(follow_redirects=True, timeout=30.0) as client:
                response = await client.get(base_url)
                if response.status_code != 200:
                    self.chat_append(f"Bot: Access failed ({response.status_code})", "bot-text")
                    return

                soup = BeautifulSoup(response.text, 'html.parser')
                links: Set[str] = set()
                
                for tag in soup.find_all(['a', 'img', 'link', 'script']):
                    attr = 'href' if tag.name in ['a', 'link'] else 'src'
                    url = tag.get(attr)
                    if not url: continue
                    full_url = urljoin(base_url, url)
                    if urlparse(full_url).netloc == domain:
                        if '.' in os.path.basename(urlparse(full_url).path):
                            links.add(full_url)

                if not links:
                    self.chat_append("Bot: No local files found.", "bot-text")
                    return

                total = len(links)
                self.chat_append(f"Discovered {total} files. Starting batch download...", "status-text")
                os.makedirs(folder_name, exist_ok=True)
                
                pb.update(total=total, progress=0)
                
                count = 0
                for link in links:
                    try:
                        filename = os.path.basename(urlparse(link).path)
                        if not filename: continue
                        res = await client.get(link)
                        if res.status_code == 200:
                            with open(os.path.join(folder_name, filename), "wb") as f:
                                f.write(res.content)
                            count += 1
                        pb.advance(1)
                    except Exception:
                        continue
                
                self.chat_append(f"Done. {count}/{total} files synced to '{folder_name}'", "bot-text")
                
        except Exception as e:
            self.chat_append(f"Bot: Error - {str(e)}", "bot-text")
        finally:
            await asyncio.sleep(1)
            pb.remove_class("active")

def main():
    parser = argparse.ArgumentParser(description="NetDrain - Minimalist Domain File Scraper")
    parser.add_argument("url", nargs="?", help="Initial URL to scrape")
    parser.add_argument("-v", "--version", action="store_true", help="Show version and exit")
    
    args = parser.parse_args()
    
    if args.version:
        print(f"NetDrain v{VERSION}")
        sys.exit(0)
        
    app = NetDrain(initial_url=args.url)
    app.run()

if __name__ == "__main__":
    main()
