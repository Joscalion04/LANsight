from fastapi import FastAPI
from app.database import engine
from app.models import device as device_model
from app.routers import device as device_router

device_model.Base.metadata.create_all(bind=engine)

app = FastAPI(title="LANsight API")

app.include_router(device_router.router)

@app.get("/")
def root():
    return {"message": "LANsight API corriendo 🚀"}
