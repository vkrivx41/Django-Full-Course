from django.urls import path



from chat import views

app_name: str = 'chat'


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('home/', views.HomeListView.as_view(), name='home'),
]
