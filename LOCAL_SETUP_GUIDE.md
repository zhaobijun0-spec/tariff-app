# 🚀 Local Development Setup - Complete Guide

This guide will get you running locally in 5 minutes!

## Prerequisites

### Check You Have These
```bash
python3 --version        # Should be 3.11+
node --version          # Should be 18+
npm --version           # Should be 9+
git --version           # Any recent version
```

If missing, install from:
- Python: https://www.python.org/downloads/
- Node.js: https://nodejs.org/

## Step 1: Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/tariff-app.git
cd tariff-app
```

## Step 2: Backend Setup (5 minutes)

### Navigate to backend
```bash
cd backend
```

### Create virtual environment
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Copy environment file
```bash
cp .env.example .env
# Edit .env if needed (optional for local development)
```

### Start backend server
```bash
python -m uvicorn main:app --reload
```

✅ Backend running at: `http://localhost:8000`

Test it:
```bash
curl http://localhost:8000/health
# Should respond: {"status":"healthy"}
```

## Step 3: Frontend Setup (5 minutes)

### In NEW terminal, navigate to frontend
```bash
cd tariff-app/frontend
```

### Install dependencies (includes Recharts for charts)
```bash
npm install
```

This installs:
- React
- Axios (API calls)
- Recharts (charting library) ✨
- And more...

### Copy environment file
```bash
cp .env.example .env
# For local development, default settings work fine
```

### Start frontend server
```bash
npm start
```

✅ Frontend running at: `http://localhost:3000`

Browser should auto-open!

## Step 4: Verify Everything Works

### Checklist
- [ ] Backend shows "Uvicorn running on" message
- [ ] Frontend shows compilation complete
- [ ] Browser opened to http://localhost:3000
- [ ] No red errors in browser console

### Test Dashboard
1. Click **"Dashboard"** tab
2. Should show 4 stats cards
3. Status should show "healthy"

### Test Charts ✨
1. Click **"📈 Trends"** tab
2. Should see interactive chart
3. Try switching chart types (Line → Area → Combined)
4. Try filtering (US vs China → US Only → China Only)

### Test API
```bash
# In another terminal
curl http://localhost:8000/api/stats
# Should return JSON with tariff counts
```

## Common Issues & Solutions

### Port Already in Use

**Error**: `Address already in use`

**Solution**:
```bash
# Kill existing process
# macOS/Linux
lsof -ti:8000 | xargs kill -9   # Backend
lsof -ti:3000 | xargs kill -9   # Frontend

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Dependencies Won't Install

**Error**: `pip install failed` or `npm install failed`

**Solution**:
```bash
# Backend
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Frontend
rm -rf node_modules
npm cache clean --force
npm install
```

### Module Not Found Errors

**Error**: `ModuleNotFoundError: No module named 'fastapi'`

**Solution**:
```bash
# Make sure venv is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall
pip install -r requirements.txt
```

### CORS Errors

**Error**: `Cross-Origin Request Blocked`

**Solution**:
- Ensure backend is running: `http://localhost:8000`
- Frontend environment variable correct: `REACT_APP_API_URL=http://localhost:8000`
- Check backend `.env` has CORS enabled

### Chart Not Displaying

**Error**: Chart tab shows blank

**Solution**:
```bash
# Make sure Recharts installed
npm list recharts

# Should show: recharts@2.10.3 or higher

# If not installed
npm install recharts

# Restart frontend
npm start
```

## Development Workflow

### Making Changes

#### Backend Changes
1. Edit files in `backend/`
2. Restart auto-reloads with `--reload` flag
3. Changes take effect immediately

#### Frontend Changes
1. Edit files in `frontend/`
2. React auto-reloads
3. Changes appear in browser immediately

#### Database Changes
```bash
# Reset database (clears all data)
rm backend/tariff_data.db

# Restart backend to create fresh database
# Backend will auto-create tables
```

### Testing API

#### Using curl
```bash
# Get all tariffs
curl http://localhost:8000/api/tariffs

# Get changes in last 7 days
curl "http://localhost:8000/api/changes?days=7"

# Get trends for charting
curl "http://localhost:8000/api/trends?days=90"

# Get stats
curl http://localhost:8000/api/stats
```

#### Using Swagger UI
1. Open: `http://localhost:8000/docs`
2. Try different endpoints
3. See request/response examples

## File Structure During Development

```
tariff-app/
├── backend/
│   ├── venv/              ← Virtual environment (created)
│   ├── main.py            ← API server
│   ├── database.py        ← Database models
│   ├── scraper.py         ← Data fetching
│   ├── requirements.txt    ← Python dependencies
│   └── .env               ← Configuration (created)
├── frontend/
│   ├── node_modules/      ← Dependencies (created)
│   ├── components/        ← React components
│   ├── App.jsx            ← Main app
│   ├── App.css            ← Styles
│   ├── package.json       ← JS dependencies
│   └── .env               ← Configuration (created)
└── documentation files
```

## Useful Commands

### Backend

```bash
# Start development server
cd backend
source venv/bin/activate
python -m uvicorn main:app --reload

# View API documentation
open http://localhost:8000/docs

# Check database
sqlite3 tariff_data.db
.tables
.quit

# Run scraper manually
python
from scraper import run_daily_scrape
from database import SessionLocal
db = SessionLocal()
run_daily_scrape(db)
```

### Frontend

```bash
# Start development server
cd frontend
npm start

# Build for production
npm run build

# Run tests
npm test

# Format code
npm run format

# Check dependencies
npm list
npm outdated
```

## Testing Different Scenarios

### Test with Real Data
```bash
# Import real_data_scraper
cd backend
python
from real_data_scraper import fetch_all_real_tariffs
from database import SessionLocal
db = SessionLocal()
fetch_all_real_tariffs(db)
```

### Test Different Chart Types
1. Go to 📈 Trends tab
2. Try each chart type:
   - Line Chart
   - Area Chart
   - Combined Chart

### Test Filters
1. Try "US Only" view
2. Try "China Only" view
3. Try "US vs China" view
4. Change date range

## Performance Tips

### Speed Up npm install
```bash
npm install --legacy-peer-deps
```

### Speed Up pip install
```bash
pip install --cache-dir ~/.pip-cache -r requirements.txt
```

### Clear Cache
```bash
npm cache clean --force
pip cache purge
```

## Git Workflow

### First Time
```bash
cd tariff-app
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/tariff-app.git
git push -u origin main
```

### Regular Development
```bash
git add .
git commit -m "Description of changes"
git push origin main
```

### Pull Changes
```bash
git pull origin main
npm install  # Update dependencies
pip install -r backend/requirements.txt
```

## Next Steps

### Immediate
- ✅ Get it running locally
- ✅ Explore the dashboard
- ✅ View sample data in charts

### Short Term
1. Connect real tariff data
2. Customize chart themes
3. Add more product categories

### Medium Term
1. Deploy to cloud
2. Set up automated updates
3. Add email alerts

### Long Term
1. Add user accounts
2. Implement advanced analytics
3. Create API for third parties

## Environment Variables

### Backend (.env)
```bash
# Database
DATABASE_URL=sqlite:///./tariff_data.db

# For production
# DATABASE_URL=postgresql://user:pass@host:5432/dbname

# API
API_HOST=localhost
API_PORT=8000

# Logging
LOG_LEVEL=INFO
```

### Frontend (.env)
```bash
# API URL
REACT_APP_API_URL=http://localhost:8000

# For production
# REACT_APP_API_URL=https://api.tariffapp.com
```

## Troubleshooting Checklist

- [ ] Python 3.11+ installed
- [ ] Node 18+ installed
- [ ] venv activated (backend)
- [ ] dependencies installed
- [ ] .env files created
- [ ] ports 8000 and 3000 available
- [ ] no errors in terminal
- [ ] browser shows dashboard
- [ ] chart displays on Trends tab

## Support

See detailed documentation:
- `README.md` - Features overview
- `CHARTS_GUIDE.md` - Chart details
- `DEPLOYMENT.md` - Deploy to cloud
- `PROJECT_STRUCTURE.md` - Code organization

## Quick Restart

Forgot how to start?

```bash
# Terminal 1 - Backend
cd tariff-app/backend
source venv/bin/activate  # Windows: venv\Scripts\activate
python -m uvicorn main:app --reload

# Terminal 2 - Frontend
cd tariff-app/frontend
npm start

# Open browser
open http://localhost:3000
```

---

**You're ready to develop!** 🎉

Questions? Check the docs or create an issue on GitHub.
