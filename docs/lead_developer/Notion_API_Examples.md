# 🗂️ Notion API – Developer Examples

---

This document offers code patterns for using the Notion API to read, write, and update workspace data programmatically. Developer GPT and collaborators should reference and expand this file as the system evolves.

---

## 🔐 Authentication

Ensure you’ve created an internal integration in Notion, and shared the relevant pages or databases with the integration.

```env
NOTION_API_KEY=your_secret_key
```

Use it in Python via environment variables and the official Notion SDK:

```python
from notion_client import Client
import os

notion = Client(auth=os.getenv("NOTION_API_KEY"))
```

---

## 📄 Create a New Page in a Database

```python
new_page = notion.pages.create({
    "parent": { "database_id": "DATABASE_ID_HERE" },
    "properties": {
        "Name": {
            "title": [{
                "text": { "content": "Agent Log Entry" }
            }]
        },
        "Status": {
            "select": { "name": "In Progress" }
        }
    }
})
```

---

## 📝 Update Page Properties

```python
notion.pages.update(
    page_id="PAGE_ID_HERE",
    properties={
        "Status": {
            "select": { "name": "Complete" }
        }
    }
)
```

---

## 📊 Query Database Entries

```python
query = notion.databases.query(database_id="DATABASE_ID_HERE")
for result in query["results"]:
    print(result["properties"]["Name"]["title"][0]["text"]["content"])
```

---

## 🧠 Use Cases in This Project

- Post GPT-generated plans, logs, and summaries  
- Read project journal entries  
- Sync Navigator GPT’s dispatch records  
- Link back to journal metadata via page ID

---

## 📌 Notes

- Use timestamps or UUIDs to track which pages were updated by which agent  
- Use page properties (tags, status, last modified) to drive logic flow  
- Sync page state to `.json` if offline fallback is needed

> Developer GPT should continually refine this file as new workflows are built.
