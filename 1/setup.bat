@echo off
REM StyleSense Setup Script for Windows
REM This script sets up the entire project

echo.
echo 🎨 StyleSense - AI Fashion Recommender
echo ========================================
echo.

REM Check Python installation
echo ✓ Checking Python installation...
python --version >nul 2>&1 || (
    echo Python is not installed
    exit /b 1
)

echo.
echo 📦 Setting up Backend...
echo.

REM Navigate to backend
cd backend

REM Create virtual environment (optional but recommended)
REM python -m venv venv
REM venv\Scripts\activate

REM Install dependencies
echo Installing Python packages...
pip install -r requirements.txt

echo.
echo ⚙️  Environment Setup
echo.

REM Check if .env exists
if not exist .env (
    echo Creating .env file from template...
    copy .env.example .env
    echo ⚠️  Please update .env with your Gemini API key!
    echo    Open backend\.env and add: GEMINI_API_KEY=your_key_here
)

echo.
echo ✅ Setup Complete!
echo.
echo 📝 Next Steps:
echo 1. Update backend\.env with your Gemini API key
echo 2. Run: python app.py (to start backend server)
echo 3. Open frontend\index.html in your browser
echo.
echo 🌟 Backend will run at: http://localhost:5000
echo 🌟 Frontend: Open frontend\index.html
echo.
pause
