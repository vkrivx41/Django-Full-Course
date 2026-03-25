from django.urls import path

from app_tasks import views

app_name: str = "tasks"


urlpatterns = [
    path("", views.home, name="home")
]
