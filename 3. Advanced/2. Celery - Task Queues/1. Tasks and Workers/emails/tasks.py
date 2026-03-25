import time

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from celery import shared_task


@shared_task
def task_sleepy(duration):
    time.sleep(duration)

    print(f"-- Running after {duration} of sleep --")

    return None


@shared_task
def task_send_email(user_email: str):
    html_content = render_to_string("emails/welcome.html", {
        'user_email': user_email
    })
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject="Testing emails with Celery",
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user_email]
    )

    email.attach_alternative(html_content, "text/html")

    email.send()

    return None
