# Deployment Guide

This guide will help you deploy your Prompt API to various platforms.

## Option 1: Render (Recommended - Easiest)

### Step 1: Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon in the top right → "New repository"
3. Name it `prompt-api`
4. Make it **Public** (Render free tier requires public repos)
5. Don't initialize with README (we already have one)
6. Click "Create repository"

### Step 2: Push to GitHub

Run these commands in your terminal:

```bash
# Add the GitHub remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/prompt-api.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Render

1. Go to [Render.com](https://render.com) and sign up/login
2. Click "New +" → "Web Service"
3. Connect your GitHub account if not already connected
4. Select your `prompt-api` repository
5. Configure the service:
   - **Name**: `prompt-api` (or any name you like)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Plan**: Free

6. Click "Create Web Service"

### Step 4: Set Environment Variables

In your Render dashboard, go to your service → "Environment" tab:

Add these environment variables:
- `PROMPT_API_KEY`: `your-secret-api-key-here`
- `PORT`: `10000` (Render uses port 10000)

### Step 5: Deploy

Click "Deploy" and wait for the build to complete. Your API will be available at:
`https://your-app-name.onrender.com`

## Option 2: Railway

### Step 1: Deploy to Railway

1. Go to [Railway.app](https://railway.app) and sign up
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your `prompt-api` repository
4. Railway will automatically detect it's a Python app

### Step 2: Set Environment Variables

In Railway dashboard:
- Go to your project → "Variables" tab
- Add:
  - `PROMPT_API_KEY`: `your-secret-api-key-here`
  - `PORT`: `$PORT` (Railway sets this automatically)

### Step 3: Deploy

Railway will automatically deploy. Your API will be available at the provided URL.

## Option 3: Heroku

### Step 1: Install Heroku CLI

```bash
# macOS
brew install heroku/brew/heroku

# Or download from https://devcenter.heroku.com/articles/heroku-cli
```

### Step 2: Login and Create App

```bash
heroku login
heroku create your-app-name
```

### Step 3: Set Environment Variables

```bash
heroku config:set PROMPT_API_KEY=your-secret-api-key-here
```

### Step 4: Deploy

```bash
git push heroku main
```

## Option 4: Vercel

### Step 1: Create vercel.json

Create a `vercel.json` file:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

### Step 2: Deploy

1. Go to [Vercel.com](https://vercel.com) and sign up
2. Click "New Project" → Import your GitHub repo
3. Vercel will automatically deploy

## Testing Your Deployed API

Once deployed, test your API:

```bash
# Replace with your actual URL
curl https://your-app-name.onrender.com/prompts/ellie -H "X-API-Key: your-secret-api-key-here"
```

## Environment Variables Summary

Set these on your chosen platform:

| Variable | Description | Default |
|----------|-------------|---------|
| `PROMPT_API_KEY` | API key for authentication | (none - open access) |
| `PORT` | Port to run on | 5000 (or platform default) |
| `PROMPTS_FILE` | Path to prompts JSON file | prompts.json |

## Troubleshooting

### Common Issues:

1. **Port Issues**: Most platforms set their own PORT environment variable
2. **API Key**: Make sure to set a strong API key in production
3. **File Paths**: The prompts.json file should be in the root directory
4. **Dependencies**: Make sure all requirements are in requirements.txt

### Getting Help:

- **Render**: [Render Documentation](https://render.com/docs)
- **Railway**: [Railway Documentation](https://docs.railway.app)
- **Heroku**: [Heroku Documentation](https://devcenter.heroku.com)
- **Vercel**: [Vercel Documentation](https://vercel.com/docs)
