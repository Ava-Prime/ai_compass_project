from src.config import NOTION_API_KEY, NOTION_PARENT_PAGE_ID
import os
import time
import requests
from datetime import datetime, timezone
from src.memory_store import log_event_to_db, fetch_prompt_queue, clear_prompt_queue


def post_to_notion_log(message):
    if not NOTION_API_KEY or not NOTION_PARENT_PAGE_ID:
        return
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    data = {
        "parent": {"page_id": NOTION_PARENT_PAGE_ID},
        "properties": {
            "title": {
                "title": [{"text": {"content": message}}]
            }
        }
    }
    try:
        res = requests.post(url, headers=headers, json=data)
        if res.status_code in (200, 201):
            print("📝 Logged to Notion.")
        else:
            print(f"⚠️ Notion log failed: {res.status_code} {res.text}")
    except Exception as e:
        print(f"⚠️ Notion exception: {e}")

def main():
    print("🤖 Coordinator started. Watching prompt queue...")
    while True:
        queue = fetch_prompt_queue()
        if not queue:
            time.sleep(3)
            continue

        for prompt in queue:
            agent = prompt["agent_name"]
            task = prompt["prompt"]
            print(f"💡 Processing prompt for {agent}: {task}")

            result = f"Simulated response to '{task}' by {agent}"
            timestamp = datetime.now(timezone.utc).isoformat()
            log_message = f"{agent} completed: {task}"

            log_event_to_db("Coordinator", log_message, timestamp)
            post_to_notion_log(log_message)

        clear_prompt_queue()
        print("🧹 Prompt queue cleared.\n")
        time.sleep(2)

if __name__ == "__main__":
    main()

