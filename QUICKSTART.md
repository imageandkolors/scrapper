# 🚀 Quick Start Guide

## Prerequisites

Before running the app, you need:

1. **PostgreSQL Database** (Replit provides this)
2. **Python 3.11+**
3. **Node.js 18+**

## Step-by-Step Setup

### 1️⃣ Database Setup (Replit)

1. In Replit, click **Tools** → **Database**
2. Create a **PostgreSQL** database
3. Copy the connection string
4. Create a `.env` file in the root:
   ```
   DATABASE_URL=postgresql://user:password@host:5432/dbname
   ```

### 2️⃣ Install Dependencies

**Option A: Automatic (Recommended)**
```bash
bash start.sh
```

**Option B: Manual**
```bash
# Python dependencies
pip install -r requirements.txt
playwright install chromium

# Frontend dependencies
cd frontend
npm install
npm run build
cd ..
```

### 3️⃣ Run the Application

**Production Mode** (serves built frontend):
```bash
python run.py
```

**Development Mode** (backend only):
```bash
python dev.py
```

Then in another terminal:
```bash
cd frontend
npm run dev
```

### 4️⃣ Access the App

- **Production**: http://localhost:8000
- **Development**: http://localhost:5173 (frontend) + http://localhost:8000 (API)
- **API Docs**: http://localhost:8000/docs

## 🎯 How to Use

1. **Search Page**: Enter a query like "coffee shops in Seattle"
2. **Wait**: The app scrapes Google Maps and audits websites (1-2 min)
3. **Dashboard**: View leads sorted by score
4. **Details**: Click any lead to see full audit
5. **Export**: Download CSV for outreach

## 📊 Lead Scoring

| Issue | Points |
|-------|--------|
| No website | 100 |
| No SSL/HTTPS | +40 |
| Slow load (>3s) | +30 |
| Not mobile responsive | +20 |
| Broken assets | +20 |
| Outdated design | +10 |
| Template text | +10 |
| Low reviews/rating | +5-10 |

**Score 60+** = Strong lead worth contacting

## 🛠️ Troubleshooting

**"Database connection failed"**
- Check your `.env` file has the correct `DATABASE_URL`
- Make sure PostgreSQL is running

**"Playwright not found"**
```bash
playwright install chromium
```

**"Frontend not showing"**
```bash
cd frontend
npm install
npm run build
```

**"Port 8000 already in use"**
- Kill the existing process or change port in `run.py`

## 📁 Project Structure

```
lead-finder/
├── backend/
│   ├── main.py          # FastAPI app
│   ├── scraper.py       # Google Maps + website auditor
│   ├── scoring.py       # Lead scoring logic
│   └── database.py      # SQLAlchemy models
├── frontend/
│   └── src/
│       ├── pages/       # React pages
│       └── App.jsx      # Main app
├── run.py               # Production runner
├── dev.py               # Development runner
└── requirements.txt     # Python deps
```

## 🔑 Key Features

✅ Google Maps scraping  
✅ Automated website audits  
✅ SSL, speed, mobile checks  
✅ Lead scoring algorithm  
✅ Sortable dashboard  
✅ CSV export  
✅ Detailed business profiles  

## 📝 Notes

- Scraping takes 1-2 minutes per search
- Some sites may block automated access
- Respect robots.txt and rate limits
- Use responsibly for legitimate business purposes

## 🆘 Need Help?

Check the full README.md for more details or open an issue.
