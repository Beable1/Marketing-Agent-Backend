import uuid
from pathlib import Path
import boto3
from botocore.config import Config
from fastapi import UploadFile
from app.core.config import settings

_session = boto3.session.Session()

s3_client = _session.client(
    "s3",
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
    region_name=settings.s3_region,
    endpoint_url=settings.s3_endpoint_url,  # None → AWS
    config=Config(signature_version="s3v4"),
)

BUCKET = settings.s3_bucket


def upload_pdf(file: UploadFile, tenant_id: str, customer_id: str) -> str:
    """Uploads the given PDF to S3 and returns the object key."""
    ext = Path(file.filename).suffix or ".pdf"
    key = f"pdf/{tenant_id}/{customer_id}/{uuid.uuid4()}{ext}"
    s3_client.upload_fileobj(file.file, BUCKET, key, ExtraArgs={"ContentType": "application/pdf"})
    return key