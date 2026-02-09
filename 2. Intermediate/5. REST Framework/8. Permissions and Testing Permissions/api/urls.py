from django.urls import path

from api.views import *
from api.serializers import OrderSerializer


app_name: str = "api"


urlpatterns = [
    path("products/", ProductListAPIView.as_view(), name="products"),
    path("products/<int:product_id>", ProductDetailAPIView.as_view(), name="product"),
    path("products/info", products_info, name="products_info"),
    path("orders/", OrderListApiView.as_view(
        serializer_class=OrderSerializer
    ), name="orders"),
    path("user-orders/", UserOrderListApiView.as_view(), name="user_orders"),
]
