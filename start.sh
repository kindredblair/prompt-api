#!/bin/bash

# Prompt API Startup Script

# Set default environment variables
export PROMPTS_FILE=${PROMPTS_FILE:-prompts.json}
export PROMPT_API_KEY=${PROMPT_API_KEY:-super-secret-key}
export PORT=${PORT:-8000}

echo "Starting Prompt API..."
echo "Port: $PORT"
echo "Prompts file: $PROMPTS_FILE"
echo "API Key: $PROMPT_API_KEY"
echo ""

# Activate virtual environment and start the server
source venv/bin/activate
python app.py
