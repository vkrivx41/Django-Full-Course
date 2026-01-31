from django.urls import path
from . import views


app_name: str = 'blog'

urlpatterns: list = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]