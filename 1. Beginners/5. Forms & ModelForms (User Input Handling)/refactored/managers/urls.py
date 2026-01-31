from django.urls import path

from . import views


app_name: str = "managers"

urlpatterns: list = [
    path("add/", views.managers, name="add"),
]