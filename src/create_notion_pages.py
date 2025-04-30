import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path='../setup/.env')

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
PARENT_PAGE_ID = os.getenv("NOTION_PARENT_PAGE_ID")

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def create_page(title):
    url = "https://api.notion.com/v1/pages"
    payload = {
        "parent": { "page_id": PARENT_PAGE_ID },
        "properties": {
            "title": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            }
        }
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to create page: {response.text}")
        return None

def main():
    page_titles = [
        "Master Project Overview",
        "Project Timeline & Milestones",
        "AI Team Directory",
        "Running Project Journal",
        "Local Machine Setup & DevOps Logs",
        "Knowledge Bases",
        "Issues, Feedback & Improvements",
        "Future Expansion Roadmap"
    ]

    db_index = {}

    for title in page_titles:
        page = create_page(title)
        if page:
            db_index[title.replace(" ", "_")] = page["id"]

    # Save the database index
    with open('../notion_db_index.json', 'w') as f:
        json.dump(db_index, f, indent=4)

if __name__ == "__main__":
    main()

