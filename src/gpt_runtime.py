from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime, timezone
from typing import List

from src.memory_store import (
    log_event as add_memory,
    fetch_memory as get_all_memories,
    queue_prompt as add_prompt_to_queue,
    fetch_prompt_queue as get_prompt_queue,
    clear_prompt_queue
)

app = FastAPI()

# Models
class AgentRequest(BaseModel):
    agent_name: str
    input_prompt: str

class LogEvent(BaseModel):
    source: str
    message: str
    timestamp: str

class PromptRequest(BaseModel):
    agent_name: str
    prompt: str
    priority: int

# Endpoints
@app.post("/call_agent")
def call_agent(request: AgentRequest):
    response = {
        "agent": request.agent_name,
        "response": f"Simulated response for: '{request.input_prompt}'"
    }
    return response

@app.post("/log_event")
def log_event(event: LogEvent):
    add_memory(event.source, event.message, event.timestamp)
    return {"status": "logged", "entry": event}

@app.post("/queue_prompt")
def queue_prompt(prompt: PromptRequest):
    add_prompt_to_queue(prompt.agent_name, prompt.prompt, prompt.priority)
    return {"status": "queued", "prompt": prompt}

@app.get("/memory_journal")
def get_memory():
    return get_all_memories()

@app.get("/prompt_queue")
def get_queue():
    return get_prompt_queue()

@app.post("/clear_prompt_queue")
def clear_queue():
    clear_prompt_queue()
    return {"status": "cleared", "remaining": 0}

@app.post("/notion_webhook")
async def notion_webhook(request: Request):
    body = await request.json()
    print("🔔 Notion Webhook Body:", body)

    if "challenge" in body:
        return JSONResponse(content={"challenge": body["challenge"]})

    add_memory("Notion Webhook", str(body), datetime.now(timezone.utc).isoformat())
    return {"status": "received"}

