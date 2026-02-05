from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection, models
from django.db.models.functions import  Concat
from django.db.models import Q, F, Value, CharField, Count, Subquery
from django.db import transaction
from django.db.utils import IntegrityError

from pprint import pprint
from datetime import date
import random

from core.models import Product, Restaurant, Rating, Sale, Staff, StaffRestaurant
from core.choices import RestaurantTypeChoices


def run():
    Restaurant.objects.create(
        name="Waka Waka",
        website="wakawaka.com",
        latitude=56,
        longitude=106,
        date_opened=timezone.now() - timezone.timedelta(days=30),
        restaurant_type=RestaurantTypeChoices.MEXICAN
    )
    restaurants = Restaurant.objects.filter(name__icontains='Waka Waka')
    print(restaurants.count())
    # print(restaurant.latitude, restaurant.longitude)
    