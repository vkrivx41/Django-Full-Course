from django.urls import path
from . import views


app_name: str = "products"

urlpatterns: list = [
    path("", views.home, name="home"),
    path("add/", views.add, name="add"),
]