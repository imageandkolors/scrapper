# 📚 Lead Finder - Documentation Index

Welcome to Lead Finder! This index will help you find the right documentation for your needs.

## 🚀 Getting Started (Start Here!)

**New to the project?** Start with these:

1. **[GETTING_STARTED.md](GETTING_STARTED.md)** - 5-minute setup guide
2. **[QUICKSTART.md](QUICKSTART.md)** - Quick reference for setup
3. **[README.md](README.md)** - Full project documentation

## 📖 Documentation Files

### Setup & Installation

| File | Purpose | When to Use |
|------|---------|-------------|
| **GETTING_STARTED.md** | Complete beginner's guide | First time setup |
| **QUICKSTART.md** | Quick setup reference | Fast setup, know what you're doing |
| **setup.md** | Detailed setup instructions | Need step-by-step help |
| **.env.example** | Environment configuration template | Setting up environment variables |

### Understanding the Project

| File | Purpose | When to Use |
|------|---------|-------------|
| **PROJECT_OVERVIEW.md** | Architecture & design decisions | Want to understand how it works |
| **README.md** | Complete project documentation | General reference |
| **INDEX.md** | This file - documentation guide | Finding the right docs |

### Troubleshooting & Help

| File | Purpose | When to Use |
|------|---------|-------------|
| **TROUBLESHOOTING.md** | Common issues & solutions | Something's not working |
| **test_setup.py** | Verify your setup | Check if everything is installed |

### Development & Usage

| File | Purpose | When to Use |
|------|---------|-------------|
| **run.py** | Production runner | Start the app (production) |
| **dev.py** | Development runner | Develop with hot reload |
| **example_usage.py** | API usage examples | Learn to use the API programmatically |

### Configuration Files

| File | Purpose |
|------|---------|
| **.replit** | Replit configuration |
| **requirements.txt** | Python dependencies |
| **pyproject.toml** | Poetry configuration |
| **.gitignore** | Git ignore rules |
| **start.sh** | Unix/Linux/Mac startup script |
| **start.bat** | Windows startup script |

## 🎯 Quick Navigation by Task

### "I want to..."

**...set up the project for the first time**
→ Read [GETTING_STARTED.md](GETTING_STARTED.md)

**...understand how it works**
→ Read [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)

**...fix an error**
→ Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

**...run the app**
→ Run `python run.py` (see [QUICKSTART.md](QUICKSTART.md))

**...develop and modify code**
→ Run `python dev.py` (see [README.md](README.md))

**...use the API programmatically**
→ Check [example_usage.py](example_usage.py)

**...deploy to production**
→ See deployment section in [README.md](README.md)

**...understand the lead scoring**
→ See scoring section in [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)

## 📁 Code Structure

### Backend (Python)

```
backend/
├── main.py          # FastAPI app + API endpoints
├── scraper.py       # Google Maps scraper + website auditor
├── scoring.py       # Lead scoring algorithm
└── database.py      # SQLAlchemy models
```

**Key files:**
- `backend/main.py` - All API endpoints, CORS, static file serving
- `backend/scraper.py` - Playwright-based scraping and auditing
- `backend/scoring.py` - Lead scoring logic (0-100 points)
- `backend/database.py` - PostgreSQL models (businesses, audits)

### Frontend (React)

```
frontend/src/
├── pages/
│   ├── SearchPage.jsx       # Search form
│   ├── LeadDashboard.jsx    # Lead table with filters
│   └── BusinessDetail.jsx   # Full audit details
├── App.jsx                  # Main app + routing
├── main.jsx                 # React entry point
└── index.css                # Tailwind imports
```

**Key files:**
- `frontend/src/App.jsx` - React Router setup
- `frontend/src/pages/SearchPage.jsx` - Search interface
- `frontend/src/pages/LeadDashboard.jsx` - Lead list and filters
- `frontend/src/pages/BusinessDetail.jsx` - Detailed audit view

## 🔧 Scripts & Tools

| Script | Command | Purpose |
|--------|---------|---------|
| **run.py** | `python run.py` | Start production server |
| **dev.py** | `python dev.py` | Start development server |
| **test_setup.py** | `python test_setup.py` | Verify installation |
| **example_usage.py** | `python example_usage.py` | API usage demo |
| **start.sh** | `bash start.sh` | Full setup + start (Unix) |
| **start.bat** | `start.bat` | Full setup + start (Windows) |

## 📊 Features Overview

### What the App Does

1. **Scrapes Google Maps** for business listings
2. **Audits websites** for quality issues
3. **Scores leads** from 0-100 based on issues
4. **Displays dashboard** with sortable/filterable results
5. **Exports CSV** for outreach campaigns

### What Gets Checked

- ✅ Website presence (no website = top lead)
- ✅ SSL/HTTPS status
- ✅ Page load speed
- ✅ Mobile responsiveness
- ✅ Broken images/assets
- ✅ Outdated design patterns
- ✅ Template/placeholder text
- ✅ Business rating & reviews

## 🎓 Learning Path

**Beginner:**
1. Read [GETTING_STARTED.md](GETTING_STARTED.md)
2. Follow setup steps
3. Run your first search
4. Explore the dashboard

**Intermediate:**
1. Read [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)
2. Understand the architecture
3. Try [example_usage.py](example_usage.py)
4. Modify search queries

**Advanced:**
1. Read the source code
2. Modify scoring logic in `backend/scoring.py`
3. Add new audit checks in `backend/scraper.py`
4. Customize the frontend
5. Deploy to production

## 🆘 Getting Help

**Something not working?**
1. Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
2. Run `python test_setup.py`
3. Check the logs for errors
4. Review the relevant documentation

**Want to understand something?**
1. Check this INDEX for the right doc
2. Read [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)
3. Look at the code comments
4. Try [example_usage.py](example_usage.py)

## 📝 Documentation Standards

All documentation follows these principles:
- **Clear**: Easy to understand
- **Actionable**: Tells you what to do
- **Complete**: Covers all scenarios
- **Organized**: Easy to navigate

## 🔄 Keeping Updated

When you modify the project:
- Update relevant documentation
- Add new features to README.md
- Document breaking changes
- Update examples if API changes

## 📞 Quick Reference

**Start the app:**
```bash
python run.py
```

**Development mode:**
```bash
python dev.py
```

**Test setup:**
```bash
python test_setup.py
```

**Build frontend:**
```bash
cd frontend && npm run build
```

**API docs:**
http://localhost:8000/docs

**Health check:**
http://localhost:8000/health

---

**Happy lead finding! 🎯**

*Choose the right documentation for your needs and get started!*
