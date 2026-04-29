#!/usr/bin/env python3
"""Refresh Google OAuth token using refresh_token."""
import json, urllib.request, urllib.parse, os, datetime

TOKEN_PATH = os.path.expanduser("~/.openclaw/workspace-heidi/google_token.json")

with open(TOKEN_PATH) as f:
    token_data = json.load(f)

payload = urllib.parse.urlencode({
    "client_id": token_data["client_id"],
    "client_secret": token_data["client_secret"],
    "refresh_token": token_data["refresh_token"],
    "grant_type": "refresh_token",
}).encode()

req = urllib.request.Request(
    "https://oauth2.googleapis.com/token",
    data=payload,
    headers={"Content-Type": "application/x-www-form-urlencoded"}
)
resp = urllib.request.urlopen(req)
new_token = json.loads(resp.read())
print(json.dumps(new_token, indent=2))

# Update token file
token_data["token"] = new_token["access_token"]
token_data["expiry"] = (datetime.datetime.utcnow() + datetime.timedelta(seconds=new_token.get("expires_in", 3600))).strftime("%Y-%m-%dT%H:%M:%SZ")
with open(TOKEN_PATH, "w") as f:
    json.dump(token_data, f)
print("\nToken refreshed and saved.")
