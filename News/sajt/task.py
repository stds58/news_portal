from celery import shared_task
import time
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

@shared_task
def rassilka_srazu(subject,body,from_email,to,html_content):
    msg = EmailMultiAlternatives(
        subject=subject,
        body=body,
        from_email=from_email,
        to=to,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    #print(msg)




#celery -A News worker -l INFO --pool=solo