# 🚀 Updated Installation Guide - With Charts

## What's New
✨ Professional charting with Recharts
✨ Trends visualization tab
✨ Interactive line/area/combined charts
✨ Real-time data tracking

## Prerequisites (Same as Before)
- Python 3.11+
- Node.js 18+
- Git

## Installation Steps

### Step 1: Backend Setup
```bash
cd /agent/home/tariff-app/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
```

### Step 2: Frontend Setup (NEW - With Chart Library)
```bash
cd /agent/home/tariff-app/frontend

# Install dependencies (includes new Recharts library)
npm install

# Copy environment file
cp .env.example .env
```

**New dependency installed:**
```json
"recharts": "^2.10.3"  ← For charts
```

### Step 3: Run the Application

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
python -m uvicorn main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```

### Step 4: Open in Browser
```
http://localhost:3000
```

### Step 5: Try the Charts
1. Click **"📈 Trends"** tab
2. See interactive chart
3. Try different types (Line/Area/Combined)
4. Filter by country (US/China/Both)

## Docker Setup (Alternative)

Same as before:
```bash
docker-compose up --build
```

Then open: `http://localhost:3000`

## Verify Installation

### Check Backend Health
```bash
curl http://localhost:8000/health
# Response: {"status":"healthy"}
```

### Check Chart API
```bash
curl http://localhost:8000/api/trends
# Response: {...chart data...}
```

### Check Frontend
- Open http://localhost:3000
- All 4 tabs visible: Dashboard, 📈 Trends, Tariffs, Changes
- Trends tab shows interactive chart

## What's Different from Before?

| Item | Before | After |
|------|--------|-------|
| Tabs | 3 | **4** (added Trends) |
| Dependencies | FastAPI, React | + **Recharts** |
| Database | Tariff, TariffHistory | + **TariffTrend** |
| API Endpoints | 3 | **4** (added /trends) |
| Features | List & Changes | + **Charts** |

## Troubleshooting

### "recharts not found" error
```bash
cd frontend
npm install recharts
npm start
```

### Chart not displaying
1. Check frontend console (F12)
2. Verify API: `curl http://localhost:8000/api/trends`
3. Check database has TariffTrend records

### Port already in use
```bash
# Kill existing process
lsof -ti:8000 | xargs kill -9   # Backend
lsof -ti:3000 | xargs kill -9   # Frontend
```

## Files to Know About

### New Files
- `frontend/components/TariffChart.jsx` - Chart component
- `CHARTS_GUIDE.md` - Complete chart documentation
- `CHART_UPDATE.md` - What's new overview

### Updated Files
- `frontend/App.jsx` - Added Trends tab
- `frontend/App.css` - Added chart styles
- `frontend/package.json` - Added Recharts
- `backend/main.py` - Added /api/trends
- `backend/database.py` - Added TariffTrend model
- `backend/scraper.py` - Now saves trend data

## Next Steps

### Immediate
1. ✅ Follow installation steps above
2. ✅ Run app
3. ✅ View charts

### Short Term
1. 📌 Read CHARTS_GUIDE.md
2. 📌 Connect real data sources
3. 📌 Customize styling

### Long Term
1. 🚀 Deploy to production
2. 🚀 Add alerts
3. 🚀 Generate reports

## Quick Commands

```bash
# Start Backend
cd backend && python -m uvicorn main:app --reload

# Start Frontend
cd frontend && npm start

# Install new dependency
cd frontend && npm install package-name

# Run Docker
docker-compose up --build

# Reset database
rm backend/tariff_data.db
```

## Documentation

- **README.md** - Features overview
- **QUICK_START.md** - 5-minute setup
- **CHARTS_GUIDE.md** - ✨ NEW - Chart details
- **DEPLOYMENT.md** - Production guide
- **PROJECT_STRUCTURE.md** - Code organization

---

**Everything is set up! Time to see those beautiful charts in action.** 📊
