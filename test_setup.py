#!/usr/bin/env python3
"""Test script to verify setup"""
import sys
import os

def test_imports():
    """Test if all required packages are installed"""
    print("Testing imports...")
    errors = []
    
    try:
        import fastapi
        print("✓ FastAPI installed")
    except ImportError:
        errors.append("FastAPI not installed")
    
    try:
        import playwright
        print("✓ Playwright installed")
    except ImportError:
        errors.append("Playwright not installed")
    
    try:
        import sqlalchemy
        print("✓ SQLAlchemy installed")
    except ImportError:
        errors.append("SQLAlchemy not installed")
    
    try:
        import psycopg2
        print("✓ psycopg2 installed")
    except ImportError:
        errors.append("psycopg2 not installed")
    
    return errors

def test_env():
    """Test if environment is configured"""
    print("\nTesting environment...")
    errors = []
    
    if not os.path.exists(".env"):
        errors.append(".env file not found - copy .env.example and configure")
    else:
        print("✓ .env file exists")
        
        from dotenv import load_dotenv
        load_dotenv()
        
        db_url = os.getenv("DATABASE_URL")
        if not db_url:
            errors.append("DATABASE_URL not set in .env")
        elif not db_url.startswith("postgresql://"):
            errors.append("DATABASE_URL should start with postgresql://")
        else:
            print("✓ DATABASE_URL configured")
    
    return errors

def test_frontend():
    """Test if frontend is built"""
    print("\nTesting frontend...")
    errors = []
    
    frontend_dist = "frontend/dist"
    if not os.path.exists(frontend_dist):
        errors.append("Frontend not built - run: cd frontend && npm install && npm run build")
    else:
        print("✓ Frontend built")
    
    return errors

def main():
    print("=" * 60)
    print("Lead Finder - Setup Test")
    print("=" * 60)
    print()
    
    all_errors = []
    
    all_errors.extend(test_imports())
    all_errors.extend(test_env())
    all_errors.extend(test_frontend())
    
    print()
    print("=" * 60)
    
    if all_errors:
        print("❌ Setup incomplete. Issues found:")
        for error in all_errors:
            print(f"  - {error}")
        print()
        print("Run: pip install -r requirements.txt")
        print("Run: playwright install chromium")
        print("Run: cd frontend && npm install && npm run build")
        sys.exit(1)
    else:
        print("✅ All checks passed! Ready to run.")
        print()
        print("Start the app with: python run.py")
        print("Or development mode: python dev.py")
        sys.exit(0)

if __name__ == "__main__":
    main()
