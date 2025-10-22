#!/bin/bash

# Transaction Risk Analytics API - Quick Deploy Script
# This script helps you deploy to Railway quickly

echo "🚀 Transaction Risk Analytics API - Railway Deployment"
echo "======================================================"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📝 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit: Transaction Risk Analytics API"
    echo "✅ Git repository initialized"
else
    echo "✅ Git repository already exists"
fi

# Check if remote origin exists
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "⚠️  No remote origin found"
    echo "Please add your GitHub repository URL:"
    echo "git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
    echo "Then run: git push -u origin main"
else
    echo "✅ Remote origin configured"
    
    # Ask if user wants to push changes
    read -p "🤔 Do you want to push changes to GitHub? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "📤 Pushing to GitHub..."
        git add .
        git commit -m "Deploy: $(date '+%Y-%m-%d %H:%M:%S')"
        git push origin main
        echo "✅ Changes pushed to GitHub"
    fi
fi

echo ""
echo "🎯 Next Steps:"
echo "1. Go to https://railway.app"
echo "2. Click 'New Project' → 'Deploy from GitHub repo'"
echo "3. Select your repository"
echo "4. Add environment variables:"
echo "   - SUPABASE_URL=your-supabase-url"
echo "   - SUPABASE_KEY=your-supabase-key"
echo "5. Deploy!"
echo ""
echo "📚 For detailed instructions, see DEPLOYMENT_GUIDE.md"
echo ""
echo "✨ Happy Deploying!"
