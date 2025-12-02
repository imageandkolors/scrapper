# Lead Finder - Project Overview

## 🎯 Purpose

Find businesses that need better websites by:
1. Scraping Google Maps for business listings
2. Auditing their websites (if they have one)
3. Scoring them as leads based on website quality issues
4. Providing a dashboard to review and export prospects

## 🏗️ Architecture

### Backend (Python + FastAPI)

**Files:**
- `backend/main.py` - FastAPI app with all API endpoints
- `backend/scraper.py` - Google Maps scraper + website auditor using Playwright
- `backend/scoring.py` - Lead scoring algorithm
- `backend/database.py` - SQLAlchemy models for PostgreSQL

**Key Features:**
- Async scraping with Playwright
- Website quality checks (SSL, speed, mobile, broken assets, outdated design)
- Lead scoring algorithm (0-100 points)
- CSV export functionality
- CORS enabled for frontend

### Frontend (React + Vite + TailwindCSS)

**Files:**
- `frontend/src/App.jsx` - Main app with routing
- `frontend/src/pages/SearchPage.jsx` - Search form
- `frontend/src/pages/LeadDashboard.jsx` - Lead list with filters
- `frontend/src/pages/BusinessDetail.jsx` - Full business audit details

**Key Features:**
- Clean, minimal UI
- Real-time scraping status
- Sortable/filterable lead table
- Detailed audit breakdowns
- CSV export button

### Database (PostgreSQL)

**Tables:**
- `businesses` - Business info + lead score
- `website_audits` - Detailed audit metrics

## 🔄 Workflow

1. **User enters search query** (e.g., "coffee shops in Seattle")
2. **Backend scrapes Google Maps** using Playwright
   - Extracts: name, address, category, rating, reviews, phone, website
3. **For each business with a website:**
   - Opens site in headless browser
   - Measures load time
   - Checks SSL, mobile responsiveness, broken assets
   - Detects outdated design patterns
   - Looks for template/placeholder text
4. **Calculate lead score** based on issues found
5. **Store in database** with full audit details
6. **Display in dashboard** sorted by score
7. **User can export CSV** for outreach

## 📊 Lead Scoring Logic

```python
Score = 0

# No website = instant top lead
if no_website:
    score = 100

# Website issues
if no_ssl:           score += 40
if slow_load:        score += 30
if not_mobile:       score += 20
if broken_assets:    score += 20
if outdated_design:  score += 10
if template_text:    score += 10

# Business signals
if low_reviews:      score += 5
if low_rating:       score += 5

# Cap at 100
score = min(score, 100)
```

**Interpretation:**
- **80-100**: Excellent lead (no website or major issues)
- **60-79**: Good lead (multiple issues)
- **40-59**: Moderate lead (some issues)
- **0-39**: Weak lead (minor issues only)

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11, FastAPI, Uvicorn |
| Scraping | Playwright (Chromium) |
| Database | PostgreSQL, SQLAlchemy |
| Frontend | React 18, Vite, TailwindCSS |
| Routing | React Router v6 |
| Deployment | Replit (or any Python host) |

## 📁 File Structure

```
lead-finder/
├── backend/
│   ├── __init__.py
│   ├── main.py              # FastAPI app + endpoints
│   ├── scraper.py           # Google Maps + website auditor
│   ├── scoring.py           # Lead scoring algorithm
│   └── database.py          # SQLAlchemy models
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── SearchPage.jsx       # Search form
│   │   │   ├── LeadDashboard.jsx    # Lead table
│   │   │   └── BusinessDetail.jsx   # Full audit view
│   │   ├── App.jsx          # Main app + routing
│   │   ├── main.jsx         # React entry point
│   │   └── index.css        # Tailwind imports
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
│
├── run.py                   # Production runner
├── dev.py                   # Development runner
├── test_setup.py            # Setup verification
├── requirements.txt         # Python dependencies
├── .env.example             # Environment template
├── .replit                  # Replit configuration
├── start.sh                 # Unix setup script
├── start.bat                # Windows setup script
├── README.md                # Full documentation
├── QUICKSTART.md            # Quick setup guide
└── PROJECT_OVERVIEW.md      # This file
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/api/scrape` | Run scraper for a query |
| GET | `/api/leads` | Get high-scoring leads (score >= 60) |
| GET | `/api/all` | Get all businesses |
| GET | `/api/business/{id}` | Get single business details |
| GET | `/api/export` | Download CSV of leads |
| GET | `/*` | Serve frontend (SPA routing) |

## 🚀 Deployment Options

### Replit (Recommended)
1. Import project
2. Set up PostgreSQL database
3. Configure `.env`
4. Click "Run"

### Other Platforms
- **Heroku**: Use Procfile with `web: python run.py`
- **Railway**: Auto-detects Python + Node
- **Render**: Configure build + start commands
- **VPS**: Run with systemd or PM2

## 🔒 Security Notes

- CORS enabled for development (restrict in production)
- No authentication (add if exposing publicly)
- Rate limiting recommended for scraping
- Respect robots.txt and website ToS
- Use responsibly for legitimate business purposes

## 🎨 Design Decisions

**Why Playwright over Selenium?**
- Faster, more reliable
- Better async support
- Built-in mobile emulation

**Why FastAPI over Flask?**
- Native async support
- Auto-generated API docs
- Type hints and validation

**Why PostgreSQL over SQLite?**
- Better for Replit deployment
- Handles concurrent writes
- Production-ready

**Why Vite over Create React App?**
- Much faster builds
- Better dev experience
- Smaller bundle sizes

## 📈 Future Enhancements

- [ ] Email/phone extraction from websites
- [ ] Social media handle detection
- [ ] Automated email outreach
- [ ] Scheduled scraping (cron jobs)
- [ ] Lead status tracking (contacted, converted, etc.)
- [ ] Multi-user support with authentication
- [ ] Webhook notifications for new leads
- [ ] Integration with CRM systems
- [ ] More audit checks (accessibility, SEO, etc.)
- [ ] Competitor analysis

## 🐛 Known Limitations

- Google Maps may block excessive scraping
- Some websites block headless browsers
- Audit accuracy depends on site complexity
- Scraping speed limited by network/CPU
- No captcha solving (manual intervention needed)

## 📝 License

Personal use only. Not for commercial redistribution.

## 🤝 Contributing

This is a personal project, but feel free to fork and customize for your needs.

---

**Built for web developers who want to find clients that actually need their services.**
