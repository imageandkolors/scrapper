# Quick Setup Guide

## 1. Set up PostgreSQL Database

In Replit:
1. Click on "Tools" in the left sidebar
2. Select "Database" 
3. Create a PostgreSQL database
4. Copy the connection string (looks like: `postgresql://user:pass@host:5432/dbname`)

## 2. Create Environment File

Create a `.env` file in the root directory:

```bash
DATABASE_URL=your_postgresql_connection_string_here
```

## 3. Run the Application

Click the "Run" button in Replit, or run:

```bash
bash start.sh
```

This will:
- Install Python dependencies
- Install Playwright browsers
- Install and build the React frontend
- Start the FastAPI backend on port 8000

## 4. Access the App

Open your browser to the Replit URL (usually shown in the webview panel)

## Manual Setup (if needed)

### Backend only:
```bash
pip install -r requirements.txt
playwright install chromium
python run.py
```

### Frontend only:
```bash
cd frontend
npm install
npm run dev
```

## Troubleshooting

**Database connection error**: Make sure your `.env` file has the correct `DATABASE_URL`

**Playwright error**: Run `playwright install chromium` manually

**Frontend not showing**: Make sure you ran `npm run build` in the frontend directory

**Port already in use**: Change the port in `run.py` or kill the existing process
