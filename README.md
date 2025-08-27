# Prompt API

A simple Flask-based API for serving system prompts for different personas. This API reads prompts from a JSON file and serves them via REST endpoints.

## Features

- Serve system prompts for different personas
- API key authentication (optional)
- Hot-reload prompts from JSON file
- Simple REST API endpoints

## Setup

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables (Optional)

```bash
export PROMPTS_FILE=prompts.json        # optional, defaults to prompts.json
export PROMPT_API_KEY=super-secret-key  # optional; omit to allow open access
export PORT=5000                        # optional, defaults to 5000
```

### 4. Run the API

```bash
python app.py
```

The API will be available at `http://localhost:8000` (or the port specified in the PORT environment variable)

## API Endpoints

### Get a specific persona prompt

```
GET /prompts/{persona}
```

**Headers (if API key is set):**
```
X-API-Key: your-api-key
```

**Example:**
```bash
curl http://localhost:8000/prompts/ellie -H "X-API-Key: super-secret-key"
```

**Response:**
```json
{
  "ellie": "You are Ellie, the user's personal Accountability Coach in the MedChefs app..."
}
```

### List all prompts

```
GET /prompts
```

**Headers (if API key is set):**
```
X-API-Key: your-api-key
```

**Example:**
```bash
curl http://localhost:8000/prompts -H "X-API-Key: super-secret-key"
```

**Response:**
```json
{
  "ellie": "You are Ellie, the user's personal Accountability Coach in the MedChefs app...",
  "nick": "You are Nick, the user's personal Accountability Coach in the MedChefs app..."
}
```

## Managing Prompts

Edit the `prompts.json` file to add, modify, or remove personas. The API will pick up changes immediately on the next request.

**Example prompts.json:**
```json
{
  "ellie": "You are Ellie, the user's personal Accountability Coach in the MedChefs app. Speak casually and compassionately, using phrases like 'Umm…' or 'Honestly…'. Keep responses short and simple (one or two sentences) and focus on being supportive. Avoid technical jargon, and write numbers the way you would say them.",
  "nick": "You are Nick, the user's personal Accountability Coach in the MedChefs app. Blend empathetic support with humor. Use casual language with filler phrases like 'Well…', 'I mean…', and 'Not to be dramatic but…'. Keep responses short and real, like a voice conversation. Lighten the mood when appropriate and avoid jargon; keep explanations high-level."
}
```

## Deployment

This Flask app can be deployed to various platforms:

- **Render**: Set environment variables in the dashboard
- **Railway**: Configure environment variables in the project settings
- **Heroku**: Use `heroku config:set` to set environment variables
- **AWS Elastic Beanstalk**: Configure environment variables in the EB console

Make sure to set the same environment variables on your hosting platform:
- `PROMPTS_FILE` (optional)
- `PROMPT_API_KEY` (optional)
- `PORT` (optional)

## Testing

Run the included test script to verify all endpoints work correctly:

```bash
python test_api.py
```

This will test:
- Getting specific persona prompts
- Listing all prompts
- Unauthorized access handling
- Non-existent persona handling

## Error Responses

- `401 Unauthorized`: Invalid or missing API key
- `404 Not Found`: Persona not found in prompts file
