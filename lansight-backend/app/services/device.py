from sqlalchemy.orm import Session
from app.models.device import Device
from app.schemas.device import DeviceCreate, DeviceUpdate
from datetime import datetime

def get_all_devices(db: Session):
    return db.query(Device).all()

def get_device_by_id(db: Session, device_id: int):
    return db.query(Device).filter(Device.id == device_id).first()

def create_device(db: Session, device: DeviceCreate):
    db_device = Device(**device.dict())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

def update_device(db: Session, device_id: int, device: DeviceUpdate):
    db_device = db.query(Device).filter(Device.id == device_id).first()
    if not db_device:
        return None
    for key, value in device.dict(exclude_unset=True).items():
        setattr(db_device, key, value)
    db_device.last_seen = datetime.utcnow()
    db.commit()
    db.refresh(db_device)
    return db_device

def delete_device(db: Session, device_id: int):
    db_device = db.query(Device).filter(Device.id == device_id).first()
    if not db_device:
        return None
    db.delete(db_device)
    db.commit()
    return db_device
