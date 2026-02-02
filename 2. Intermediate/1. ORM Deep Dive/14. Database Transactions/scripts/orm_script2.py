from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection, models
from django.db.models.functions import  Concat
from django.db.models import Q, F, Value, CharField, Count, Subquery, OuterRef, Exists

from pprint import pprint
from datetime import date
import random

from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from core.choices import RestaurantTypeChoices


def run():
    # 1. for each restaurant return the income of the last sale that was made

    # inner query (subquery)
    # the OuterRef(field) access the field from an outer query, once used in the subquery it will be the called object
    sales = Sale.objects.filter(restaurant=OuterRef('pk')).order_by('-datetime')

    # outer query
    restaurants = Restaurant.objects.annotate(
        last_sale_income=Subquery(sales.values('income')[:1]),
        last_sale_expenditure=Subquery(sales.values('expenditure')[:1]),
        last_profit=F('last_sale_income') - F('last_sale_expenditure')
    )

    for restaurant in restaurants:
        print(f"{restaurant.pk} = {restaurant.last_profit}")

    print(restaurants.count())
    print()

    # 2. filter restaurants that have any sale with income > 85

    # inner query
    sales = Sale.objects.filter(restaurant=OuterRef('pk'), income__gt=85)

    # outer query
    restaurants = Restaurant.objects.filter(Exists(sales))

    print(restaurants)
    print(restaurants.count())


    # 3. get restaurants with sales in the last 20 days
    
    twenty_days_ago = timezone.now() - timezone.timedelta(days=20)

    restaurants = Restaurant.objects.filter(
        Exists(Sale.objects.filter(
            restaurant=OuterRef('pk'),
            datetime__gt=twenty_days_ago
        ))
    )
    print(restaurants.count())