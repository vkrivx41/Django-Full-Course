from django.urls import path

from . import views


app_name: str = "core"


urlpatterns: list = [
    path('', views.index, name='index'),
    path('order_product/', views.order_product, name='order_product'),
    path('orders/', views.orders, name='orders'),
]