from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection, models
from django.db.models.functions import  Concat
from django.db.models import Q, F, Value, CharField, Count

from pprint import pprint
from datetime import date
import random

from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from core.choices import RestaurantTypeChoices


def run():
    restaurant1 = Restaurant.objects.first()
    restaurant2 = Restaurant.objects.last()

    # restaurants = Restaurant.objects.filter(
    #     capacity__isnull=True
    # ).values('name')

    restaurants = Restaurant.objects.filter().order_by(F('capacity').asc(
        nulls_last=True
    )).values('capacity')

    print(restaurants)
    print(restaurants.aggregate(count=Count('pk')))

    # print(connection.queries)