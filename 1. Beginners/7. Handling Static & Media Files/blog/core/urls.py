
from django.contrib import admin
from django.urls import path, include
from users import views as users_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls"), name="home"),
    path('', include("users.urls"), name="register"),
    path('', include("users.urls"), name="login"),
    path('', include("users.urls"), name="logout"),
]
