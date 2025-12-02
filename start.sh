#!/bin/bash

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Install Playwright browsers
echo "Installing Playwright browsers..."
playwright install chromium

# Install frontend dependencies and build
echo "Installing frontend dependencies..."
cd frontend
npm install
echo "Building frontend..."
npm run build
cd ..

# Start backend server
echo "Starting backend server on port 8000..."
python run.py
