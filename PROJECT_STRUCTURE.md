# Project Structure

```
tariff-app/
├── backend/                          # Python FastAPI Backend
│   ├── main.py                      # FastAPI application & endpoints
│   ├── database.py                  # SQLAlchemy models & database setup
│   ├── scraper.py                   # Tariff data scraping logic
│   ├── requirements.txt              # Python dependencies
│   ├── .env.example                 # Environment variables template
│   └── Dockerfile                   # Docker configuration for backend
│
├── frontend/                         # React Web Dashboard
│   ├── App.jsx                      # Main React component
│   ├── App.css                      # Styling
│   ├── index.js                     # React entry point
│   ├── components/
│   │   ├── Dashboard.jsx            # Dashboard overview page
│   │   ├── TariffList.jsx           # Tariff search & list view
│   │   └── ChangeLog.jsx            # Change history view
│   ├── public/
│   │   └── index.html               # HTML template
│   ├── package.json                 # Node.js dependencies
│   ├── .env.example                 # Environment variables template
│   └── Dockerfile                   # Docker configuration for frontend
│
├── docker-compose.yml               # Multi-container setup
├── README.md                         # Quick start & feature overview
├── DEPLOYMENT.md                     # Production deployment guide
└── PROJECT_STRUCTURE.md              # This file

## File Descriptions

### Backend Files

**main.py** - FastAPI Application
- Routes for /api/tariffs, /api/changes, /api/stats
- Scheduled daily tariff scraping job
- CORS middleware for web access
- Health check endpoint

**database.py** - Database Layer
- SQLAlchemy ORM models
- Tariff and TariffHistory tables
- Database connection management
- Session management

**scraper.py** - Data Fetching
- TariffScraper class for fetching tariff data
- Integration with US Customs sources
- Integration with China Customs sources
- Data transformation and storage
- Change tracking logic

**requirements.txt** - Python Dependencies
- fastapi, uvicorn (web framework)
- sqlalchemy (ORM)
- requests, beautifulsoup4 (web scraping)
- APScheduler (task scheduling)
- pydantic (data validation)

### Frontend Files

**App.jsx** - Main Component
- Tab navigation between pages
- Statistics loading
- API integration
- Main layout structure

**components/Dashboard.jsx** - Overview Page
- Statistics cards (US tariffs, China tariffs, etc.)
- Information about the dashboard
- Key metrics display

**components/TariffList.jsx** - Search & List
- Filter by country and HS code
- Paginated table view
- Sort by various fields
- Detailed tariff information

**components/ChangeLog.jsx** - Changes View
- Filter by country and time period
- Shows old → new rate changes
- Lists change reasons
- Date-based filtering

**App.css** - Styling
- Responsive design (mobile & desktop)
- Color scheme and typography
- Component-specific styles
- Animation and transitions

## Data Flow

```
┌─────────────────────────────────┐
│   User Access Dashboard         │
│   (http://localhost:3000)       │
└──────────────────┬──────────────┘
                   │
                   ▼
┌─────────────────────────────────┐
│   React Frontend                │
│   - Fetches data via API calls  │
│   - Renders UI components       │
└──────────────────┬──────────────┘
                   │
                   ▼ HTTP GET/POST
┌─────────────────────────────────┐
│   FastAPI Backend               │
│   - /api/tariffs                │
│   - /api/changes                │
│   - /api/stats                  │
└──────────────────┬──────────────┘
                   │
                   ▼
┌─────────────────────────────────┐
│   Database                      │
│   - Tariffs table               │
│   - TariffHistory table         │
└─────────────────────────────────┘

Daily (00:00):
┌─────────────────────────────────┐
│   APScheduler Job               │
│   - Runs scraper.py             │
│   - Fetches US tariffs          │
│   - Fetches China tariffs       │
│   - Updates database            │
│   - Tracks changes              │
└─────────────────────────────────┘
```

## Dependencies

### Backend
- **fastapi** - Web framework
- **uvicorn** - ASGI server
- **sqlalchemy** - ORM
- **psycopg2** - PostgreSQL adapter
- **requests** - HTTP library
- **beautifulsoup4** - Web scraping
- **APScheduler** - Job scheduling
- **pydantic** - Data validation
- **python-dotenv** - Environment variables

### Frontend
- **react** - UI library
- **react-dom** - React rendering
- **axios** - HTTP client
- **react-router-dom** - Routing
- **date-fns** - Date formatting

## Environment Variables

### Backend (.env)
```
DATABASE_URL=sqlite:///./tariff_data.db
API_HOST=0.0.0.0
API_PORT=8000
SCRAPE_HOUR=0
SCRAPE_MINUTE=0
ALLOWED_ORIGINS=http://localhost:3000
```

### Frontend (.env)
```
REACT_APP_API_URL=http://localhost:8000
```

## Running Locally

1. **Backend**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```

2. **Frontend**
   ```bash
   cd frontend
   npm install
   npm start
   ```

3. **Database**
   - SQLite (default): Automatic, stored as `tariff_data.db`
   - PostgreSQL: Update `DATABASE_URL` in backend/.env

## Key Features

### Data Management
- Tracks tariff rates for 2400+ HS codes
- Records historical changes
- Supports US and China tariffs

### API Endpoints
- `GET /api/tariffs` - Retrieve all tariffs
- `GET /api/changes` - Get recent changes
- `GET /api/stats` - Dashboard statistics
- `POST /api/trigger-scrape` - Manual data refresh

### Frontend Pages
- **Dashboard** - Overview and statistics
- **Tariff List** - Search and filter tariffs
- **Change Log** - Track rate changes

## Extending the Application

### Add New Tariff Sources
1. Update `scraper.py` with new data source
2. Implement fetch method
3. Test data parsing
4. Add to daily job

### Add User Authentication
1. Install `fastapi-jwt-extended`
2. Add user model to `database.py`
3. Create login endpoint
4. Add JWT protection to routes

### Add Email Notifications
1. Install `python-multipart` and `aiosmtplib`
2. Create email notification function
3. Trigger on significant changes
4. Add email config to `.env`

### Deploy to Production
See DEPLOYMENT.md for complete instructions

