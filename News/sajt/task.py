from celery import shared_task
import time
from django.core.mail import EmailMultiAlternatives
from .models import Post, Category, User, Author
from django.template.loader import render_to_string
from django.conf import settings
from django.utils import timezone
import datetime


@shared_task
def rassilka_srazu(pk):
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    subscribers_emails = []
    avtor_email = post.author.user.email

    for cat in categories:
        subscribers = cat.subscribers.all()
        for s in subscribers:
            if s.email != avtor_email:
                subscribers_emails.append(s.email)


    html_content = render_to_string(
        'post_created_email.html',
        {
            'small_text': post.preview(),
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=post.head,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_emails,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()



@shared_task
def rassilka_nedela():
    today = timezone.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(datetime_in__gte=last_week)
    categories = set(posts.values_list('category__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers', flat=True))

    for user_id in subscribers:
        if user_id:
            user = User.objects.get(id=user_id)
            user_is_author = Author.objects.filter(user_id=user_id).exists()
            print(f'posts-{posts}')
            if user_is_author:
                postses = posts
                postses = postses.exclude(author=user.author)
                posts_ = set(posts)
            if postses:
                html_content = render_to_string(
                    'daily_post.html',
                    {
                        'link': settings.SITE_URL,
                        'posts': posts_,

                    }
                )

                msg = EmailMultiAlternatives(
                    subject='новости за неделю',
                    body='',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[user.email],
                )

                msg.attach_alternative(html_content, 'text/html')
                msg.send()





#celery -A News worker -l INFO --pool=solo
#celery -A News beat -l INFO