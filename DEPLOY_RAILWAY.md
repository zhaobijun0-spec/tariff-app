# 🚀 Deploy to Railway.app

Railway is modern, fast, and beginner-friendly.

## Prerequisites
- GitHub account
- Railway account (free at railway.app)

## Step 1: Setup GitHub

Push your code:
```bash
git push origin main
```

## Step 2: Deploy with Railway

### Connect GitHub
1. Go to [Railway Dashboard](https://railway.app)
2. Click **"New Project"**
3. Select **"GitHub Repo"**
4. Authorize and select your repository

## Step 3: Configure Services

### Backend Service
1. Create new service from your repo
2. Add environment variables:
   ```
   ENVIRONMENT=production
   DATABASE_URL=postgresql://...
   ```
3. Set start command:
   ```
   cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

### Frontend Service
1. Create new service
2. Build command:
   ```
   cd frontend && npm install && npm run build
   ```
3. Environment variables:
   ```
   REACT_APP_API_URL=https://backend-url.railway.app
   ```

## Step 4: Add Database

### PostgreSQL
1. Click **"Add"** → **"Database"** → **"PostgreSQL"**
2. Copy connection string
3. Add as `DATABASE_URL` to backend service

## Step 5: Deploy

1. Railway auto-deploys on git push
2. Monitor in dashboard
3. Check service health

## URLs Generated
- Backend: `https://backend-xxxx.railway.app`
- Frontend: `https://frontend-xxxx.railway.app`

## Tips

### Auto-Deploy
Every git push automatically deploys!

### Environment Variables
Easy to manage in Railway dashboard

### Scaling
Simple scaling up if needed

## Costs
- **Free**: Limited compute hours
- **Pro**: Pay as you go (~$5/month for basic setup)

---

See also: `DEPLOY_RENDER.md`, `DEPLOY_AWS.md`, `DEPLOY_HEROKU.md`
