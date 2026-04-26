#!/usr/bin/env python3
"""
Send egg invoice email from [AGENT EMAIL]
"""
import os
import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

TOKEN_PATH = os.path.expanduser("~/.openclaw/workspace-heidi/google_token.json")

def send_invoice(to, subject, body):
    creds = Credentials.from_authorized_user_file(TOKEN_PATH)
    gmail = build("gmail", "v1", credentials=creds)

    msg = MIMEText(body, "plain")
    msg["To"] = to
    msg["From"] = "Heidi <[AGENT EMAIL]>"
    msg["Subject"] = subject

    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    gmail.users().messages().send(userId="me", body={"raw": raw}).execute()
    print(f"Sent to {to}")

if __name__ == "__main__":
    send_invoice(
        to="[OWNER EMAIL]",
        subject="Egg Delivery Invoice — February & March 2026",
        body="""Hi [OWNER],

Please find below a summary of egg deliveries for February and March 2026.

Date              | Item          | Qty          | Amount
Feb 21, 2025      | Chicken eggs  | 2 dozen      | $8.00
Feb 21, 2025      | Duck eggs     | 1 half dozen | $4.00
Mar 28, 2025      | Chicken eggs  | 3 dozen      | $12.00
Mar 28, 2025      | Duck eggs     | 2 half dozen | $8.00
                                    Total:          $32.00

Please apply this amount as a credit to [OWNER]'s account. Thank you!

Best,
Heidi
Assistant to [OWNER]"""
    )
