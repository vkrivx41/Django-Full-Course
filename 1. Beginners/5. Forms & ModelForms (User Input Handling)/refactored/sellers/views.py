from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from .forms import SellerForm, Seller


def sellers(request) -> HttpResponse:
    sellers = Seller.objects.all()
    
    if request.method == "POST":
        form = SellerForm(request.POST)

        if form.is_valid():
            form.save()

            seller_name = form.cleaned_data.get("username")
            messages.success(request, f"Seller {seller_name} added successfully.")

            return redirect("sellers:add")
    else:
        form = SellerForm()
    
    return render(request, "sellers/sellers.html", context={
        'title': "Sellers",
        'sellers': sellers,
        'form': form,
        }
    )