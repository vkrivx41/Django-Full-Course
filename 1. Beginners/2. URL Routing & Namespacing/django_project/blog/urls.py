from django.urls import path
from . import views

# this is the namespace of this app 'blog'
# when referring to it it must be used as a prefix ex blog:index

app_name = "blog"

urlpatterns: list = [
    path("", views.home, name="index"),
    path("about/", views.about, name="about"),
]