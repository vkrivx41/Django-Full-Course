from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Sum, Prefetch
from django.db import transaction

from functools import partial
import time

from .forms import RatingForm, RestaurantForm, ProductOrderForm
from core.models import (Order, Product, Restaurant, Rating, Sale, Staff, StaffRestaurant)


def index(request):
    # jobs whose staff members id is 2
    # note: the Prefetch object accepts only QuerySet not a single model
    staff_2 = Prefetch(
        'staff',
        Staff.objects.filter(id=2)
    )

    jobs = StaffRestaurant.objects.prefetch_related("restaurant", staff_2)

    context: dict = {
        'jobs': jobs
    }

    return render(request, 'core/index.html', context=context)


def send_email(email):
    print(f"Hello {email}, your order was placed successfully!")


def order_product(request):
    form = ProductOrderForm()

    if request.method == "POST":
        form = ProductOrderForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                order = form.save(commit=False)
                product = Product.objects.select_for_update(
                    # nowait=True,  # will raise an error claiming not access to a locked row
                    # skip_locked=True,  # will raise a DoesNotExist error pretending the row doesn't exist
                ).get(id=order.product.id)

                time.sleep(10)

                product.number_in_stock -= order.number_of_items
                product.save()
                order.save()

            transaction.on_commit(partial(send_email, "user@gmail.com"))

            return redirect(to='core:orders')

    context: dict = {
        'form': form
    }

    return render(request, 'core/order_product.html', context)


def orders(request):
    orders = Order.objects.select_related('product')

    context: dict = {
        'orders': orders
    }

    return render(request, 'core/orders.html', context)