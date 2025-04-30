# 🏗️ MVP System Blueprint – AI Compass

---

## 📌 Purpose

This blueprint outlines the high-level architecture, integration points, and system design principles for the AI Compass platform MVP. It is a collaborative artifact — evolved and refined by Architect GPT, Developer GPT, and Human-Proxy GPT.

---

## 🌐 System Overview

**AI Compass** is a locally hosted, cloud-integrated orchestration system that connects:

- Custom GPT agents (via ChatGPT Pro)
- Local execution environment (Python/WSL)
- Notion workspace (via API)
- AWS services (Lambda, DynamoDB, S3, CloudWatch, etc.)

The system operates through structured tasks, logs, and agent collaboration.

---

## 🧱 High-Level Architecture (Initial)

[ GPT Agents ] <---> [ Navigator / Human-Proxy ] <---> [ Notion Workspace ] | V [ Local Execution Layer ] | V [ AWS Services ]

---

## 🔌 Core Integrations

| Integration | Purpose |
|-------------|---------|
| **Notion API** | Log tasks, documents, journal entries, assignments  
| **OpenAI GPT Agents** | Role-based intelligence, planning, creation  
| **Python CLI (WSL)** | Execute scripts, connect services, log locally  
| **AWS SDK (boto3)** | Deploy Lambda functions, write to DynamoDB, store in S3  
| **Navigator Logic** | Activate agents, track project flow, reduce redundancy  

---

## 🛠️ Modules & Scripts

| Component | Role |
|----------|------|
| `create_notion_pages.py` | Builds the agent Notion pages  
| `assign_agent_tasks.py` | Sends task prompts to each GPT  
| `notion_db_index.json` | Tracks database IDs for syncing  
| `journal_logger.py` | Writes to project log  
| `navigator_orchestrator.py` | (Future) Central agent dispatcher  

---

## 📋 Key Design Principles

- Simplicity first.  
- Modular and extensible.  
- Local-first, cloud-expandable.  
- Transparent logs, versioned documents.  
- Intelligence layered atop automation.

---

## 🚧 Pending Additions

- Detailed AWS architecture (from Architect GPT)
- Scripted AWS resource deployment (via Developer GPT)
- System state diagrams
- End-to-end flow simulation

---

> This document evolves with the system.  
> Architect GPT and Developer GPT will update and expand its sections.
