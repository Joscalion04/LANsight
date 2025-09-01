from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from app.database import Base

class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String, unique=True, index=True, nullable=False)
    mac = Column(String, unique=True, index=True, nullable=False)
    hostname = Column(String, index=True)
    last_seen = Column(DateTime, default=datetime.utcnow)
    suspicious = Column(Boolean, default=False)
