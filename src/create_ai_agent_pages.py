import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path='../setup/.env')

# Notion API Setup
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Load the Notion Database Index
with open('../notion_db_index.json', 'r') as f:
    notion_db = json.load(f)

# Get the Parent Page ID for the AI Team Directory
parent_page_id = notion_db["AI_Team_Directory"]

# Define the Agents to Create (including Navigator GPT)
agents = [
    "Chief Architect GPT",
    "Lead Developer GPT",
    "Business Strategist GPT",
    "Marketing Specialist GPT",
    "Investor Relations GPT",
    "Customer Success GPT",
    "Growth Catalyst GPT",
    "Human-Proxy GPT",
    "Navigator GPT",
]

# Dictionary to store new agent page IDs
agent_ids = {}

def create_subpage(title):
    """Create a sub-page under the AI Team Directory for each agent."""
    url = "https://api.notion.com/v1/pages"
    payload = {
        "parent": { "page_id": parent_page_id },
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

    if response.status_code in [200, 201]:
        print(f"✅ Created sub-page: {title}")
        return response.json()["id"]
    else:
        print(f"❌ Failed to create sub-page {title}: {response.text}")
        return None

def main():
    """Main function to create agent subpages and update the database index."""
    for agent in agents:
        page_id = create_subpage(agent)
        if page_id:
            agent_key = agent.replace(" ", "_")
            agent_ids[agent_key] = page_id

    # Update Agents Section in notion_db_index.json
    notion_db["Agents"] = agent_ids
    with open('../notion_db_index.json', 'w') as f:
        json.dump(notion_db, f, indent=4)

    print("🎯 All AI agent sub-pages created and database index updated.")

if __name__ == "__main__":
    main()

