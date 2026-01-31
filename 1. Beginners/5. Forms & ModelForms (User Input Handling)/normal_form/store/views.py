from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from .forms import ProductForm
from .models import Product


def add(request) -> HttpResponse:
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            product_name: str = form.cleaned_data.get('product_name')

            product = Product(
                product_name=product_name,
                product_category=form.cleaned_data.get('product_category'),
                product_price=form.cleaned_data.get('product_price'),
                warrant_months=form.cleaned_data.get('warrant_months'),
                is_used=form.cleaned_data.get('is_used'),
                promotion_ends_date=form.cleaned_data.get('promotion_ends_date'),
            )
            product.save()
            
            messages.success(request, f"Product {product_name} added successfully.")

            return redirect("store:index")

    return render(request, "store/add.html", context={
        'title': "Add",
        'form': form
        }
    )


def index(request) -> HttpResponse:
    products: dict = Product.objects.all()

    return render(request, "store/index.html", context={
        'title': "Home",
        'products': products
        } 
    )