import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RENDER_API_KEY")
SERVICE_ID = os.getenv("RENDER_SERVICE_ID")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

url = f"https://api.render.com/v1/services/{SERVICE_ID}/deploys"
payload = {"clearCache": False}

print("🚀 Triggering deploy on Render...")

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 201:
    data = response.json()
    deploy_id = data.get("deploy", {}).get("id")
    view_url = f"https://dashboard.render.com/web/srv-{SERVICE_ID}/deploys/{deploy_id}" if deploy_id else "Check Render dashboard manually"
    print("✅ Deploy triggered successfully!")
    print(f"🔗 View on Render: {view_url}")
else:
    print("❌ Failed to trigger deploy")
    print("Status Code:", response.status_code)
    print("Response:", response.json())

