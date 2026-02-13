#!/bin/bash

# StyleSense Setup Script
# This script sets up the entire project

echo "🎨 StyleSense - AI Fashion Recommender"
echo "========================================"
echo ""

# Check Python installation
echo "✓ Checking Python installation..."
python --version || { echo "Python is not installed"; exit 1; }

echo ""
echo "📦 Setting up Backend..."
echo ""

# Navigate to backend
cd backend

# Create virtual environment (optional but recommended)
# python -m venv venv
# source venv/bin/activate  # For Linux/Mac
# venv\Scripts\activate  # For Windows

# Install dependencies
echo "Installing Python packages..."
pip install -r requirements.txt

echo ""
echo "⚙️  Environment Setup"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please update .env with your Gemini API key!"
    echo "   Open backend/.env and add: GEMINI_API_KEY=your_key_here"
fi

echo ""
echo "✅ Setup Complete!"
echo ""
echo "📝 Next Steps:"
echo "1. Update backend/.env with your Gemini API key"
echo "2. Run: python app.py (to start backend server)"
echo "3. Open frontend/index.html in your browser"
echo ""
echo "🌟 Backend will run at: http://localhost:5000"
echo "🌟 Frontend: Open frontend/index.html"
echo ""
