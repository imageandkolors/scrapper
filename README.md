# Lead Finder - Web Development Prospect Finder

A web app that finds businesses with poor or missing websites, perfect for web development services outreach.

## Features

- **Google Maps Scraping**: Search for businesses by category and location
- **Website Auditing**: Automatically checks website quality
- **Lead Scoring**: Ranks prospects from 0-100 based on website issues
- **Dashboard**: View and filter high-quality leads
- **CSV Export**: Export leads for outreach campaigns

## Tech Stack

- **Backend**: Python, FastAPI, Playwright
- **Frontend**: React, Vite, TailwindCSS
- **Database**: PostgreSQL (Replit Postgres)

## Setup

### 1. Database Setup

In Replit:
1. Go to Tools → Database
2. Create a new PostgreSQL database
3. Copy the connection string
4. Create a `.env` file with:
   ```
   DATABASE_URL=your_postgres_connection_string
   ```

### 2. Install Dependencies

The `start.sh` script will automatically:
- Install Python packages
- Install Playwright browsers
- Install and build frontend
- Start the backend server

### 3. Run the App

Click the "Run" button in Replit, or:
```bash
bash start.sh
```

The backend will run on port 8000, and the frontend will be served from the backend.

## Usage

1. **Search**: Enter a query like "coffee shops in Seattle"
2. **Wait**: The scraper will find businesses and audit their websites
3. **Review**: Check the dashboard for high-scoring leads
4. **Export**: Download CSV for outreach

## Lead Scoring

- **100 points**: No website
- **40 points**: No SSL/HTTPS
- **30 points**: Slow load time (>3s)
- **20 points**: Not mobile responsive
- **20 points**: Broken assets
- **10 points**: Outdated design
- **10 points**: Template text
- **Bonus**: Low ratings or reviews

## API Endpoints

- `POST /api/scrape` - Run scraper
- `GET /api/leads` - Get high-scoring leads
- `GET /api/all` - Get all businesses
- `GET /api/business/{id}` - Get business details
- `GET /api/export` - Export CSV
- `GET /health` - Health check

## Development

### Backend Only
```bash
cd backend
python main.py
```

### Frontend Only
```bash
cd frontend
npm run dev
```

## Notes

- Scraping can take 1-2 minutes depending on results
- Some websites may block automated access
- Respect robots.txt and rate limits
- Use responsibly for legitimate business purposes

## License

Personal use only
