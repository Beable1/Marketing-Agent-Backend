from celery import Celery

celery_app = Celery(
    "marketing_agent",
    broker="amqp://guest:guest@rabbitmq:5672//",
    backend="rpc://",
)

celery_app.conf.task_routes = {
    "tasks.ingestion.ingest_pdf_task": {"queue": "ingestion"},
}
