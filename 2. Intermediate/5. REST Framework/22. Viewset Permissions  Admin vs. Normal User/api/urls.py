from django.urls import path

from rest_framework.routers import DefaultRouter

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
]

router = DefaultRouter()

router.register("orders", viewset=OrderViewSet)

urlpatterns += router.urls
