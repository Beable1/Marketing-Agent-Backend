from pydantic import BaseModel, Field

class UploadResponse(BaseModel):
    key: str = Field(..., description="S3 object key of stored PDF")
