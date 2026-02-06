from django.urls import path

from products.views import ProductDetailView, SellerDetailView, ProductsView, SellersView

app_name: str = 'products'

urlpatterns: list = [
    path('', ProductsView.as_view(), name='products'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product'),
    path('sellers/', SellersView.as_view(
        template_name='products/sellers.html'
    ), name='sellers'),
    path('seller/<slug:slug>', SellerDetailView.as_view(), name='seller'),
]
