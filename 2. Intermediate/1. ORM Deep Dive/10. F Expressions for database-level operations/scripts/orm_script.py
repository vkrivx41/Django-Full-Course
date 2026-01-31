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
    sales = Sale.objects.annotate(
        profit=F('income') - F('expenditure')
    ).order_by('-profit')

    print(sales.first().profit)

    sales = Sale.objects.aggregate(
        profit=Count('id', filter=Q(income__gt=F('expenditure'))),
        loss=Count('id', filter=Q(income__lt=F('expenditure'))),
    )

    print(sales)

    rating = Rating.objects.first()

    print(rating.rating)

    rating.rating = F('rating') + 1
    rating.save()

    rating.refresh_from_db()

    print(rating.rating)