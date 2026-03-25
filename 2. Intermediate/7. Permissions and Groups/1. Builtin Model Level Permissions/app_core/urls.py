from django.urls import path

from . import views

app_name = "document"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),

    path("", views.document_list, name="list"),
    path("<int:id>/", views.document_detail, name="detail"),
]


