#!/usr/bin/env python3
"""Simple runner script for development"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

if __name__ == "__main__":
    import uvicorn
    from backend.main import app
    
    print("Starting Lead Finder API on http://0.0.0.0:8000")
    print("Make sure you've built the frontend: cd frontend && npm run build")
    
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
