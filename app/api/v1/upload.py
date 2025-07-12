from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status
from app.core.storage import upload_pdf
from app.schemas.file import UploadResponse

from app.tasks.ingestion import ingest_pdf_task

router = APIRouter(tags=["Files"])

# ✨ Basit tenant simülasyonu (gerçekte OAuth claim’den gelecek)
async def get_tenant_id() -> str:
    return "demo-tenant"  # to‑do: decode from OAuth token

@router.post("/upload/pdf", response_model=UploadResponse)
async def upload_pdf_endpoint(
    customer_id: str = Form(..., description="Customer UUID"),
    file: UploadFile = File(..., description="PDF file"),
    tenant_id: str = Depends(get_tenant_id),
):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Only PDF allowed")
    key = upload_pdf(file, tenant_id, customer_id)
    ingest_pdf_task.delay(key, tenant_id)
    return UploadResponse(key=key)