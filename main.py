"""Main entry point for the application"""
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.dirname(__file__))

if __name__ == "__main__":
    import uvicorn
    from backend.main import app
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
