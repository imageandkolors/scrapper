#!/usr/bin/env python3
"""Development script - runs backend without building frontend"""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

if __name__ == "__main__":
    import uvicorn
    from backend.main import app
    
    print("=" * 60)
    print("Lead Finder - Development Mode")
    print("=" * 60)
    print("Backend API: http://localhost:8000")
    print("API Docs: http://localhost:8000/docs")
    print("Health Check: http://localhost:8000/health")
    print()
    print("For frontend development, run in another terminal:")
    print("  cd frontend && npm run dev")
    print("=" * 60)
    
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=["backend"]
    )
