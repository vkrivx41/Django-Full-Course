from django.urls import path
from . import views

# this is the namespace of this app 'dashboard'
# when referring to it it must be used as a prefix ex dashboard:index

app_name = "dashboard"

urlpatterns = [
    path('', views.dashboard, name="index"),
    path('analytics/', views.analytics, name="analytics"),
]