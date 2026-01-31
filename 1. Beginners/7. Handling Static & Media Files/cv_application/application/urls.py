from django.urls import path

from . import views


app_name = "cv"

urlpatterns: list = [
    path("", views.home, name="home"),
    path("application/", views.application, name="application"),
    path("edit", views.edit, name="edit"),
    path("delete", views.delete, name="delete"),
]