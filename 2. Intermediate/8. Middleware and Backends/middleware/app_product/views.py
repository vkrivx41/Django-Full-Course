import time

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics, response


def home(request):
    return HttpResponse("Home Page")


def slow(request):
    time.sleep(1)

    return HttpResponse("Slow Page")

def error(request):

    print(5/0)
    return HttpResponse("Error Page")


class TestView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return response.Response({
            "detail": "Page Loaded",
        })