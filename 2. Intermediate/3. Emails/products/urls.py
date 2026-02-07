from django.urls import path

from products.views import (
    ProductDetailView, ProductsView, ProductCreateView, ProductOrderView,
    OrdersListView
)

app_name: str = 'products'

urlpatterns: list = [
    path('', ProductsView.as_view(), name='home'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product'),
    path('products/create', ProductCreateView.as_view(), name='create_product'),
    path('products/orders/', OrdersListView.as_view(), name='orders'),
    path('products/order/<int:pk>', ProductOrderView.as_view(), name='order_product'),
]
