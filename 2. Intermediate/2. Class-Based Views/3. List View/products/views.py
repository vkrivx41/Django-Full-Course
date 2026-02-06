from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from products.models import Product, Seller


class ProductsView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'base/index.html'

    paginate_by = 7

    def get_queryset(self):
        products = super().get_queryset()
        return products.select_related('seller')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page: int = int(self.request.GET.get('page', 1))

        context['paginator'] = context['page_obj']  # rewrite the default page_obj for pagination
        context['page'] = page

        del context['page_obj']

        return context
    
    def get_paginate_by(self, queryset):
        """
        Can be used to manipulate the paginate_by value in case needed
        """
        return super().get_paginate_by(queryset)
    
    def paginate_queryset(self, queryset, page_size):
        """
        Used for more sophisticated manipulation of the pagination and Paginator object
        """
        return super().paginate_queryset(queryset, page_size)


class SellersView(ListView):
    model = Seller
    context_object_name = 'sellers'

    paginate_by = 3

    def get_queryset(self):
        sellers = super().get_queryset()
        return sellers.prefetch_related('products')
    

class ProductDetailView(DetailView):
    model = Product

    context_object_name = 'product'
    template_name = 'products/product.html'

    slug_field = 'slug'  # DB model slug field
    slug_url_kwarg = 'slug'  # url slug field name (from url.py)


class SellerDetailView(DetailView):
    model = Seller
    
    context_object_name = 'seller'
    template_name = 'products/seller.html'

    def get_object(self, **kwargs):
        seller =  super().get_object(**kwargs)
        return seller
