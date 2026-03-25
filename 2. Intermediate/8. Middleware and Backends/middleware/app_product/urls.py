from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("slow/", views.slow, name="slow"),
    path("error/", views.error, name="error"),

    path("api/", views.TestView.as_view(), name="test"),
]
