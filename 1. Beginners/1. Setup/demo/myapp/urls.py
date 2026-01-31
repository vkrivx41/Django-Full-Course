from django.urls import path
from . import views

# It's mandatory to name it 'urlpatterns'

urlpatterns: list = [
    path("", views.home, name="home"),
]