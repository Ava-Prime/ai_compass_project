from src.config import NOTION_API_KEY, WEBHOOK_CALLBACK_URL
import os
import requests


headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

payload = {
    "callback_url": WEBHOOK_CALLBACK_URL,
    "event_types": ["page.updated", "database.updated"]
}

print("📡 Notion Webhook Registration:")

response = requests.post(
    "https://api.notion.com/v1/webhooks",
    headers=headers,
    json=payload
)

print(response.status_code)
try:
    print(response.json())
except Exception:
    print(response.text)

