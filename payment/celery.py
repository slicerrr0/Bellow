from celery import Celery

app = Celery(
    'payment',
)