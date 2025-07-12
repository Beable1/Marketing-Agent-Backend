# Celery uygulamasını içe aktar ve `celery` adıyla dışa aktar
from app.core.celery_app import celery_app as celery  # noqa: F401

# Görevlerin modülü – import side‑effect olarak register olur
import app.tasks.ingestion  # noqa: E402,F401