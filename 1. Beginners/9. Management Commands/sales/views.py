from django.shortcuts import render, HttpResponse


def sales(request) -> HttpResponse:
    return HttpResponse('<h1>Sales</h1>')