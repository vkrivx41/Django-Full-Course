from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection, models
from django.db.models.functions import Upper, Length, Concat, RowNumber
from django.db.models import CharField, Sum, Count, Min, Max, Avg, Value

from pprint import pprint
from datetime import date

from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from core.choices import RestaurantTypeChoices


def run():
    # Look for advanced techniques
    
    # 4. return the restaurants whose sales are above the average sales for the restaurant type
    # 5. return the restaurant's sales that are higher the the previous ones
    # result = Restaurant.objects.annotate(RowNumber())
    # print(result)
    print(Restaurant.objects.values().first())