import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bellow.settings')

app = Celery('payment')