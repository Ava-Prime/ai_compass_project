from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from datetime import datetime, timezone

app = FastAPI()

# In-memory data stores
memory_journal: List[dict] = []
prompt_queue: List[dict] = []

# Models
class AgentRequest(BaseModel):
    agent_name: str
    input_prompt: str

class LogEvent(BaseModel):
    source: str
    message: str
    timestamp: str  # ISO 8601 format with timezone

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
    memory_journal.append(event.dict())
    return {"status": "logged", "entry": event}

@app.post("/queue_prompt")
def queue_prompt(prompt: PromptRequest):
    prompt_queue.append(prompt.dict())
    return {"status": "queued", "prompt": prompt}

@app.get("/memory_journal")
def get_memory():
    return memory_journal

@app.get("/prompt_queue")
def get_prompt_queue():
    return prompt_queue

@app.post("/clear_prompt_queue")
def clear_prompt_queue():
    prompt_queue.clear()
    return {"status": "cleared", "remaining": len(prompt_queue)}

@app.post("/notion_webhook")
async def notion_webhook(request: Request):
    body = await request.json()
    print("🔔 Notion Webhook Body:", body)

    # ✅ Respond to Notion's verification challenge
    if "challenge" in body:
        return JSONResponse(content={"challenge": body["challenge"]})

    # ✅ Optionally log other webhook events
    memory_journal.append({
        "source": "Notion Webhook",
        "message": str(body),
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

    return {"status": "received"}

