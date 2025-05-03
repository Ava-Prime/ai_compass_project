from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime, timezone
from src.memory_store import (
    log_event,
    queue_prompt,
    fetch_memory,
    fetch_prompt_queue,
    clear_prompt_queue
)

app = FastAPI(
    title="GPT Runtime API",
    version="0.1.0",
    openapi_version="3.1.0",
    servers=[{"url": "https://gpt-runtime.onrender.com"}]
)

# Pydantic models for validation
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

@app.post("/call_agent", summary="Call Agent")
def call_agent(req: AgentRequest):
    return {
        "status": "called",
        "agent": req.agent_name,
        "input_prompt": req.input_prompt
    }

@app.post("/log_event", summary="Log Event")
def log_event_api(req: LogEvent):
    log_event(req.source, req.message)
    return {"status": "logged", "event": req.dict()}

@app.post("/queue_prompt", summary="Queue Prompt")
def queue_prompt_api(req: PromptRequest):
    queue_prompt(req.agent_name, req.prompt, req.priority)
    return {"status": "queued", "prompt": req.dict()}

@app.get("/memory_journal", summary="Get Memory")
def get_memory():
    return fetch_memory()

@app.get("/prompt_queue", summary="Get Queue")
def get_queue():
    return fetch_prompt_queue()

@app.post("/clear_prompt_queue", summary="Clear Queue")
def clear_queue():
    clear_prompt_queue()
    return {"status": "cleared"}

@app.post("/notion_webhook", summary="Notion Webhook")
async def notion_webhook(request: Request):
    data = await request.json()
    return {"status": "received", "data": data}

@app.get("/healthz", summary="Healthcheck")
def healthcheck():
    return {"status": "ok"}

