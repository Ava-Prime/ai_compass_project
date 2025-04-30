# deploy.py
import os
import requests

RENDER_API_KEY = os.getenv("RENDER_API_KEY")
RENDER_SERVICE_ID = os.getenv("RENDER_SERVICE_ID")

def trigger_deploy():
    print("🚀 Triggering deploy on Render...")
    
    url = f"https://api.render.com/v1/services/{RENDER_SERVICE_ID}/deploys"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {RENDER_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json={})

    if response.status_code == 201:
        print("✅ Deploy triggered successfully!")
        deploy_url = response.json().get("deploy", {}).get("deployUrl", "Not provided")
        print(f"🔗 View on Render: {deploy_url}")
    else:
        print("❌ Failed to trigger deploy")
        print("Status Code:", response.status_code)
        print("Response:", response.json())

if __name__ == "__main__":
    trigger_deploy()
