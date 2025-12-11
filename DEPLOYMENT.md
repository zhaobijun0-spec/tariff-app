# Deployment Guide

## Production Deployment Options

### 1. Render.com (Easiest - Recommended for Getting Started)

#### Prerequisites
- GitHub account with code pushed
- Render.com account (free tier available)

#### Steps

1. **Create Backend Service**
   - Go to dashboard.render.com
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Configuration:
     - Name: `tariff-api`
     - Environment: `Python 3`
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `uvicorn main:app --host 0.0.0.0`
     - Add Environment Variables:
       - `DATABASE_URL`: `postgresql://...` (use Render's PostgreSQL)
   - Deploy

2. **Create Database**
   - Click "New +" → "PostgreSQL"
   - Name: `tariff-db`
   - Copy connection string to backend's `DATABASE_URL`

3. **Create Frontend Service**
   - Click "New +" → "Static Site"
   - Connect your GitHub repo
   - Configuration:
     - Name: `tariff-dashboard`
     - Build Command: `cd frontend && npm install && npm run build`
     - Publish Directory: `frontend/build`
   - Add Environment Variable:
     - `REACT_APP_API_URL`: `https://tariff-api.onrender.com`
   - Deploy

#### Cost
- Free tier available (with limitations)
- Production: ~$7-12/month

---

### 2. Railway.app

1. **Connect GitHub Repository**
   - Go to railway.app
   - Click "New Project" → "Deploy from GitHub"
   - Select your repository

2. **Configure Services**
   - Railway auto-detects services
   - Set environment variables:
     - Backend: `DATABASE_URL`, `API_PORT`
     - Frontend: `REACT_APP_API_URL`

3. **Deploy**
   - Railway automatically deploys on push

#### Cost
- Free tier: $5 credit/month
- Production: Pay-as-you-go (~$0.10/hour for basic setup)

---

### 3. AWS Deployment

#### Backend (Elastic Beanstalk)
```bash
# Install EB CLI
pip install awsebcli

# Initialize EB
eb init -p python-3.11 tariff-app

# Create environment
eb create tariff-api-env

# Deploy
eb deploy

# View logs
eb logs
```

#### Frontend (S3 + CloudFront)
```bash
# Build
cd frontend
npm run build

# Create S3 bucket
aws s3 mb s3://tariff-dashboard

# Upload
aws s3 sync build/ s3://tariff-dashboard

# Create CloudFront distribution (via AWS Console)
```

#### Database (RDS)
1. Go to AWS RDS Console
2. Create PostgreSQL instance
3. Note endpoint
4. Update `DATABASE_URL` in EB environment variables

---

### 4. Docker on VPS (DigitalOcean, Linode, etc.)

#### Prerequisites
- VPS with Docker installed
- Domain name

#### Steps

```bash
# SSH to your VPS
ssh root@your-vps-ip

# Clone repo
git clone https://github.com/yourusername/tariff-app.git
cd tariff-app

# Create .env files
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# Edit .env with production values
nano backend/.env
nano frontend/.env

# Build and run
docker-compose -f docker-compose.prod.yml up -d

# Set up Nginx reverse proxy
# (See nginx.conf example)
```

#### Nginx Configuration
Create `/etc/nginx/sites-available/tariff-app`:
```nginx
upstream backend {
    server localhost:8000;
}

server {
    listen 80;
    server_name tariff.yourdomain.com;

    # Redirect to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name tariff.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/tariff.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/tariff.yourdomain.com/privkey.pem;

    location /api {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location / {
        root /var/www/tariff-app/frontend/build;
        try_files $uri /index.html;
    }
}
```

#### Cost
- DigitalOcean: $4-6/month (basic VPS)
- Linode: $5+/month

---

## Environment Variables Checklist

Before deploying, ensure these are set:

### Backend
- [ ] `DATABASE_URL` - PostgreSQL connection string
- [ ] `API_HOST` - 0.0.0.0 for cloud
- [ ] `API_PORT` - 8000
- [ ] `ALLOWED_ORIGINS` - Your frontend domain

### Frontend
- [ ] `REACT_APP_API_URL` - Your backend API URL (with https://)

---

## SSL/TLS Certificates

### Using Let's Encrypt (Free)
```bash
# Install certbot
sudo apt-get install certbot python3-certbot-nginx

# Generate certificate
sudo certbot certonly --nginx -d tariff.yourdomain.com

# Auto-renewal
sudo systemctl enable certbot.timer
```

### Render.com/Railway.app
- Automatically provides HTTPS certificates

### AWS
- Use ACM (AWS Certificate Manager) - Free

---

## Monitoring & Logging

### Backend Health Check
```bash
curl https://your-backend.com/health
```

### View Logs
- **Render**: Logs tab in dashboard
- **Railway**: Logs tab in service
- **AWS EB**: `eb logs`
- **Docker/VPS**: `docker logs container-name`

### Set Up Alerts
- Configure monitoring in Render/Railway dashboard
- Set up CloudWatch alarms in AWS
- Use Sentry for error tracking

---

## Updating Code

### Push Updates
```bash
git push origin main
```

- **Render/Railway**: Auto-deploys
- **Docker/VPS**: Manual pull & rebuild
  ```bash
  cd /path/to/tariff-app
  git pull
  docker-compose up -d --build
  ```

---

## Troubleshooting

### Frontend shows "Cannot connect to API"
- Check `REACT_APP_API_URL` is correct
- Ensure backend API is accessible
- Check CORS settings in backend

### Database connection errors
- Verify `DATABASE_URL` format
- Ensure database is running and accessible
- Check firewall rules allow connection

### High memory/CPU usage
- Check database query performance
- Limit API response sizes
- Use caching

---

## Cost Comparison

| Platform | Setup | Monthly | Notes |
|----------|-------|---------|-------|
| Render | Easy | $7-12 | Best for beginners |
| Railway | Easy | $5+ | Good balance |
| AWS | Medium | $10-20 | Most scalable |
| DigitalOcean | Medium | $4-6 | Good for full control |

---

## Next Steps After Deployment

1. **Enable HTTPS** - Use Let's Encrypt or cloud provider
2. **Set up monitoring** - Monitor uptime and errors
3. **Configure backups** - Daily database backups
4. **Implement real data sources** - Connect to actual tariff APIs
5. **Add authentication** - For premium features
6. **Set up CI/CD** - Automated testing and deployment

