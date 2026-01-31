from django.urls import path
from . import views


app_name: str = 'todo'

urlpatterns: list = [
    path("", views.home, name="index"),
    path("create/", views.create, name="create"),
]