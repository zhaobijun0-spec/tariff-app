# 🚀 Deploy to Heroku (Classic)

Heroku is simple but now requires paid plans.

## Prerequisites
- GitHub account
- Heroku account
- Heroku CLI installed

## Step 1: Install Heroku CLI

```bash
npm install -g heroku
heroku login
```

## Step 2: Create App

```bash
heroku create tariff-app-backend
heroku create tariff-app-frontend
```

## Step 3: Deploy Backend

### Add Procfile
```
web: cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
```

### Add Runtime.txt
```
python-3.11.6
```

### Push to Heroku
```bash
heroku git:remote -a tariff-app-backend
git push heroku main
```

### Set Environment Variables
```bash
heroku config:set DATABASE_URL=postgresql://...
heroku logs --tail
```

## Step 4: Deploy Frontend

### Build and Deploy
```bash
cd frontend
npm run build
heroku create tariff-app-frontend
git subtree push --prefix frontend heroku main
```

## Step 5: Add Database

```bash
heroku addons:create heroku-postgresql:hobby-dev
```

## Step 6: Update Configuration

Backend CORS:
```python
origins = ["https://tariff-app-frontend.herokuapp.com"]
```

Frontend env:
```
REACT_APP_API_URL=https://tariff-app-backend.herokuapp.com
```

## Costs
- **Hobby (free)**: No longer available
- **Starter**: $7/month per dyno
- **Standard**: $50/month per dyno

## Alternatives
Since Heroku removed free tier, consider:
- ✅ Render (better value)
- ✅ Railway (modern)
- ✅ AWS (powerful)
- ✅ DigitalOcean (simple)

---

See also: `DEPLOY_RENDER.md`, `DEPLOY_RAILWAY.md`, `DEPLOY_AWS.md`
