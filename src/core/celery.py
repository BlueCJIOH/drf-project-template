import os

from celery import Celery
from celery.schedules import crontab
from kombu import Queue

from core.conf.cache import REDIS_PASSWORD, REDIS_HOST, REDIS_PORT
from core.settings import DEBUG, INSTALLED_APPS, TIME_ZONE

from core.conf.environ import env

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Use separate DB indexes for broker/results by default
CELERY_BROKER_DB = env("CELERY_BROKER_DB", default=0)
CELERY_RESULT_DB = env("CELERY_RESULT_DB", default=1)

def _redis_url(db_index: int) -> str:
    password_part = f":{REDIS_PASSWORD}@" if REDIS_PASSWORD else ""
    return f"redis://{password_part}{REDIS_HOST}:{REDIS_PORT}/{db_index}"


CELERY_BROKER_URL = env("CELERY_BROKER_URL", default=_redis_url(CELERY_BROKER_DB))
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND", default=_redis_url(CELERY_RESULT_DB))
CELERY_TIMEZONE = env("CELERY_TIMEZONE", default="UTC")
CELERY_ENABLE_UTC = env.bool("CELERY_ENABLE_UTC", default=True)
CELERY_TASK_ALWAYS_EAGER = env.bool("CELERY_TASK_ALWAYS_EAGER", default=False)
CELERY_TASK_EAGER_PROPAGATES = env.bool("CELERY_TASK_EAGER_PROPAGATES", default=False)

CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = env.bool(
    "CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP", default=True
)

CELERY_TASK_DEFAULT_QUEUE = env("CELERY_TASK_DEFAULT_QUEUE", default="default")


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

celery = Celery("app")

celery.conf.update(
    broker_url=env("CELERY_BROKER_URL"),
    result_backend=env("CELERY_RESULT_BACKEND"),
    timezone=TIME_ZONE,
    broker_connection_retry_on_startup=True,
    task_always_eager=env("CELERY_ALWAYS_EAGER", cast=bool, default=DEBUG),
    task_eager_propagates=True,
    task_ignore_result=True,
    task_acks_late=True,
    task_store_errors_even_if_ignored=True,
    task_queues=(
        Queue("default", routing_key="default"),
    ),
    task_routes={
        "apps.healthz.tasks.*": {"queue": "default"},
    },
    task_default_queue="default",
    beat_schedule={
        "health_ping": {
            "task": "apps.healthz.tasks.ping",
            "schedule": crontab(minute="*/5"),
            "options": {"queue": "default"},
        },
    },
)


celery.autodiscover_tasks(lambda: INSTALLED_APPS)

__all__ = ("celery",)
