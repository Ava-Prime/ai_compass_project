#!/bin/bash

echo "🧼 Cleaning up old processes..."
pkill -f uvicorn
pkill -f ngrok
sleep 1

echo "🚀 Launching GPT Runtime API..."
uvicorn src.gpt_runtime:app --host 0.0.0.0 --port 8000 --reload > logs/api.log 2>&1 &

sleep 2
echo "🌐 Starting ngrok tunnel..."
ngrok http 8000 > /dev/null &
sleep 5

NGROK_URL=$(curl -s http://127.0.0.1:4040/api/tunnels | \
    grep -o 'https://[a-z0-9.-]*ngrok-free.app' | head -n 1)

if [[ -z "$NGROK_URL" ]]; then
  echo "❌ Failed to fetch ngrok URL. Aborting."
  exit 1
fi

echo "🔗 Ngrok URL: $NGROK_URL"

# Update and export .env
WEBHOOK_URL="${NGROK_URL}/notion_webhook"
sed -i "s|^WEBHOOK_CALLBACK_URL=.*|WEBHOOK_CALLBACK_URL=${WEBHOOK_URL}|" .env
export $(grep -v '^#' .env | xargs)

echo "📡 Webhook callback URL set to: $WEBHOOK_CALLBACK_URL"
echo "📬 Registering Notion webhook..."

python3 src/register_webhook.py

echo "📖 Starting Coordinator..."
python3 src/coordinator.py

