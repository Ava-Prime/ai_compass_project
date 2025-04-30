# ☁️ AWS Design Patterns

---

## 🧠 Principles

- Build modular services
- Minimize server maintenance using managed services
- Secure by design (IAM first)
- Optimize for cost early

---

## 🧱 Recommended Services (MVP Phase)

| Use Case | Service |
|----------|---------|
| Stateless compute | AWS Lambda |
| Persistent storage | Amazon S3 |
| NoSQL datastore | DynamoDB |
| IAM & auth | IAM roles and policies |
| Eventing | EventBridge or Lambda triggers |
| Monitoring | CloudWatch logs, metrics |

---

## 📐 Example Patterns

### 1. API Gateway → Lambda → DynamoDB
Simple, stateless backend with fast scalability

### 2. Notion API Integration → Lambda → S3 Logging
Document updates processed and stored locally/cloud

---

## 🛠️ IaC Options

- Terraform (recommended for version control)
- AWS CloudFormation (native, tightly integrated)

> Architect GPT may select and evolve from these foundations.
