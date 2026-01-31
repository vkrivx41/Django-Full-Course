from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection, models
from django.db.models.functions import  Concat, Coalesce
from django.db.models import Q, F, Value, CharField, Count, Sum, Avg

from pprint import pprint
from datetime import date
import random

from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from core.choices import RestaurantTypeChoices


def run():
    Restaurant.objects.update(
        capacity=None
    )

    print(Restaurant.objects.aggregate(total_cap=Sum('capacity')))
    print(Restaurant.objects.aggregate(total_cap=Coalesce(Sum('capacity'), 0)))

    negative_ratings = Rating.objects.filter(rating__lt=0)
    print(negative_ratings)
    print(negative_ratings.aggregate(mean=Avg('rating')))
    print(negative_ratings.aggregate(mean=Coalesce(Avg('rating'), 0.0)))
    print(negative_ratings.aggregate(mean=Avg('rating', default=0.0)))

    print()
    restaurants = Restaurant.objects.annotate(
        nick=Coalesce(F('nickname'), F('name'))
    ).values('nick')

    print(restaurants)

