import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exchanger.settings.localhost')

app = Celery('exchanger')
app.config_from_object('django.conf:settings')

app.conf.beat_schedule = {
    'add-daily-at-nine': {
        'task': 'app.tasks.update_currencies',
        'schedule': crontab(minute=0, hour=9)
    },
}

app.conf.timezone = 'Europe/Moscow'

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
