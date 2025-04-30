import os
import json
from pathlib import Path
from notion_client import Client
from dotenv import load_dotenv

# Load environment variables from .env
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_PARENT_PAGE_ID = os.getenv("NOTION_PARENT_PAGE_ID")

print(f"Using Parent Page ID: {NOTION_PARENT_PAGE_ID}")

notion = Client(auth=NOTION_API_KEY)

# Paths
docs_path = Path(__file__).resolve().parents[1] / "docs"
index_file = Path(__file__).resolve().parents[1] / "notion_db_index.json"

# Load existing index or initialize new one
db_index = {}
if index_file.exists():
    with open(index_file, "r") as f:
        db_index = json.load(f)

def upload_markdown_to_notion(title, content, parent_id):
    response = notion.pages.create(
        parent={ "page_id": parent_id },
        properties={
            "title": [{
                "type": "text",
                "text": { "content": title }
            }]
        },
        children=[
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{
                        "type": "text",
                        "text": { "content": content[:1900] }
                    }]
                }
            }
        ]
    )
    return response["id"]

# Upload all markdown files to Notion
for folder in docs_path.iterdir():
    if folder.is_dir():
        for md_file in folder.glob("*.md"):
            title = md_file.stem.replace("_", " ")
            key = f"{folder.name}/{md_file.name}"
            if key in db_index:
                print(f"✅ Already uploaded: {key}")
                continue
            content = md_file.read_text()
            page_id = upload_markdown_to_notion(title, content, NOTION_PARENT_PAGE_ID)
            db_index[key] = page_id
            print(f"📘 Uploaded: {key}")

# Save updated index
with open(index_file, "w") as f:
    json.dump(db_index, f, indent=2)

print("✅ Sync complete. Index updated.")
