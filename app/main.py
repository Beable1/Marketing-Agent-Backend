from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import health, upload

app = FastAPI(title=settings.project_name, version="0.2.0", debug=settings.debug)

app.include_router(health.router, prefix="/api/v1")
app.include_router(upload.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"msg": "Backend up & running"}