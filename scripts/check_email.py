#!/usr/bin/env python3
"""Check Gmail for new emails since a given timestamp."""
import json, urllib.request, datetime, base64, sys

TOKEN_PATH = "/Users/heidi/.openclaw/workspace-heidi/google_token.json"

with open(TOKEN_PATH) as f:
    token_data = json.load(f)
access_token = token_data["token"]

HEADERS = {"Authorization": f"Bearer {access_token}"}

def api_get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    resp = urllib.request.urlopen(req)
    return json.loads(resp.read())

# After 10 AM ET today = 14:00 UTC
after_ts = int(datetime.datetime(2026, 4, 28, 14, 0, 0).timestamp())
# Use Gmail query format
query = f"after:{after_ts}"

data = api_get(f"https://gmail.googleapis.com/gmail/v1/users/me/messages?q={urllib.request.quote(query)}&maxResults=25")
messages = data.get("messages", [])
print(f"Messages since 10 AM ET: {len(messages)}")

for msg in messages:
    detail = api_get(f"https://gmail.googleapis.com/gmail/v1/users/me/messages/{msg['id']}?format=metadata&metadataHeaders=From&metadataHeaders=Subject&metadataHeaders=Date")
    headers = {h["name"]: h["value"] for h in detail.get("payload", {}).get("headers", [])}
    snippet = detail.get("snippet", "")[:120]
    print(f"\n---")
    print(f"From: {headers.get('From', '?')}")
    print(f"Subject: {headers.get('Subject', '?')}")
    print(f"Date: {headers.get('Date', '?')}")
    print(f"Snippet: {snippet}")
