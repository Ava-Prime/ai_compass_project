# 🧱 System Architecture Notes – Draft

---

## 🎯 MVP Goal

Enable intelligent orchestration of GPT agents, task logging, and automation via:
- Local execution (WSL + Python)
- Cloud augmentation (AWS)
- Persistent knowledge (Notion)

---

## 🧩 Planned Modules

| Module | Purpose |
|--------|---------|
| Navigator Core | Task dispatch, dependency tracking |
| Journal Logger | Logs events, outputs, reviews |
| Notion Sync | Stores prompts, plans, knowledge |
| GPT Prompter | Sends instructions to GPTs |
| AWS Orchestrator | Deploys and manages cloud functions |

---

## 📂 Folder Structure Proposal

```
src/
├── orchestrator/
├── notion_sync/
├── agents/
└── logs/
```

---

## 🔌 Integration Touchpoints

- `boto3` for AWS control
- `requests` or `openai` for GPT interaction
- `notion-client` for workspace communication

This file is to evolve **with Architect GPT's proposals**.
