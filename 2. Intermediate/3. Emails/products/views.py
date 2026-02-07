from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.db import transaction

from functools import partial

from products.models import Product, Order, Buyer

from services.EmailService import EmailService

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


class ProductOrderView(CreateView):
    model = Order
    fields = ('buyer', 'product', 'quantity')

    success_url = reverse_lazy('products:orders')
    template_name = 'products/order_product.html'

    def form_valid(self, form):
        order = form.instance
        product = Product.objects.select_for_update(nowait=False).get(
            pk=order.product.pk
        )
    
        try:
            with transaction.atomic():
                product.number_in_stock -= order.quantity
                product.save()

                transaction.on_commit(partial(EmailService().send_email, context={
                    'buyer': order.buyer,
                    'order': order,
                    'orders_url': self.request.build_absolute_uri(reverse('products:orders')),
                }))

                return super().form_valid(form)
        except Exception as e:
            form.add_error(None, f"Order failed: {str(e)}")
            return self.form_invalid(form)


class OrdersListView(ListView):
    model = Order
    paginate_by = 5

    context_object_name = 'orders'
    template_name = 'products/orders.html'

    def get_queryset(self):
        orders = super().get_queryset()
        return orders.select_related('buyer', 'product')