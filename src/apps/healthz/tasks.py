from core.celery import celery


@celery.task
def ping() -> str:
    return "pong"
