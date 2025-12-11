# 🚀 Deploy to Render.com

Render is the easiest way to deploy your app (free tier available).

## Prerequisites
- GitHub account with code pushed
- Render account (free at render.com)

## Step 1: Prepare Your Code

### Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/tariff-app.git
git push -u origin main
```

## Step 2: Deploy Backend

### Create Backend Service
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Fill in details:
   - **Name**: tariff-app-backend
   - **Environment**: Python 3.11
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0`
   - **Plan**: Free (or Starter)

### Set Environment Variables
1. In Service Settings → Environment
2. Add:
   ```
   DATABASE_URL=postgresql://user:pass@host/dbname
   PYTHON_VERSION=3.11
   ```

### Create Database (Optional)
If using PostgreSQL:
1. Click **"New +"** → **"PostgreSQL"**
2. Create database
3. Copy connection string to `DATABASE_URL`

## Step 3: Deploy Frontend

### Create Frontend Service
1. Click **"New +"** → **"Static Site"**
2. Connect your GitHub repository
3. Fill in details:
   - **Name**: tariff-app-frontend
   - **Build Command**: `cd frontend && npm install && npm run build`
   - **Publish Directory**: `frontend/build`

### Set Environment Variables
1. In Static Site Settings → Environment
2. Add:
   ```
   REACT_APP_API_URL=https://tariff-app-backend.onrender.com
   ```

(Replace with your actual backend URL)

## Step 4: Configure CORS

Update backend `main.py`:
```python
origins = [
    "https://tariff-app-frontend.onrender.com",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Step 5: Monitor Deployment

1. Watch logs in Render Dashboard
2. Check service health
3. Test frontend → backend connection

## URLs
- **Backend**: `https://tariff-app-backend.onrender.com`
- **Frontend**: `https://tariff-app-frontend.onrender.com`

## Troubleshooting

### Build Failed
- Check build logs in Render
- Ensure `requirements.txt` exists
- Check Python version compatibility

### CORS Errors
- Verify `REACT_APP_API_URL` environment variable
- Update CORS origins in backend
- Redeploy both services

### Database Connection
- Verify `DATABASE_URL` is set correctly
- Check database credentials
- Test connection string locally first

## Costs
- **Free Tier**: Limited but functional
- **Starter**: $7/month for persistent services
- **Pro**: Scale as needed

## Benefits
✅ Easy deployment
✅ Free tier available
✅ Auto HTTPS
✅ Environment variables
✅ Zero configuration
✅ Deploy from GitHub

---

See also: `DEPLOY_RAILWAY.md`, `DEPLOY_AWS.md`, `DEPLOY_HEROKU.md`
