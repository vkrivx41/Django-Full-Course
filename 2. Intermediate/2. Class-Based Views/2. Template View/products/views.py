from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from products.models import Product


class ProductsView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        products = Product.objects.select_related('seller')

        context['products'] = products
        return context
    


class ProductDetailView(TemplateView):
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        path: str = self.request.get_full_path()
        obj_name: str = path.split("/")[-1]

        product = Product.objects.get(
            slug=obj_name
        )

        context =  super().get_context_data(**kwargs)
        context['product'] = product

        return context
    