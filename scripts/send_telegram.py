#!/usr/bin/env python3
"""
ZAVINO Telegram Publisher
Usage: python3 scripts/send_telegram.py /path/to/post.txt
Token is passed via TELEGRAM_TOKEN env variable.
"""
import sys
import json
import os
import urllib.request
import urllib.error

TOKEN = os.environ.get("TELEGRAM_TOKEN", "8692413834:AAGqGYCXoiaOnShoD54pD_j-XwqZDPfk7q0")
CHAT_ID = "@zavinoai"

def send(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = json.dumps({
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    try:
        res = json.loads(urllib.request.urlopen(req).read().decode("utf-8"))
        if res.get("ok"):
            print("SENT ok message_id:", res["result"]["message_id"])
            return True
        else:
            print("TELEGRAM ERROR:", res)
            return False
    except urllib.error.HTTPError as e:
        print("HTTP ERROR:", e.code, e.read().decode("utf-8"))
        return False
    except Exception as e:
        print("ERROR:", repr(e))
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 send_telegram.py <post_file.txt>")
        sys.exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        text = f.read().strip()
    ok = send(text)
    sys.exit(0 if ok else 1)
