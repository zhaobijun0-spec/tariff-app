from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Use SQLite for simplicity (can switch to PostgreSQL later)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./tariff_data.db")

if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Tariff(Base):
    __tablename__ = "tariffs"
    
    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, index=True)  # "US" or "China"
    hs_code = Column(String, index=True)  # Product code
    product_description = Column(Text)
    rate = Column(Float)  # Tariff rate
    effective_date = Column(DateTime)
    source_url = Column(String)
    last_updated = Column(DateTime, default=datetime.utcnow)
    
    __table_args__ = (
        Index('idx_country_hs_code', 'country', 'hs_code'),
        Index('idx_effective_date', 'effective_date'),
    )

class TariffHistory(Base):
    __tablename__ = "tariff_history"
    
    id = Column(Integer, primary_key=True, index=True)
    tariff_id = Column(Integer, index=True)
    country = Column(String, index=True)
    hs_code = Column(String, index=True)
    old_rate = Column(Float)
    new_rate = Column(Float)
    change_date = Column(DateTime, default=datetime.utcnow)
    change_reason = Column(Text)

class TariffTrend(Base):
    __tablename__ = "tariff_trends"
    
    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, index=True)  # "US" or "China"
    hs_code = Column(String, index=True)
    product_description = Column(Text)
    rate = Column(Float)  # Historical rate
    record_date = Column(DateTime, index=True)  # When this rate was recorded
    created_at = Column(DateTime, default=datetime.utcnow)
    
    __table_args__ = (
        Index('idx_country_date', 'country', 'record_date'),
        Index('idx_hs_code_date', 'hs_code', 'record_date'),
    )

# Create tables
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
