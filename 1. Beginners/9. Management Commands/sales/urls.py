from django.urls import path

from . import views


urlpatterns: list = [
    path('', views.sales, name='sales')
]