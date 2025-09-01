from pydantic import BaseModel
from datetime import datetime

class DeviceBase(BaseModel):
    ip: str
    mac: str
    hostname: str

class DeviceCreate(DeviceBase):
    pass

class DeviceUpdate(BaseModel):
    hostname: str | None = None
    suspicious: bool | None = None

class Device(DeviceBase):
    id: int
    last_seen: datetime
    suspicious: bool

    class Config:
        orm_mode = True
