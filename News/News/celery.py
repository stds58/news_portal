import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'News.settings')

app = Celery('News')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


# app.conf.beat_schedule = {
#     'action_every_30_seconds': {
#         'task': 'sajt.task.rassilka_nedela',
#         'schedule': 10,
#     },
# }

app.conf.beat_schedule = {
    'email_news_every_monday_8_utra': {
        'task': 'sajt.task.rassilka_nedela',
        #'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'schedule': crontab(hour=17, minute=16, day_of_week='saturday'),
    },
}
