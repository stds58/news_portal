from celery import shared_task
import time



@shared_task
def rassilka_srazu(res):
    res.send()



#celery -A News worker -l INFO --pool=solo