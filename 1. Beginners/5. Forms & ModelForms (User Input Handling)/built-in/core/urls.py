
from django.contrib import admin
from django.urls import path, include
from users import views as users_view


# setting a path using the view is not ideal because it restricts the addition of namespaces
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
    path('register/', users_view.register, name="register"),
]
