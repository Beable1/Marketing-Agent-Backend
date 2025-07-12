from app.core.celery_app import celery_app
from app.core.storage import s3_client, BUCKET
from app.utils.pdf import extract_chunks
from app.core.vector import vector_db

@celery_app.task(name="tasks.ingestion.ingest_pdf_task", bind=True, max_retries=3, retry_backoff=True)
def ingest_pdf_task(self, s3_key: str, tenant_id: str):
    """PDF'i S3'ten indir, metni çıkar, sahte embedding üret, vektör DB'ye yükle"""
    try:
        obj = s3_client.get_object(Bucket=BUCKET, Key=s3_key)
        chunks = extract_chunks(obj["Body"].read())
        # SAHTE embedding: metin uzunluğuna göre float listesi
        embeddings = [[len(c) / 1000.0] * 3 for c in chunks]
        items = [(f"{s3_key}-{i}", vec) for i, vec in enumerate(embeddings)]
        vector_db.upsert(namespace=tenant_id, items=items)
    except Exception as exc:
        raise self.retry(exc=exc)