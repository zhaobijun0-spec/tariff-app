# 🚀 Deploy to AWS

Deploy on Amazon's powerful infrastructure.

## Prerequisites
- AWS Account
- AWS CLI installed
- IAM user with permissions

## Step 1: Setup Backend on EC2

### Launch EC2 Instance
```bash
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t3.micro \
  --key-name your-key
```

### SSH into Instance
```bash
ssh -i your-key.pem ec2-user@your-instance-ip
```

### Install Dependencies
```bash
sudo yum update -y
sudo yum install python3 python3-pip git -y
```

### Clone and Setup
```bash
git clone https://github.com/YOUR_USERNAME/tariff-app.git
cd tariff-app/backend

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start with systemd
sudo nano /etc/systemd/system/tariff-api.service
```

### Systemd Service File
```ini
[Unit]
Description=Tariff API
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user/tariff-app/backend
ExecStart=/home/ec2-user/tariff-app/backend/venv/bin/uvicorn main:app --host 0.0.0.0

[Install]
WantedBy=multi-user.target
```

Start service:
```bash
sudo systemctl enable tariff-api
sudo systemctl start tariff-api
```

## Step 2: Deploy Frontend

### Setup S3 + CloudFront

1. Create S3 bucket:
```bash
aws s3 mb s3://tariff-app-frontend
```

2. Build frontend:
```bash
cd tariff-app/frontend
npm install
npm run build
```

3. Upload to S3:
```bash
aws s3 sync build/ s3://tariff-app-frontend/
```

4. Create CloudFront distribution
5. Point to S3 bucket

## Step 3: Database

### RDS PostgreSQL
```bash
aws rds create-db-instance \
  --db-instance-identifier tariff-db \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --master-username admin
```

## Step 4: Security Groups

Allow traffic:
- Port 80 (HTTP)
- Port 443 (HTTPS)
- Port 5432 (PostgreSQL)

## Step 5: SSL Certificate

Use AWS Certificate Manager (free!)

## Costs
- EC2 t3.micro: ~$9/month
- RDS t3.micro: ~$15/month
- S3: ~$1/month
- **Total**: ~$25/month

## Commands Summary

```bash
# View instances
aws ec2 describe-instances

# View databases
aws rds describe-db-instances

# View S3 buckets
aws s3 ls

# Monitor CloudWatch
aws cloudwatch get-metric-statistics ...
```

---

See also: `DEPLOY_RENDER.md`, `DEPLOY_RAILWAY.md`, `DEPLOY_HEROKU.md`
