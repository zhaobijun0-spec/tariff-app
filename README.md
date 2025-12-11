# Tariff Dashboard - US and China Tariff Tracking

A web-based dashboard that tracks daily tariff rate changes between the United States and China. Real-time data sourced from US Customs and China Customs.

## Features

✅ **Daily Automated Updates** - Automatically fetches tariff data every 24 hours  
✅ **Dashboard Overview** - View statistics at a glance  
✅ **Comprehensive Tariff Database** - Search and filter by country and HS code  
✅ **Change History** - Track tariff rate changes over time  
✅ **REST API** - Programmatic access to all data  
✅ **Responsive Design** - Works on desktop and mobile  

## Architecture

```
┌─────────────────────────────────────────┐
│        Frontend (React)                  │
│  - Dashboard, Tariff List, Change Log   │
│  Port: 3000                             │
└──────────┬──────────────────────────────┘
           │
┌──────────▼──────────────────────────────┐
│        Backend (FastAPI)                 │
│  - REST API, Data Processing            │
│  - APScheduler for daily scraping       │
│  Port: 8000                             │
└──────────┬──────────────────────────────┘
           │
┌──────────▼──────────────────────────────┐
│        Database (PostgreSQL/SQLite)      │
│  - Tariff rates                         │
│  - Historical changes                   │
└─────────────────────────────────────────┘
```

## Quick Start - Local Development

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL (optional, SQLite works for development)

### 1. Clone and Navigate
```bash
cd tariff-app
```

### 2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python -m uvicorn main:app --reload
```
Backend runs on: `http://localhost:8000`

### 3. Frontend Setup (in new terminal)
```bash
cd frontend
npm install
cp .env.example .env
npm start
```
Frontend runs on: `http://localhost:3000`

### 4. Test the Application
- Open `http://localhost:3000` in your browser
- You should see the dashboard with sample data
- Click "Trigger Scrape" button in the backend API docs to fetch real data: `http://localhost:8000/docs`

## Docker Deployment

### Using Docker Compose
```bash
docker-compose up --build
```

This will start:
- Frontend on `http://localhost:3000`
- Backend on `http://localhost:8000`
- PostgreSQL database on `localhost:5432`

## API Documentation

### Get All Tariffs
```
GET /api/tariffs?country=US&hs_code=6204&skip=0&limit=100
```
**Response:**
```json
{
  "total": 150,
  "data": [
    {
      "id": 1,
      "country": "US",
      "hs_code": "6204.62.20",
      "product_description": "Women's cotton trousers",
      "rate": 16.5,
      "effective_date": "2024-01-01T00:00:00",
      "last_updated": "2024-12-11T00:00:00"
    }
  ]
}
```

### Get Recent Changes
```
GET /api/changes?country=US&days=7&skip=0&limit=100
```
**Response:**
```json
{
  "total": 5,
  "days": 7,
  "data": [
    {
      "id": 1,
      "country": "US",
      "hs_code": "6204.62.20",
      "old_rate": 15.0,
      "new_rate": 16.5,
      "change_date": "2024-12-10T00:00:00",
      "change_reason": "Updated from USITC"
    }
  ]
}
```

### Get Statistics
```
GET /api/stats
```
**Response:**
```json
{
  "us_tariffs": 1250,
  "china_tariffs": 1180,
  "total_tariffs": 2430,
  "recent_changes_7d": 15,
  "last_update": "2024-12-11T12:00:00"
}
```

### Trigger Manual Scrape
```
POST /api/trigger-scrape
```

## Production Deployment

### Option 1: Render.com
1. Push code to GitHub
2. Create new Web Services for both frontend and backend
3. Set environment variables
4. Deploy

### Option 2: AWS
1. Backend: Deploy to Elastic Beanstalk or EC2
2. Frontend: Deploy to S3 + CloudFront
3. Database: Use RDS PostgreSQL

### Option 3: Heroku
```bash
# Install Heroku CLI
heroku login
heroku create tariff-app-backend
git push heroku main
```

## Configuration

### Environment Variables

**Backend (.env):**
- `DATABASE_URL` - Database connection string
- `SCRAPE_HOUR` - Hour for daily scrape (0-23)
- `SCRAPE_MINUTE` - Minute for daily scrape (0-59)

**Frontend (.env):**
- `REACT_APP_API_URL` - Backend API URL

## Data Sources

### Current
- US Customs: USITC, USTR websites (currently using sample data)
- China Customs: China Customs website (currently using sample data)

### Next Steps to Implement Real Data
1. Create web scraping functions for USITC/USTR
2. Implement China Customs API integration
3. Add data validation and error handling
4. Set up alerts for significant changes

## Database Schema

### Tariffs Table
```sql
CREATE TABLE tariffs (
  id INTEGER PRIMARY KEY,
  country VARCHAR(50),
  hs_code VARCHAR(20),
  product_description TEXT,
  rate FLOAT,
  effective_date DATETIME,
  source_url VARCHAR(500),
  last_updated DATETIME
);
```

### Tariff History Table
```sql
CREATE TABLE tariff_history (
  id INTEGER PRIMARY KEY,
  tariff_id INTEGER,
  country VARCHAR(50),
  hs_code VARCHAR(20),
  old_rate FLOAT,
  new_rate FLOAT,
  change_date DATETIME,
  change_reason TEXT
);
```

## Troubleshooting

### Database Connection Issues
- Check DATABASE_URL in .env
- Ensure PostgreSQL is running
- Try switching to SQLite for development

### API Not Responding
- Check backend is running on port 8000
- Verify CORS configuration
- Check backend logs for errors

### Frontend Not Loading Data
- Check browser console for errors
- Verify REACT_APP_API_URL in .env
- Ensure backend API is accessible

## Contributing

To add real tariff data sources:
1. Implement scraper for new source in `scraper.py`
2. Add tests for new sources
3. Update `_save_tariffs()` to handle new fields
4. Document data source in README

## License

MIT

## Support

For issues or questions, please create an issue in the repository.
