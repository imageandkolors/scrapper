# 🔧 Troubleshooting Guide

## Common Issues & Solutions

### 1. Database Connection Errors

**Error:** `sqlalchemy.exc.OperationalError: could not connect to server`

**Solutions:**
- Check your `.env` file exists and has `DATABASE_URL`
- Verify the connection string format: `postgresql://user:pass@host:5432/dbname`
- In Replit: Make sure PostgreSQL database is created in Tools > Database
- Test connection: `psql $DATABASE_URL` (if psql is installed)

### 2. Playwright Installation Issues

**Error:** `playwright._impl._api_types.Error: Executable doesn't exist`

**Solutions:**
```bash
# Install Playwright browsers
playwright install chromium

# If that fails, try with sudo (Linux/Mac)
sudo playwright install chromium

# Or install all browsers
playwright install
```

**Windows specific:**
- Make sure you have Visual C++ Redistributable installed
- Run PowerShell as Administrator

### 3. Frontend Not Building

**Error:** `npm ERR!` or build failures

**Solutions:**
```bash
cd frontend

# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install

# Try building again
npm run build

# If still failing, check Node version
node --version  # Should be 18+
```

### 4. Port Already in Use

**Error:** `Address already in use: 8000`

**Solutions:**

**Linux/Mac:**
```bash
# Find process using port 8000
lsof -i :8000

# Kill it
kill -9 <PID>
```

**Windows:**
```cmd
# Find process
netstat -ano | findstr :8000

# Kill it
taskkill /PID <PID> /F
```

**Or change port in `run.py`:**
```python
uvicorn.run(app, host="0.0.0.0", port=8001)  # Use 8001 instead
```

### 5. Scraping Returns No Results

**Possible causes:**
- Google Maps changed their HTML structure
- IP blocked by Google (too many requests)
- Search query too specific
- Network/firewall issues

**Solutions:**
- Try a different, broader search query
- Wait a few minutes and try again
- Check if Google Maps loads in a regular browser
- Use a VPN if IP is blocked
- Update Playwright: `pip install --upgrade playwright`

### 6. Website Audit Fails

**Error:** `TimeoutError` or `Navigation failed`

**Causes:**
- Website is down or very slow
- Website blocks headless browsers
- SSL certificate issues
- Firewall blocking requests

**Solutions:**
- The app handles this gracefully - check audit_summary for errors
- Increase timeout in `scraper.py`:
  ```python
  await page.goto(url, wait_until="domcontentloaded", timeout=30000)  # 30s
  ```

### 7. Frontend Shows "Cannot GET /api/..."

**Cause:** Backend not running or wrong proxy configuration

**Solutions:**
- Make sure backend is running: `python run.py`
- Check `frontend/vite.config.js` proxy settings
- In development, run both:
  - Terminal 1: `python dev.py`
  - Terminal 2: `cd frontend && npm run dev`

### 8. CORS Errors in Browser

**Error:** `Access to fetch at 'http://localhost:8000/api/...' has been blocked by CORS policy`

**Solutions:**
- Backend should have CORS enabled (check `backend/main.py`)
- If you changed the frontend URL, update CORS origins:
  ```python
  app.add_middleware(
      CORSMiddleware,
      allow_origins=["http://localhost:5173", "your-frontend-url"],
      ...
  )
  ```

### 9. Module Import Errors

**Error:** `ModuleNotFoundError: No module named 'backend'`

**Solutions:**
```bash
# Make sure you're in the project root
pwd  # or cd on Windows

# Run from root, not from backend/
python run.py  # ✓ Correct
cd backend && python main.py  # ✗ Wrong

# Or add to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"  # Linux/Mac
set PYTHONPATH=%PYTHONPATH%;%CD%  # Windows
```

### 10. Slow Scraping Performance

**Causes:**
- Network latency
- Too many results requested
- Slow websites being audited

**Solutions:**
- Reduce `max_results` in search (try 10 instead of 20)
- Scraping is inherently slow - be patient
- Run on a faster network
- Consider caching results

### 11. Database Tables Not Created

**Error:** `relation "businesses" does not exist`

**Solution:**
The app should auto-create tables on first run. If not:

```python
# Run this Python script once
from backend.database import init_db
init_db()
print("Tables created!")
```

Or manually:
```sql
-- Connect to your database and run:
CREATE TABLE businesses (
    id SERIAL PRIMARY KEY,
    query VARCHAR,
    name VARCHAR,
    category VARCHAR,
    address VARCHAR,
    rating FLOAT,
    review_count INTEGER,
    website VARCHAR,
    phone VARCHAR,
    lead_score INTEGER DEFAULT 0,
    audit_summary JSON,
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE website_audits (
    id SERIAL PRIMARY KEY,
    business_id INTEGER REFERENCES businesses(id),
    load_time FLOAT,
    ssl_ok BOOLEAN DEFAULT FALSE,
    mobile_ok BOOLEAN DEFAULT TRUE,
    broken_assets_count INTEGER DEFAULT 0,
    outdated_ui_flag BOOLEAN DEFAULT FALSE,
    template_text_flag BOOLEAN DEFAULT FALSE,
    raw_audit_data JSON,
    audited_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 12. Replit-Specific Issues

**Issue:** App stops after inactivity

**Solution:** Replit free tier sleeps after inactivity. Upgrade to Always On or use a keep-alive service.

**Issue:** Database connection lost

**Solution:** Replit databases may restart. The app should reconnect automatically. If not, restart the app.

**Issue:** Out of memory

**Solution:** 
- Reduce `max_results` in searches
- Clear old data from database
- Upgrade Replit plan

## 🧪 Testing Your Setup

Run the test script:
```bash
python test_setup.py
```

This checks:
- ✓ All Python packages installed
- ✓ Environment configured
- ✓ Frontend built

## 📊 Debugging Tips

### Enable Debug Logging

In `run.py` or `dev.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check API Directly

Visit http://localhost:8000/docs for interactive API documentation.

Test endpoints:
```bash
# Health check
curl http://localhost:8000/health

# Get leads
curl http://localhost:8000/api/leads

# Scrape (POST)
curl -X POST http://localhost:8000/api/scrape \
  -H "Content-Type: application/json" \
  -d '{"query": "test query", "max_results": 5}'
```

### Check Database

```bash
# Connect to database
psql $DATABASE_URL

# List tables
\dt

# Check businesses
SELECT name, lead_score FROM businesses ORDER BY lead_score DESC LIMIT 10;

# Exit
\q
```

## 🆘 Still Stuck?

1. Check the logs for error messages
2. Verify all dependencies are installed: `pip list` and `npm list`
3. Try a fresh install in a new directory
4. Check if it's a known issue in the project
5. Make sure you're using Python 3.11+ and Node 18+

## 📝 Reporting Issues

When reporting issues, include:
- Operating system and version
- Python version: `python --version`
- Node version: `node --version`
- Full error message and stack trace
- Steps to reproduce
- What you've already tried

---

**Most issues are environment-related. Double-check your setup first!**
