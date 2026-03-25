from django.shortcuts import render
from django.http import HttpResponse

from kombu.exceptions import ConnectionError, SerializationError

from . import tasks


def index(request):
    tasks.task_sleepy.delay(5)

    tasks.task_send_email.delay("kapedmour@gmail.com")
    
    return HttpResponse("<h1>Running Celery in the Background</h1>")
