from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime

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
    timestamp: str

class PromptRequest(BaseModel):
    agent_name: str
    prompt: str
    priority: int

# Endpoints
@app.post("/call_agent")
def call_agent(request: AgentRequest):
    # Simulated response
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


