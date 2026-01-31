from django.shortcuts import render, HttpResponse

def home(request):
    """The home page view"""

    # create some dummy posts
    posts: list[dict] = [
        {
            'author': "Michael Givens",
            'title': "Blog Post 1",
            'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolor, nulla!",
            'date_posted': "February 13, 2025",
        },
        {
            'author': "Anna Bella",
            'title': "Blog Post 2",
            'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolor, nulla!",
            'date_posted': "January 20, 2025",
        }
    ]

    # create context dict to be passed as a context
    context: dict = {
        'posts': posts
    }

    return render(request, "home.html", context=context)

    
def about(request):
    """The about page view"""

    return render(request, "about.html", context={'title': "About"})