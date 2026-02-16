from django.urls import path

from api.views import *
from api.serializers import OrderSerializer


app_name: str = "api"


urlpatterns = [
    path("products/", ProductListCreateAPIView.as_view(), name="products"),
    path("products/create/", ProductCreateAPIView.as_view(), name="products_create"),
    path("products/update/<int:pk>/", ProductUpdateAPIView.as_view(), name="products_update"),
    path("products/delete/<int:pro_id>/", ProductDeleteAPIView.as_view(), name="products_delete"),
    path("products/<int:product_id>/", ProductDetailAPIView.as_view(), name="product"),
    path("products/info/", ProductInfoAPIView.as_view(), name="products_info"),
    path("orders/", OrderListApiView.as_view(
        serializer_class=OrderSerializer
    ), name="orders"),
    path("user-orders/", UserOrderListApiView.as_view(), name="user_orders"),
]
