from django.shortcuts import render, HttpResponse

def home(request):
    """The home page view"""

    return HttpResponse("<h1>Blog Home</h1>")

    
def about(request):
    """The about page view"""

    return HttpResponse("<h1>Blog About</h1>")