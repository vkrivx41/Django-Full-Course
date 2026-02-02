from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection, models
from django.db.models.functions import  Concat
from django.db.models import Q, F, Value, CharField, Count, Subquery

from pprint import pprint
from datetime import date
import random

from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from core.choices import RestaurantTypeChoices


def run():
    # sales for restaurants that are IT or CH
    restaurant_types = [RestaurantTypeChoices.ITALIAN, RestaurantTypeChoices.ITALIAN]

    # inner query (subquery)
    restaurants = Restaurant.objects.filter(restaurant_type__in=restaurant_types)

    # outer query
    sales = Sale.objects.filter(restaurant__in=Subquery(restaurants.values('id')))

    print(sales.count())
    