from django.urls import path

from products.views import (
    ProductDetailView, SellerDetailView, ProductsView, SellersListView,
    ProductCreateView, ProductUpdateView, SellerCreateView
)

app_name: str = 'products'

urlpatterns: list = [
    path('', ProductsView.as_view(), name='home'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product'),
    path('products/create', ProductCreateView.as_view(), name='create_product'),
    path('products/update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('sellers/', SellersListView.as_view(
        template_name='products/sellers.html'
    ), name='sellers'),
    path('sellers/create', SellerCreateView.as_view(), name='create_seller'),
    path('seller/<slug:slug>', SellerDetailView.as_view(), name='seller'),
]
