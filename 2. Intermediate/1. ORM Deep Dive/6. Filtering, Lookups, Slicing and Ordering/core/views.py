from django.shortcuts import render, redirect

from .forms import RatingForm, RestaurantForm


def index(request):
    form = RestaurantForm()

    if request.method == "POST":
        form = RestaurantForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(to="core:index")

    context: dict = {
        'form': form
    }

    return render(request, 'core/index.html', context)