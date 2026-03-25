from django.urls import path

from . import views

app_name = "document"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),

    path("me/", views.MeView.as_view(), name="me"),

    path("", views.DocumentListView.as_view(), name="list"),
    path("<int:document_id>/", views.DocumentDetailView.as_view(), name="detail"),
]


