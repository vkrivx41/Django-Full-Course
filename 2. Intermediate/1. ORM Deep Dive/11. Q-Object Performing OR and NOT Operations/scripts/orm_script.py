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
    # find all the restaurants with the number 1 in the name
    # it_or_pizz = Q(name__icontains="italian") | Q(name__icontains="pizzeria")
    # recently_opened = ~Q(date_opened__gt=timezone.now() - timezone.timedelta(days=30))

    # restaurants = Restaurant.objects.filter(
    #     it_or_pizz & recently_opened
    # )

    # print(restaurants)

    # find all the sales where
    #     - profit is greater than the expenditure
    # OR
    #     - name contains a number [0-9]

    contains_num = Q(restaurant__name__regex=r'[0-9]+')
    profit_gt_expenditure = Q(income__gt=F('expenditure'))

    sales = Sale.objects.select_related('restaurant')\
        .filter(contains_num & profit_gt_expenditure)\
        .values('restaurant__name', 'income', 'expenditure')
    
    print(sales.count())