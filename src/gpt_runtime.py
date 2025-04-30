from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import json
import os

app = FastAPI(title="GPT Runtime API")

# === File Paths ===
LOG_DIR = "../logs"
UNIVERSAL_DIR = "../docs/universal"
QUEUE_FILE = os.path.join(LOG_DIR, "prompt_queue.json")
JOURNAL_FILE = os.path.join(UNIVERSAL_DIR, "Master_Journal_Log.jsonl")

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(UNIVERSAL_DIR, exist_ok=True)

# === Models ===
class CallAgentRequest(BaseModel):
    agent_name: str
    input_prompt: str

class LogEventRequest(BaseModel):
    source: str
    message: str
    timestamp: str

class QueuePromptRequest(BaseModel):
    agent_name: str
    prompt: str
    priority: Optional[int] = 5

# === Routes ===

@app.post("/call_agent")
async def call_agent(req: CallAgentRequest):
    # In production, you'd make an API call to another GPT here
    log_entry = {
        "source": "runtime",
        "message": f"Routing prompt to {req.agent_name}: {req.input_prompt}",
        "timestamp": datetime.utcnow().isoformat()
    }
    append_to_journal(log_entry)
    return {"status": "queued", "agent": req.agent_name, "prompt": req.input_prompt}

@app.post("/log_event")
async def log_event(req: LogEventRequest):
    append_to_journal(req.dict())
    return {"status": "logged"}

@app.post("/queue_prompt")
async def queue_prompt(req: QueuePromptRequest):
    queue = load_json(QUEUE_FILE, default=[])
    queue.append({
        "agent_name": req.agent_name,
        "prompt": req.prompt,
        "priority": req.priority,
        "timestamp": datetime.utcnow().isoformat()
    })
    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)
    return {"status": "queued"}

@app.get("/memory_journal")
async def memory_journal():
    if not os.path.exists(JOURNAL_FILE):
        return []
    with open(JOURNAL_FILE, "r") as f:
        return [json.loads(line) for line in f.readlines()]

@app.get("/prompt_queue")
async def prompt_queue():
    return load_json(QUEUE_FILE, default=[])

# === Utilities ===
def append_to_journal(entry: dict):
    with open(JOURNAL_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

def load_json(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path, "r") as f:
        return json.load(f)


