
from django.shortcuts import render, HttpResponse
from .models import Post

def home(request):
    """The home page view"""

    # create context dict to be passed as a context
    context: dict = {
        'posts': Post.objects.all()
    }

    return render(request, "blog/home.html", context=context)

    
def about(request):
    """The about page view"""

    return render(request, "blog/about.html", context={'title': "About"})