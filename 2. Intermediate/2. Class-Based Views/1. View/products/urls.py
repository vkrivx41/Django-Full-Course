from django.urls import path

from products.views import *

app_name: str = 'products'

urlpatterns: list = [
    path('', BaseView.as_view(), name='base'),
    path('products/', ProductsView.as_view(), name='products'),
]