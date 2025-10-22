@echo off
echo 🚀 Transaction Risk Analytics API - Railway Deployment
echo ======================================================

REM Check if git is initialized
if not exist ".git" (
    echo 📝 Initializing Git repository...
    git init
    git add .
    git commit -m "Initial commit: Transaction Risk Analytics API"
    echo ✅ Git repository initialized
) else (
    echo ✅ Git repository already exists
)

REM Check for changes and offer to commit
git status --porcelain > nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo 📝 Checking for changes...
    for /f %%i in ('git status --porcelain ^| find /c /v ""') do set changes=%%i
    if !changes! GTR 0 (
        set /p commit="🤔 You have uncommitted changes. Commit and push? (y/n): "
        if /i "!commit!"=="y" (
            git add .
            git commit -m "Deploy: %date% %time%"
            git push origin main
            echo ✅ Changes committed and pushed
        )
    ) else (
        echo ✅ No uncommitted changes
    )
)

echo.
echo 🎯 Next Steps:
echo 1. Go to https://railway.app
echo 2. Click 'New Project' → 'Deploy from GitHub repo'
echo 3. Select your repository
echo 4. Add environment variables:
echo    - SUPABASE_URL=your-supabase-url
echo    - SUPABASE_KEY=your-supabase-key
echo 5. Deploy!
echo.
echo 📚 For detailed instructions, see DEPLOYMENT_GUIDE.md
echo.
echo ✨ Happy Deploying!
pause
