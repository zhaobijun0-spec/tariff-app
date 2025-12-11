from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import desc, and_
from datetime import datetime, timedelta
from database import get_db, Tariff, TariffHistory, TariffTrend
from scraper import run_daily_scrape
from apscheduler.schedulers.background import BackgroundScheduler
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Tariff Dashboard API",
    description="API for US and China tariff rate tracking",
    version="1.0.0"
)

# Add CORS middleware for web access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize scheduler for daily scraping
scheduler = BackgroundScheduler()

@app.on_event("startup")
def start_scheduler():
    """Start the background scheduler for daily tariff updates"""
    def daily_job():
        db = next(get_db())
        try:
            run_daily_scrape(db)
        except Exception as e:
            logger.error(f"Error in daily scrape job: {str(e)}")
    
    scheduler.add_job(daily_job, "cron", hour=0, minute=0)  # Run at midnight daily
    scheduler.start()
    logger.info("Scheduler started")

@app.on_event("shutdown")
def stop_scheduler():
    scheduler.shutdown()

# Routes
@app.get("/")
async def root():
    return {
        "message": "Tariff Dashboard API",
        "version": "1.0.0",
        "endpoints": {
            "tariffs": "/api/tariffs",
            "changes": "/api/changes",
            "trends": "/api/trends",
            "stats": "/api/stats",
            "health": "/health"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/api/tariffs")
async def get_tariffs(
    country: str = Query(None, description="Filter by country: US or China"),
    hs_code: str = Query(None, description="Filter by HS code"),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get tariff rates"""
    query = db.query(Tariff)
    
    if country:
        query = query.filter(Tariff.country == country.upper())
    
    if hs_code:
        query = query.filter(Tariff.hs_code.contains(hs_code))
    
    total = query.count()
    tariffs = query.order_by(desc(Tariff.last_updated)).offset(skip).limit(limit).all()
    
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": [
            {
                "id": t.id,
                "country": t.country,
                "hs_code": t.hs_code,
                "product_description": t.product_description,
                "rate": t.rate,
                "effective_date": t.effective_date,
                "last_updated": t.last_updated
            }
            for t in tariffs
        ]
    }

@app.get("/api/changes")
async def get_tariff_changes(
    days: int = Query(7, description="Number of days to look back"),
    country: str = Query(None, description="Filter by country: US or China"),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get recent tariff changes"""
    cutoff_date = datetime.utcnow() - timedelta(days=days)
    query = db.query(TariffHistory).filter(TariffHistory.change_date >= cutoff_date)
    
    if country:
        query = query.filter(TariffHistory.country == country.upper())
    
    total = query.count()
    changes = query.order_by(desc(TariffHistory.change_date)).offset(skip).limit(limit).all()
    
    return {
        "total": total,
        "days": days,
        "skip": skip,
        "limit": limit,
        "data": [
            {
                "id": c.id,
                "country": c.country,
                "hs_code": c.hs_code,
                "old_rate": c.old_rate,
                "new_rate": c.new_rate,
                "change_date": c.change_date,
                "change_reason": c.change_reason
            }
            for c in changes
        ]
    }

@app.get("/api/trends")
async def get_tariff_trends(
    country: str = Query(None, description="Filter by country: US or China"),
    hs_code: str = Query(None, description="Filter by HS code"),
    days: int = Query(90, description="Number of days to look back"),
    db: Session = Depends(get_db)
):
    """Get historical tariff trends for charting"""
    cutoff_date = datetime.utcnow() - timedelta(days=days)
    query = db.query(TariffTrend).filter(TariffTrend.record_date >= cutoff_date)
    
    if country:
        query = query.filter(TariffTrend.country == country.upper())
    
    if hs_code:
        query = query.filter(TariffTrend.hs_code == hs_code)
    
    trends = query.order_by(TariffTrend.record_date).all()
    
    # Group by date for chart display
    grouped_data = {}
    for trend in trends:
        date_key = trend.record_date.strftime("%Y-%m-%d")
        if date_key not in grouped_data:
            grouped_data[date_key] = {
                "date": date_key,
                "us_rate": None,
                "china_rate": None,
                "rates": {}
            }
        
        if trend.country == "US":
            grouped_data[date_key]["us_rate"] = trend.rate
        elif trend.country == "China":
            grouped_data[date_key]["china_rate"] = trend.rate
        
        code_key = f"{trend.country}_{trend.hs_code}"
        grouped_data[date_key]["rates"][code_key] = {
            "rate": trend.rate,
            "product": trend.product_description
        }
    
    return {
        "country": country,
        "hs_code": hs_code,
        "days": days,
        "data": sorted(grouped_data.values(), key=lambda x: x["date"])
    }

@app.get("/api/stats")
async def get_stats(db: Session = Depends(get_db)):
    """Get dashboard statistics"""
    us_count = db.query(Tariff).filter(Tariff.country == "US").count()
    china_count = db.query(Tariff).filter(Tariff.country == "China").count()
    recent_changes = db.query(TariffHistory).filter(
        TariffHistory.change_date >= datetime.utcnow() - timedelta(days=7)
    ).count()
    
    return {
        "us_tariffs": us_count,
        "china_tariffs": china_count,
        "total_tariffs": us_count + china_count,
        "recent_changes_7d": recent_changes,
        "last_update": datetime.utcnow()
    }

@app.post("/api/trigger-scrape")
async def trigger_scrape(db: Session = Depends(get_db)):
    """Manually trigger a tariff scrape (admin only)"""
    count = run_daily_scrape(db)
    return {
        "status": "success",
        "tariffs_processed": count,
        "timestamp": datetime.utcnow()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
