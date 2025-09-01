from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.device import Device, DeviceCreate, DeviceUpdate
from app.services import device as device_service
from app.database import get_db

router = APIRouter(prefix="/devices", tags=["Devices"])

@router.get("/", response_model=list[Device])
def read_devices(db: Session = Depends(get_db)):
    return device_service.get_all_devices(db)

@router.get("/{device_id}", response_model=Device)
def read_device(device_id: int, db: Session = Depends(get_db)):
    db_device = device_service.get_device_by_id(db, device_id)
    if not db_device:
        raise HTTPException(status_code=404, detail="Device not found")
    return db_device

@router.post("/", response_model=Device)
def create_device(device: DeviceCreate, db: Session = Depends(get_db)):
    return device_service.create_device(db, device)

@router.put("/{device_id}", response_model=Device)
def update_device(device_id: int, device: DeviceUpdate, db: Session = Depends(get_db)):
    db_device = device_service.update_device(db, device_id, device)
    if not db_device:
        raise HTTPException(status_code=404, detail="Device not found")
    return db_device

@router.delete("/{device_id}", response_model=Device)
def delete_device(device_id: int, db: Session = Depends(get_db)):
    db_device = device_service.delete_device(db, device_id)
    if not db_device:
        raise HTTPException(status_code=404, detail="Device not found")
    return db_device
