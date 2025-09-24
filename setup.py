#!/usr/bin/env python3
"""
Setup script for Python Weather App
This script helps users set up the weather app with proper dependencies
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    try:
        print("📦 Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        print("✅ Successfully installed all requirements!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements.")
        return False

def check_api_key():
    """Check if API key is configured"""
    try:
        with open('weather_app.py', 'r') as file:
            content = file.read()
            if 'your_api_key_here' in content:
                return False
        return True
    except FileNotFoundError:
        return False

def main():
    print("🌤️ Python Weather App Setup")
    print("=" * 30)
    
    # Install requirements
    if not install_requirements():
        return
    
    # Check API key configuration
    if not check_api_key():
        print("\n⚠️  IMPORTANT: API Key Setup Required!")
        print("1. Visit: https://openweathermap.org/api")
        print("2. Sign up for a free account")
        print("3. Get your API key")
        print("4. Replace 'your_api_key_here' in weather_app.py with your actual API key")
        print("\n📝 After setting up your API key, run: python weather_app.py")
    else:
        print("\n🎉 Setup complete! Your weather app is ready to use.")
        print("Run: python weather_app.py")

if __name__ == "__main__":
    main()
