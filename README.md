# Marketing Agent Backend – Quickstart

```bash
cp .env.sample .env
# edit credentials if needed

# Build & run local stack
docker compose up --build

# Test liveness
http :8000/api/v1/health

# Test upload
http -f POST :8000/api/v1/upload/pdf \
  customer_id=123e4567-e89b-12d3-a456-426614174000 \
  file@./tests/sample.pdf
```

> Bu sürüm, **PDF yükleme** işlevini tamamlar ve dosyaları MinIO/S3’e kaydeder. Bir sonraki adımda:
> 1️⃣ Veritabanı (PostgreSQL + SQLAlchemy) ekleyip `File` meta kaydını tutacağız.
> 2️⃣ Celery/RabbitMQ ile ingestion worker kuracağız.
