from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Sum, Prefetch

from .forms import RatingForm, RestaurantForm
from core.models import (Restaurant, Rating, Sale, Staff, StaffRestaurant)


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