from django.urls import path

from products.views import ProductDetailView, ProductsView

app_name: str = 'products'

urlpatterns: list = [
    path('', ProductsView.as_view(), name='products'),
    path('product/<str:slug>', ProductDetailView.as_view(), name='product'),
]
