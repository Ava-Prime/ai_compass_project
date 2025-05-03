#!/bin/bash

# Step 1: Fix requirements.txt by removing duplicate/conflicting requests lines
echo "📦 Cleaning up requirements.txt..."

awk '!seen[$0]++' requirements.txt | grep -vE '^requests==2\.31\.0$' > fixed_requirements.txt
mv fixed_requirements.txt requirements.txt

# Step 2: Git commit and push
echo "📤 Committing and pushing changes..."
git add requirements.txt
git commit -m "🚑 Fix: Resolve requests version conflict in requirements.txt"
git push

echo "🚀 Done! Please trigger a redeploy from the Render dashboard if it doesn't auto-deploy."

