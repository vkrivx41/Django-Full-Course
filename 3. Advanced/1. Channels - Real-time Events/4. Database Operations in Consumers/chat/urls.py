from django.urls import path

from chat import views

app_name: str = 'chat'


urlpatterns = [
    path('<str:room_name>/', views.room, name='room'),
]