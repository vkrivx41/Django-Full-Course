from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    """The home page view"""
    
    print(request)  # <WSGIRequest: GET '/'>
    print(type(request))  # <class 'django.core.handlers.wsgi.WSGIRequest'>

    return HttpResponse("<h1>Blog Home</h1>")