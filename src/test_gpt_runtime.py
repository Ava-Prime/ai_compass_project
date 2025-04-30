import requests
from datetime import datetime

BASE_URL = "https://gpt-runtime.onrender.com"

def call_agent():
    payload = {
        "agent_name": "Lead Developer GPT",
        "input_prompt": "Please generate a FastAPI onboarding assistant template."
    }
    response = requests.post(f"{BASE_URL}/call_agent", json=payload)
    print("Call Agent Status:", response.status_code)
    try:
        print("Call Agent Response:", response.json())
    except Exception:
        print("Call Agent Raw Text:", response.text)

def log_event():
    payload = {
        "source": "Human-Proxy GPT",
        "message": "Reviewed and approved onboarding assistant template.",
        "timestamp": datetime.utcnow().isoformat()
    }
    response = requests.post(f"{BASE_URL}/log_event", json=payload)
    print("Log Event Response:", response.status_code, response.json())

def queue_prompt():
    payload = {
        "agent_name": "Growth Catalyst GPT",
        "prompt": "Draft a growth roadmap for the AI onboarding feature.",
        "priority": 3
    }
    response = requests.post(f"{BASE_URL}/queue_prompt", json=payload)
    print("Queue Prompt Response:", response.status_code, response.json())

def fetch_memory():
    response = requests.get(f"{BASE_URL}/memory_journal")
    print("Memory Journal:", response.status_code, response.json())

def fetch_queue():
    response = requests.get(f"{BASE_URL}/prompt_queue")
    print("Prompt Queue:", response.status_code, response.json())

if __name__ == "__main__":
    print("🚀 Running GPT Runtime Tests")
    call_agent()
    log_event()
    queue_prompt()
    fetch_memory()
    fetch_queue()

