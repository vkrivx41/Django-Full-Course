from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Sum, Prefetch

from .forms import RatingForm, RestaurantForm
from core.models import (Restaurant, Rating, Sale)


def index(request):
    # Get all restaurants with a 5-star rating and sum their sales income up

    month = timezone.now() - timezone.timedelta(days=30)
    monthly_sales = Prefetch(
        'sales',
        queryset=Sale.objects.filter(datetime__gte=month)
    )

    restaurants = Restaurant.objects\
        .prefetch_related("ratings", monthly_sales)\
        .filter(ratings__rating=5)
    
    total = restaurants.annotate(total=Sum("sales__income"))
    context: dict = {
        'restaurants': restaurants,
        'sums': total,

    }

    return render(request, 'core/index.html', context)