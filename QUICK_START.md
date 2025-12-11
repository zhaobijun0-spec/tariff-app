# Quick Start Guide

## Option 1: Local Development (5 minutes)

### Prerequisites
- Python 3.11+
- Node.js 18+

### Backend Setup
```bash
cd backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy env file
cp .env.example .env

# Run server
python -m uvicorn main:app --reload
```
✅ Backend running on http://localhost:8000

### Frontend Setup (new terminal)
```bash
cd frontend

# Install dependencies
npm install

# Copy env file
cp .env.example .env

# Start development server
npm start
```
✅ Frontend running on http://localhost:3000

### Test It
- Open http://localhost:3000 in browser
- See dashboard with sample data
- Click tabs to explore (Tariffs, Changes)
- API docs available at http://localhost:8000/docs

---

## Option 2: Docker (2 minutes)

### Prerequisites
- Docker & Docker Compose

### Run Everything
```bash
docker-compose up --build
```

Wait for services to start:
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- Database: localhost:5432

---

## Option 3: Cloud Deployment (10 minutes)

### Deploy to Render.com (Easiest)

1. **Push code to GitHub**
   ```bash
   git push origin main
   ```

2. **Create Backend Service**
   - Go to https://dashboard.render.com
   - Click "New +" → "Web Service"
   - Connect GitHub
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn main:app --host 0.0.0.0`

3. **Create Database**
   - New +" → "PostgreSQL"
   - Copy connection string

4. **Create Frontend Service**
   - New +" → "Static Site"
   - Build: `cd frontend && npm install && npm run build`
   - Publish: `frontend/build`

✅ Live in minutes!

---

## Verify Installation

### Backend Check
```bash
curl http://localhost:8000/health
# Response: {"status":"healthy"}
```

### Frontend Check
Open http://localhost:3000 and see:
- Dashboard with stats
- Tariffs tab
- Changes tab

### API Check
```bash
curl http://localhost:8000/api/stats
# Response: {...statistics...}
```

---

## Next Steps

1. **Explore Data**
   - View sample tariff data
   - Check change history
   - Review statistics

2. **Configure Real Data** (Optional)
   - Update scraper.py with real tariff sources
   - Modify database.py for additional fields
   - Test with actual data

3. **Customize**
   - Add your branding
   - Change colors in App.css
   - Modify dashboard widgets

4. **Deploy**
   - Choose deployment platform (Render, AWS, etc.)
   - Follow deployment guide in DEPLOYMENT.md
   - Set up custom domain

---

## Troubleshooting

### Port Already in Use
```bash
# Kill process on port
lsof -ti:8000 | xargs kill -9   # Backend
lsof -ti:3000 | xargs kill -9   # Frontend
```

### Database Errors
- Check DATABASE_URL in .env
- Ensure PostgreSQL running
- Try SQLite (default)

### API Not Responding
- Check backend running: `curl localhost:8000/health`
- Check REACT_APP_API_URL in .env
- Look at browser console for errors

### Module Not Found
```bash
# Reinstall dependencies
pip install -r requirements.txt  # Backend
npm install                       # Frontend
```

---

## File Structure at a Glance

```
tariff-app/
├── backend/           # Python API
├── frontend/          # React UI
├── docker-compose.yml # Docker setup
├── README.md          # Full documentation
├── DEPLOYMENT.md      # How to deploy
└── QUICK_START.md     # This file
```

---

## Commands Reference

### Backend
```bash
# Development
cd backend
python -m uvicorn main:app --reload

# Production
gunicorn -w 4 -b 0.0.0.0:8000 main:app

# Install packages
pip install -r requirements.txt

# Add new package
pip install package-name
pip freeze > requirements.txt
```

### Frontend
```bash
# Development
cd frontend
npm start

# Production build
npm run build

# Install packages
npm install package-name

# Test
npm test
```

### Docker
```bash
# Start
docker-compose up

# Stop
docker-compose down

# View logs
docker-compose logs -f

# Rebuild
docker-compose up --build
```

---

## Getting Help

1. **Check Documentation**
   - README.md - Features & architecture
   - DEPLOYMENT.md - Production setup
   - PROJECT_STRUCTURE.md - Code organization

2. **Check Logs**
   - Backend: Check terminal running uvicorn
   - Frontend: Check browser console (F12)
   - Docker: `docker-compose logs service-name`

3. **Common Issues**
   - Database: Reset by deleting tariff_data.db
   - Ports: Change in .env if already in use
   - CORS: Check ALLOWED_ORIGINS in .env

---

## What's Next?

- ✅ Local development
- ✅ Understand architecture  
- ⬜ Deploy to cloud
- ⬜ Add real tariff data sources
- ⬜ Add authentication
- ⬜ Set up notifications

Start with local development, then move to deployment! 🚀
