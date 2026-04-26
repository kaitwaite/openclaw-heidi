#!/usr/bin/env python3
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import datetime, os

TOKEN_PATH = os.path.expanduser("~/.openclaw/workspace-heidi/google_token.json")
SCOPES = [
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/gmail.readonly",
]

creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

# Test Calendar
cal = build("calendar", "v3", credentials=creds)
now = datetime.datetime.utcnow().isoformat() + "Z"
events = cal.events().list(calendarId="primary", timeMin=now, maxResults=5, singleEvents=True, orderBy="startTime").execute()
print("📅 Next 5 calendar events:")
for e in events.get("items", []):
    start = e["start"].get("dateTime", e["start"].get("date"))
    print(f"  - {start}: {e.get('summary','(no title)')}")

# Test Gmail
gmail = build("gmail", "v1", credentials=creds)
msgs = gmail.users().messages().list(userId="me", maxResults=3, labelIds=["INBOX"]).execute()
print(f"\n📬 Gmail connected — {msgs.get('resultSizeEstimate', 0)} messages in inbox")
