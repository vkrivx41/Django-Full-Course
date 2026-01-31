from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .forms import ProductForm
from .models import Product


def home(request) -> HttpResponse:
    products: list = Product.objects.all()
    return render(request, 'products/home.html', context={'products': products})

def add(request) -> HttpResponse:
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            product_category: str = form.cleaned_data.get("category")
            product_name: str = form.cleaned_data.get("product_name")

            instance.set_colors(form.cleaned_data.get("available_colors"))
            instance.save()

            messages.success(request, f"{product_category.title()}, {product_name} added successfully.")

            return redirect("products:home")
    else:
        form = ProductForm()

    return render(request, 'products/add.html', context={
        'title': "Products",
        'form': form
    })
