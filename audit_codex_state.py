# ~/ai_compass_project/audit_codex_state.py

import os
import glob
import json
from datetime import datetime
from dotenv import load_dotenv
from notion_client import Client

# Load .env from root or src if needed
env_path = os.path.expanduser(".env")
load_dotenv(dotenv_path=env_path)

# Config vars
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_PARENT_PAGE_ID = os.getenv("NOTION_PARENT_PAGE_ID")

GPT_ROLES = [
    "human_proxy", "navigator", "chief_architect", "lead_developer",
    "business_strategist", "marketing_specialist", "customer_success",
    "growth_catalyst", "investor_relations"
]

def check_scrolls(role):
    scroll_dir = os.path.expanduser(f"./docs/{role}")
    scrolls = glob.glob(f"{scroll_dir}/*.md")
    zip_files = glob.glob(f"{scroll_dir}/*.zip")
    return len(scrolls), len(zip_files), scroll_dir

def check_universal_scrolls():
    scroll_dir = os.path.expanduser("./docs/universal")
    scrolls = glob.glob(f"{scroll_dir}/*.md")
    return len(scrolls), scroll_dir

def check_scripts():
    scripts = [
        "./src/sync_scrolls_to_notion.py",
        "./src/create_notion_pages.py",
        "./src/gpt_runtime.py",
        "./src/memory_store.py",
        "./src/create_ai_agent_pages.py"
    ]
    return [s for s in scripts if os.path.exists(s)]

def check_action_schema():
    path = "./src/gpt_runtime_openapi.yaml"
    return path if os.path.exists(path) else None

def check_notion_connection():
    try:
        notion = Client(auth=NOTION_API_KEY)
        res = notion.search(filter={"object": "page"}, page_size=1)
        return True
    except Exception:
        return False

def check_notion_db_index():
    index_path = "./notion_db_index.json"
    if os.path.exists(index_path):
        with open(index_path, "r") as f:
            dbs = json.load(f)
        return dbs
    return {}

def main():
    print("🌐 Running Codex State Auditor for AI Compass Project\n")

    print(f"🔑 Notion API Key: {'✅' if NOTION_API_KEY else '❌ MISSING'}")
    print(f"📘 Parent Page ID: {NOTION_PARENT_PAGE_ID or '❌ MISSING'}\n")

    # Scroll Reflection
    uni_count, uni_path = check_universal_scrolls()
    print(f"📚 Universal Scrolls: {uni_count} found in {uni_path}")

    total_scrolls = 0
    for role in GPT_ROLES:
        count, zip_count, path = check_scrolls(role)
        total_scrolls += count
        print(f"📂 {role:20s}: {count} .md | {zip_count} .zip in {path}")

    # Scripts
    scripts = check_scripts()
    print(f"\n⚙️ Scripts Detected: {len(scripts)}")
    for s in scripts:
        print(f"   🔹 {s}")

    # Action schema
    schema_path = check_action_schema()
    print(f"\n🧾 GPT Action Schema: {schema_path if schema_path else '❌ MISSING'}")

    # Notion
    db_index = check_notion_db_index()
    print(f"\n📒 Notion DB Index: {len(db_index)} entries loaded")
    for k, v in db_index.items():
        print(f"   🔹 {k:25s} → {v}")

    notion_ok = check_notion_connection()
    print(f"\n🔗 Notion API Test: {'✅ Connected' if notion_ok else '❌ Failed'}")

    print("\n🌸 Audit Complete 🌸")
    print(f"🕊️ Total GPT Scrolls (excluding universal): {total_scrolls}")
    print(f"⏰ Timestamp: {datetime.now().isoformat()}\n")

if __name__ == "__main__":
    main()

