from django.urls import path
from . import views


app_name: str = "store"


urlpatterns: list = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
]