#!/bin/bash

echo "🚀 Prompt API Deployment Helper"
echo "================================"
echo ""

echo "Which platform would you like to deploy to?"
echo "1. Render (Recommended - Easiest)"
echo "2. Railway"
echo "3. Heroku"
echo "4. Vercel"
echo "5. Exit"
echo ""

read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo ""
        echo "🎯 Deploying to Render..."
        echo ""
        echo "Step 1: Create a GitHub repository"
        echo "   - Go to https://github.com"
        echo "   - Click '+' → 'New repository'"
        echo "   - Name it 'prompt-api'"
        echo "   - Make it PUBLIC"
        echo "   - Don't initialize with README"
        echo ""
        echo "Step 2: Push to GitHub"
        echo "   Run these commands:"
        echo "   git remote add origin https://github.com/YOUR_USERNAME/prompt-api.git"
        echo "   git branch -M main"
        echo "   git push -u origin main"
        echo ""
        echo "Step 3: Deploy on Render"
        echo "   - Go to https://render.com"
        echo "   - Click 'New +' → 'Web Service'"
        echo "   - Connect GitHub and select your repo"
        echo "   - Build Command: pip install -r requirements.txt"
        echo "   - Start Command: python app.py"
        echo "   - Set environment variables:"
        echo "     PROMPT_API_KEY=your-secret-key"
        echo "     PORT=10000"
        echo ""
        echo "Your API will be available at: https://your-app-name.onrender.com"
        ;;
    2)
        echo ""
        echo "🚂 Deploying to Railway..."
        echo ""
        echo "Step 1: Go to https://railway.app"
        echo "Step 2: Click 'New Project' → 'Deploy from GitHub repo'"
        echo "Step 3: Select your prompt-api repository"
        echo "Step 4: Set environment variables:"
        echo "   PROMPT_API_KEY=your-secret-key"
        echo "   PORT=\$PORT"
        echo ""
        echo "Railway will automatically deploy your app!"
        ;;
    3)
        echo ""
        echo "⚡ Deploying to Heroku..."
        echo ""
        echo "Step 1: Install Heroku CLI:"
        echo "   brew install heroku/brew/heroku"
        echo ""
        echo "Step 2: Login and create app:"
        echo "   heroku login"
        echo "   heroku create your-app-name"
        echo ""
        echo "Step 3: Set environment variables:"
        echo "   heroku config:set PROMPT_API_KEY=your-secret-key"
        echo ""
        echo "Step 4: Deploy:"
        echo "   git push heroku main"
        echo ""
        echo "Your API will be available at: https://your-app-name.herokuapp.com"
        ;;
    4)
        echo ""
        echo "⚡ Deploying to Vercel..."
        echo ""
        echo "Step 1: Go to https://vercel.com"
        echo "Step 2: Click 'New Project' → Import your GitHub repo"
        echo "Step 3: Vercel will automatically detect and deploy"
        echo ""
        echo "Your API will be available at the provided Vercel URL"
        ;;
    5)
        echo "Goodbye! 👋"
        exit 0
        ;;
    *)
        echo "Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "📚 For detailed instructions, see DEPLOYMENT.md"
echo "🔧 For troubleshooting, check the platform documentation"
echo ""
echo "Happy deploying! 🎉"
