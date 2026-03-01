from django.urls import path



from chat import views

app_name: str = 'chat'


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('home/', views.HomeGeneralView.as_view(), name='home'),
    path('home-data/', views.HomeDataView.as_view(), name='home_data'),
    path('read-messages/', views.ReadMessageView.as_view(), name='read_messages'),
    path('room-messages/', views.MessageListView.as_view(), name='room_messages'),
]
