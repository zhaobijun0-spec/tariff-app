import requests
from bs4 import BeautifulSoup
from datetime import datetime
from sqlalchemy.orm import Session
from database import Tariff, TariffHistory, TariffTrend
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TariffScraper:
    """Scrapes tariff data from US and China customs sources"""
    
    def __init__(self):
        self.us_sources = {
            "usitc": "https://www.usitc.gov/trade_remedy/731_investigations/731_investigations.htm",
            "ustr": "https://ustr.gov/issue-areas/trade-agreements"
        }
        self.china_sources = {
            "cccn": "http://cccn.customs.gov.cn/"
        }
    
    def fetch_us_tariffs(self, db: Session):
        """Fetch US tariff data from USITC and USTR"""
        logger.info("Fetching US tariff data...")
        
        try:
            # This is a placeholder - actual implementation would parse real tariff data
            # For now, we'll create sample data to demonstrate the system
            us_data = [
                {
                    "hs_code": "6204.62.20",
                    "description": "Women's cotton trousers",
                    "rate": 16.5,
                    "source": "USITC"
                },
                {
                    "hs_code": "8471.30.00",
                    "description": "Automatic data processing machines",
                    "rate": 0.0,
                    "source": "USTR"
                }
            ]
            
            self._save_tariffs(db, us_data, "US")
            logger.info(f"Successfully fetched {len(us_data)} US tariffs")
            return len(us_data)
        except Exception as e:
            logger.error(f"Error fetching US tariffs: {str(e)}")
            return 0
    
    def fetch_china_tariffs(self, db: Session):
        """Fetch China tariff data from China Customs"""
        logger.info("Fetching China tariff data...")
        
        try:
            # Placeholder for China tariff data
            china_data = [
                {
                    "hs_code": "6204.62.20",
                    "description": "Women's cotton trousers",
                    "rate": 12.0,
                    "source": "China Customs"
                },
                {
                    "hs_code": "8471.30.00",
                    "description": "Automatic data processing machines",
                    "rate": 0.0,
                    "source": "China Customs"
                }
            ]
            
            self._save_tariffs(db, china_data, "China")
            logger.info(f"Successfully fetched {len(china_data)} China tariffs")
            return len(china_data)
        except Exception as e:
            logger.error(f"Error fetching China tariffs: {str(e)}")
            return 0
    
    def _save_tariffs(self, db: Session, data: list, country: str):
        """Save tariff data and track changes"""
        for item in data:
            existing = db.query(Tariff).filter(
                Tariff.country == country,
                Tariff.hs_code == item["hs_code"]
            ).first()
            
            if existing:
                # Check if rate changed
                if existing.rate != item["rate"]:
                    history = TariffHistory(
                        tariff_id=existing.id,
                        country=country,
                        hs_code=item["hs_code"],
                        old_rate=existing.rate,
                        new_rate=item["rate"],
                        change_reason=f"Updated from {item['source']}"
                    )
                    db.add(history)
                    existing.rate = item["rate"]
                    existing.last_updated = datetime.utcnow()
            else:
                # New tariff
                tariff = Tariff(
                    country=country,
                    hs_code=item["hs_code"],
                    product_description=item["description"],
                    rate=item["rate"],
                    effective_date=datetime.utcnow(),
                    source_url=item.get("source", "")
                )
                db.add(tariff)
            
            # Save trend data for charting
            trend = TariffTrend(
                country=country,
                hs_code=item["hs_code"],
                product_description=item["description"],
                rate=item["rate"],
                record_date=datetime.utcnow()
            )
            db.add(trend)
            db.commit()

def run_daily_scrape(db: Session):
    """Run the daily tariff scrape job"""
    scraper = TariffScraper()
    us_count = scraper.fetch_us_tariffs(db)
    china_count = scraper.fetch_china_tariffs(db)
    logger.info(f"Daily scrape completed: {us_count} US + {china_count} China tariffs")
    return us_count + china_count
