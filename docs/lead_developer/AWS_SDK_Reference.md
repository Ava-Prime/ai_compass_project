# ☁️ AWS SDK (boto3) Reference

---

This file provides working examples of AWS service usage via the `boto3` SDK. It is intended as a starting point for Developer GPT when building cloud-integrated systems.

---

## 🔐 IAM Role Creation

```python
import boto3
import json

iam = boto3.client("iam")

assume_role_policy = {
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "Service": "lambda.amazonaws.com"
    },
    "Action": "sts:AssumeRole"
  }]
}

role = iam.create_role(
    RoleName="LambdaExecutionRole",
    AssumeRolePolicyDocument=json.dumps(assume_role_policy),
    Description="IAM role for Lambda execution"
)
```

---

## 📦 S3 File Upload

```python
import boto3

s3 = boto3.client("s3")
s3.upload_file("local_file.txt", "my-bucket", "remote_file.txt")
```

---

## 📜 CloudWatch Log Group Listing

```python
logs = boto3.client("logs")
groups = logs.describe_log_groups(limit=10)
for g in groups["logGroups"]:
    print(g["logGroupName"])
```

---

## 🔍 DynamoDB Table Creation

```python
dynamodb = boto3.client("dynamodb")

response = dynamodb.create_table(
    TableName="ProjectLogs",
    KeySchema=[
        {'AttributeName': 'id', 'KeyType': 'HASH'}
    ],
    AttributeDefinitions=[
        {'AttributeName': 'id', 'AttributeType': 'S'}
    ],
    BillingMode='PAY_PER_REQUEST'
)
```

---

## 📝 Notes

- All boto3 actions should use environment-based credential management.  
- Developer GPT should reuse session tokens when chaining service calls.  
- Logging and error handling should be added in production-ready versions.

> This document grows with each cloud interaction the system performs.
