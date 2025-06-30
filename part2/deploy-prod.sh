#!/bin/bash

# Configuration
IMAGE_NAME="ai-agent-prod"
PORT=8000

# Build with production settings
docker build -t $IMAGE_NAME .

# Run with resource limits
docker run -d \
  --name $IMAGE_NAME \
  --restart unless-stopped \
  -p $PORT:$PORT \
  -e PORT=$PORT \
  -e WORKERS=4 \
  -e TIMEOUT=60 \
  -e MAX_REQUESTS=1000 \
  -e OPENAI_API_KEY="$OPENAI_API_KEY" \
  -e WEATHER_API_KEY="$WEATHER_API_KEY" \
  --memory="512m" \
  --cpus="1" \
  $IMAGE_NAME

echo "✅ Production deployment complete"
echo "📡 Access: http://$(curl -s ifconfig.me):$PORT/docs"