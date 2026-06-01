#!/usr/bin/env python3
"""
ZAVINO Telegram Publisher
Reads a markdown post file and sends it to the ZAVINO Telegram channel.
Supports text-only posts and posts with images (image_url in frontmatter).

Usage:
    python scripts/telegram-publish.py outputs/telegram/post.md
    python scripts/telegram-publish.py outputs/instagram/2026-05-27-post.md
"""

import sys
import os
import re
import requests
from pathlib import Path

# Fix Windows console encoding
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


# ── Config ────────────────────────────────────────────────────────────────────

def load_env():
    """Load .env file from project root."""
    env_path = Path(__file__).parent.parent / ".env"
    env = {}
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, val = line.partition("=")
                env[key.strip()] = val.strip().strip('"').strip("'")
    return env

env = load_env()
BOT_TOKEN   = env.get("TELEGRAM_BOT_TOKEN", "")
CHANNEL_ID  = env.get("TELEGRAM_CHANNEL_ID", "")  # e.g. @zavinotech or -1001234567890

CAPTION_LIMIT = 1024  # Telegram caption max characters


# ── Helpers ───────────────────────────────────────────────────────────────────

def get_image_url_from_frontmatter(raw: str) -> str:
    """Extract image_url from YAML frontmatter if present."""
    raw = raw.strip()
    if not raw.startswith("---"):
        return ""
    end = raw.find("---", 3)
    if end == -1:
        return ""
    frontmatter = raw[3:end]
    for line in frontmatter.splitlines():
        stripped = line.strip()
        if stripped.startswith("image_url:"):
            value = stripped.split(":", 1)[1].strip().strip('"').strip("'")
            return value
    return ""


def strip_frontmatter(text: str) -> str:
    """Remove YAML frontmatter (--- ... ---) from markdown."""
    text = text.strip()
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            text = text[end + 3:].strip()
    return text


def strip_section_headers(text: str) -> str:
    """Remove markdown section headers that are workspace meta (## Notes, etc.)"""
    meta_headers = ["## Notes", "## notes"]
    lines = text.splitlines()
    result = []
    skip = False
    for line in lines:
        if any(line.strip().startswith(h) for h in meta_headers):
            skip = True
        if skip and line.startswith("## ") and not any(line.strip().startswith(h) for h in meta_headers):
            skip = False
        if not skip:
            result.append(line)
    return "\n".join(result).strip()


def md_to_telegram(text: str) -> str:
    """
    Convert markdown to Telegram HTML format.
    Telegram supports: <b>, <i>, <code>, <pre>, <a href="">
    """
    # Bold: **text** → <b>text</b>
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Italic: *text* or _text_ → <i>text</i>
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', text)
    text = re.sub(r'(?<!_)_(?!_)(.+?)(?<!_)_(?!_)', r'<i>\1</i>', text)
    # Inline code: `code` → <code>code</code>
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Remove markdown headers (#, ##, ###) — keep the text
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # Remove horizontal rules
    text = re.sub(r'^---+$', '', text, flags=re.MULTILINE)
    # Clean up excessive blank lines (max 2)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def split_message(text: str, max_len: int = 4000) -> list[str]:
    """Split message into chunks ≤ max_len characters, splitting on blank lines."""
    if len(text) <= max_len:
        return [text]
    chunks = []
    current = ""
    for paragraph in text.split("\n\n"):
        candidate = (current + "\n\n" + paragraph).strip()
        if len(candidate) <= max_len:
            current = candidate
        else:
            if current:
                chunks.append(current.strip())
            current = paragraph
    if current:
        chunks.append(current.strip())
    return chunks


def send_message(text: str, preview: bool = False) -> dict:
    """Send a text message to the Telegram channel."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": not preview,
    }
    response = requests.post(url, json=payload, timeout=15)
    return response.json()


def send_photo(image_url: str, caption: str = "") -> dict:
    """Send a photo with optional caption to the Telegram channel."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    payload = {
        "chat_id": CHANNEL_ID,
        "photo": image_url,
        "parse_mode": "HTML",
    }
    if caption:
        payload["caption"] = caption
    response = requests.post(url, json=payload, timeout=15)
    return response.json()


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    # Validate config
    if not BOT_TOKEN or not CHANNEL_ID:
        print("❌ Error: TELEGRAM_BOT_TOKEN or TELEGRAM_CHANNEL_ID not set in .env")
        print("   Create a .env file in the project root with:")
        print("   TELEGRAM_BOT_TOKEN=your_token_here")
        print("   TELEGRAM_CHANNEL_ID=@yourchannel")
        sys.exit(1)

    # Validate file arg
    if len(sys.argv) < 2:
        print("Usage: python scripts/telegram-publish.py <path-to-post.md>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        sys.exit(1)

    # Read raw content
    raw = file_path.read_text(encoding="utf-8")

    # Extract image URL from frontmatter (before stripping it)
    image_url = get_image_url_from_frontmatter(raw)

    # Prepare text content
    text = strip_frontmatter(raw)
    text = strip_section_headers(text)
    text = md_to_telegram(text)

    if not text:
        print("❌ Post is empty after processing.")
        sys.exit(1)

    print(f"📤 Sending to {CHANNEL_ID}...")
    if image_url:
        print(f"🖼  Image: {image_url[:80]}{'...' if len(image_url) > 80 else ''}")
    print("─" * 50)
    print(text[:300] + ("..." if len(text) > 300 else ""))
    print("─" * 50)

    # ── With image ─────────────────────────────────────────────────────────────
    if image_url:
        if len(text) <= CAPTION_LIMIT:
            # Short enough → send as photo with caption
            result = send_photo(image_url, caption=text)
            if result.get("ok"):
                msg_id = result["result"]["message_id"]
                print(f"✅ Photo + caption sent — message_id: {msg_id}")
            else:
                err = result.get("description", "Unknown error")
                print(f"❌ Photo send failed: {err}")
                # Fallback: send photo without caption, then send text
                print("   Retrying: photo only, then text...")
                r1 = send_photo(image_url)
                r2 = send_message(text)
                if r1.get("ok") and r2.get("ok"):
                    print(f"✅ Fallback succeeded — photo: {r1['result']['message_id']}, text: {r2['result']['message_id']}")
                else:
                    print(f"❌ Fallback also failed. Photo: {r1.get('description')} | Text: {r2.get('description')}")
                    sys.exit(1)
        else:
            # Text too long for caption → send photo first, then text
            print(f"ℹ️  Caption too long ({len(text)} chars > {CAPTION_LIMIT}). Sending photo + separate message.")
            r1 = send_photo(image_url)
            if not r1.get("ok"):
                print(f"❌ Photo send failed: {r1.get('description', 'Unknown error')}")
                sys.exit(1)
            print(f"✅ Photo sent — message_id: {r1['result']['message_id']}")

            chunks = split_message(text)
            for i, chunk in enumerate(chunks, 1):
                r2 = send_message(chunk)
                if r2.get("ok"):
                    print(f"✅ Text part {i}/{len(chunks)} sent — message_id: {r2['result']['message_id']}")
                else:
                    print(f"❌ Text part {i} failed: {r2.get('description', 'Unknown error')}")
                    sys.exit(1)

    # ── Text only ──────────────────────────────────────────────────────────────
    else:
        chunks = split_message(text)
        total = len(chunks)
        for i, chunk in enumerate(chunks, 1):
            result = send_message(chunk)
            if result.get("ok"):
                msg_id = result["result"]["message_id"]
                print(f"✅ Part {i}/{total} sent — message_id: {msg_id}")
            else:
                err = result.get("description", "Unknown error")
                print(f"❌ Part {i}/{total} failed: {err}")
                sys.exit(1)

    print(f"\n🚀 Done — post published to {CHANNEL_ID}")


if __name__ == "__main__":
    main()
