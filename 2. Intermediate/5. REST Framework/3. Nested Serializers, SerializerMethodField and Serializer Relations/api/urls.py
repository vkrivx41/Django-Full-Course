from django.urls import path

from api.views import *


app_name: str = "api"


urlpatterns = [
    path("products/", product_list, name="products"),
    path("products/<int:pk>", product_detail, name="product"),
    path("orders/", order_list, name="orders"),
]
