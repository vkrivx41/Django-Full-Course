from django.urls import path


from . import views

app_name: str = "dogs"

urlpatterns: list = [
    path("", views.list, name="list"),
    path("upload/", views.upload, name="upload"),
    path("delete/<int:pk>", views.delete, name="delete"),
]