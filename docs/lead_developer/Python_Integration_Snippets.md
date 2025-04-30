# 🐍 Python Integration Snippets

---

This file provides a collection of reusable Python code snippets for integrating core systems used by the AI Compass project, including Notion, AWS (via boto3), and OpenAI GPTs.

It serves as a living reference for Developer GPT and human collaborators.

---

## 🧠 Environment Setup

Ensure the following Python packages are installed in your virtual environment:

```bash
pip install requests openai boto3 python-dotenv notion-client
```

Also, load credentials using `.env`:

```ini
OPENAI_API_KEY=your_openai_key
NOTION_API_KEY=your_notion_key
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
```

---

## 🗂️ Notion API: Basic Page Creation

```python
from notion_client import Client
import os

notion = Client(auth=os.getenv("NOTION_API_KEY"))

page = notion.pages.create({
    "parent": { "database_id": "YOUR_DB_ID" },
    "properties": {
        "Name": {
            "title": [{
                "text": {
                    "content": "New Page Title"
                }
            }]
        }
    }
})
```

---

## ☁️ AWS Lambda Deployment (boto3)

```python
import boto3

lambda_client = boto3.client("lambda")

with open("function.zip", "rb") as f:
    zipped_code = f.read()

response = lambda_client.create_function(
    FunctionName="MyFunction",
    Runtime="python3.12",
    Role="arn:aws:iam::123456789012:role/lambda-execution-role",
    Handler="lambda_function.lambda_handler",
    Code={"ZipFile": zipped_code},
)
```

---

## 🧠 OpenAI Chat Completion (GPT-4)

```python
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a webhook for Notion API integration."}
    ]
)

print(response.choices[0].message["content"])
```

---

## 📝 Notes

- Always sanitize user input and validate API responses.
- Log actions and exceptions to support transparency and debugging.
- Developer GPT should expand this file as new modules are added to the system.
