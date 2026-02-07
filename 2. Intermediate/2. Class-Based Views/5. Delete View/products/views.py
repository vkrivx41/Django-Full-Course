from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages

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
    

class ProductDetailView(DetailView):
    model = Product

    context_object_name = 'product'
    template_name = 'products/product.html'

    slug_field = 'slug'  # DB model slug field
    slug_url_kwarg = 'slug'  # url slug field name (from url.py)


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'

    template_name = 'products/create_product.html'
    success_url = reverse_lazy('products:home')  # re-writes the get_absolute_url method

    def form_valid(self, form):
        product_name: str = form.cleaned_data['name']

        messages.success(self.request, f"Product {product_name} Created.")
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'number_in_stock', 'price')

    template_name = 'products/update_product.html'


class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'product'

    template_name = 'products/delete_product.html'
    success_url = reverse_lazy('products:home')

    def form_valid(self, form):
        """
        Enables us to send messages or perform any other event before deleteing.
        This is ran after submission from a confirmation page.
        """
        obj = self.object
        product_name = obj.name

        messages.success(self.request, f"Product {product_name} has been deleted.")

        return super().form_valid(form)



######################################################################################3

class SellersListView(ListView):
    model = Seller
    context_object_name = 'sellers'

    paginate_by = 3

    def get_queryset(self):
        sellers = super().get_queryset()
        return sellers.prefetch_related('products')


class SellerDetailView(DetailView):
    model = Seller
    
    context_object_name = 'seller'
    template_name = 'products/seller.html'

    def get_object(self, **kwargs):
        seller =  super().get_object(**kwargs)
        return seller


class SellerCreateView(CreateView):
    model = Seller
    fields = '__all__'

    template_name = 'products/create_seller.html'