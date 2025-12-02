# 🚀 Getting Started with Lead Finder

Welcome! This guide will get you up and running in 5 minutes.

## What You're Building

A web app that finds businesses with poor or missing websites - perfect prospects for your web development services.

## Prerequisites

✅ Python 3.11+  
✅ Node.js 18+  
✅ PostgreSQL database (Replit provides this)

## 5-Minute Setup

### Step 1: Get the Database URL

**In Replit:**
1. Click **Tools** → **Database**
2. Create a **PostgreSQL** database
3. Copy the connection string (looks like `postgresql://...`)

**Elsewhere:**
- Use any PostgreSQL database
- Local: `postgresql://localhost:5432/leadfinder`
- Cloud: Heroku, Railway, Supabase, etc.

### Step 2: Configure Environment

Create a `.env` file:
```bash
DATABASE_URL=your_postgresql_connection_string_here
```

### Step 3: Install & Run

**Option A: Automatic (Recommended)**
```bash
bash start.sh
```

**Option B: Manual**
```bash
# Install Python dependencies
pip install -r requirements.txt
playwright install chromium

# Install and build frontend
cd frontend
npm install
npm run build
cd ..

# Run the app
python run.py
```

### Step 4: Open the App

Visit: **http://localhost:8000**

## First Search

1. Enter a search query: `"coffee shops in Seattle"`
2. Click **Run Scraper**
3. Wait 1-2 minutes while it:
   - Scrapes Google Maps
   - Audits each website
   - Calculates lead scores
4. View results in the **Dashboard**
5. Click any business for full details
6. Export CSV for outreach

## Understanding Lead Scores

| Score | Meaning | Action |
|-------|---------|--------|
| 80-100 | 🔥 Hot lead | Contact immediately |
| 60-79 | ⭐ Good lead | Strong prospect |
| 40-59 | 💡 Warm lead | Worth considering |
| 0-39 | 😐 Cold lead | Low priority |

**What makes a high score?**
- No website (100 points)
- No SSL/HTTPS (+40)
- Slow loading (+30)
- Not mobile-friendly (+20)
- Broken images/links (+20)
- Outdated design (+10)
- Template text (+10)

## Development Mode

Want to modify the code?

**Terminal 1 - Backend:**
```bash
python dev.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

Frontend: http://localhost:5173  
Backend: http://localhost:8000  
API Docs: http://localhost:8000/docs

## Project Structure

```
lead-finder/
├── backend/          # Python FastAPI backend
│   ├── main.py      # API endpoints
│   ├── scraper.py   # Google Maps + website auditor
│   ├── scoring.py   # Lead scoring logic
│   └── database.py  # Database models
├── frontend/         # React frontend
│   └── src/
│       ├── pages/   # Search, Dashboard, Details
│       └── App.jsx  # Main app
└── run.py           # Start here!
```

## Quick Commands

```bash
# Production mode
python run.py

# Development mode
python dev.py

# Test setup
python test_setup.py

# Install dependencies
pip install -r requirements.txt
playwright install chromium

# Build frontend
cd frontend && npm run build

# Run frontend dev server
cd frontend && npm run dev
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/api/scrape` | POST | Run scraper |
| `/api/leads` | GET | Get top leads |
| `/api/all` | GET | Get all businesses |
| `/api/business/{id}` | GET | Get details |
| `/api/export` | GET | Download CSV |

## Example Search Queries

Try these:
- `"restaurants in Austin"`
- `"plumbers near Denver"`
- `"hair salons in Miami"`
- `"auto repair shops in Portland"`
- `"yoga studios in San Francisco"`
- `"coffee shops in Brooklyn"`

## Tips for Best Results

✅ Use specific locations  
✅ Try different business categories  
✅ Start with 10-20 results  
✅ Check multiple cities  
✅ Export and track your outreach  

❌ Don't scrape too frequently (rate limits)  
❌ Don't use vague queries  
❌ Don't request 100+ results at once  

## What Gets Checked?

For each business, we check:

**Basic Info:**
- Name, address, phone
- Category, rating, reviews
- Website URL (if any)

**Website Audit (if website exists):**
- ✓ SSL/HTTPS status
- ✓ Page load speed
- ✓ Mobile responsiveness
- ✓ Broken images/assets
- ✓ Outdated design patterns
- ✓ Template/placeholder text

## Next Steps

1. ✅ Run your first search
2. ✅ Review the dashboard
3. ✅ Check a business detail page
4. ✅ Export your first CSV
5. ✅ Start reaching out to leads!

## Need Help?

- 📖 **Full docs**: See `README.md`
- 🔧 **Issues**: Check `TROUBLESHOOTING.md`
- 🏗️ **Architecture**: Read `PROJECT_OVERVIEW.md`
- ⚡ **Quick ref**: See `QUICKSTART.md`

## Common Issues

**"Database connection failed"**
→ Check your `.env` file

**"Playwright not found"**
→ Run `playwright install chromium`

**"Frontend not showing"**
→ Run `cd frontend && npm run build`

**"Port already in use"**
→ Kill the process or change port in `run.py`

## Success Checklist

Before you start scraping:

- [ ] PostgreSQL database created
- [ ] `.env` file configured with `DATABASE_URL`
- [ ] Python dependencies installed
- [ ] Playwright browsers installed
- [ ] Frontend built
- [ ] App running on http://localhost:8000
- [ ] Health check passes: http://localhost:8000/health

Run `python test_setup.py` to verify everything!

## Ready to Find Leads?

You're all set! Start with a simple search and watch the leads roll in.

**Happy prospecting! 🎯**

---

*Built for web developers who want to find clients that actually need their services.*
