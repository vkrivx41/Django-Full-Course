from django.urls import path

from . import views

app_name: str = 'agenda'


urlpatterns: list = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('edit/<int:pk>', views.edit, name='edit'),
]