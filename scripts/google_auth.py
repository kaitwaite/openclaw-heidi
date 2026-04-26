#!/usr/bin/env python3
"""
Google Workspace OAuth setup for Heidi (OpenClaw).
Run: python3 google_auth.py ~/Downloads/client_secret_XXXX.json
"""

import sys
import os
import json

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/documents.readonly",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets",
]

TOKEN_PATH = os.path.expanduser("~/.openclaw/workspace-heidi/google_token.json")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 google_auth.py <path-to-client-secret.json>")
        sys.exit(1)

    creds_file = sys.argv[1]

    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
    except ImportError:
        print("Missing dependencies. Run:")
        print("  pip3 install --user google-auth-oauthlib google-auth-httplib2 google-api-python-client")
        sys.exit(1)

    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_PATH, "w") as f:
            f.write(creds.to_json())
        print(f"\n✅ Auth complete! Token saved to:\n   {TOKEN_PATH}")
    else:
        print("✅ Already authenticated and token is valid.")

if __name__ == "__main__":
    main()
