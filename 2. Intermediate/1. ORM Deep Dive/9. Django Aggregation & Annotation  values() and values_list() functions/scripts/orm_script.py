from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection, models
from django.db.models.functions import Upper, Length, Concat
from django.db.models import CharField, Sum, Count, Min, Max, Avg, Value

from pprint import pprint
from datetime import date

from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from core.choices import RestaurantTypeChoices


def run():
    # 1. return the average income per each restaurant type
    # 2. return the restaurants with a total rating of above 10
    # 3. return the restaurants whose sales are above the average sales of all sales

    # Look for advanced techniques
    
    # 4. return the restaurants whose sales are above the average sales for the restaurant type
    # 5. return the restaurant's sales that are higher the the previous ones

    # Restaurant 1: [Rating: 4.3]

    # display = Concat('name', 
    #     Value(' [Rating: '), Avg('ratings__rating'), Value(' ]'),
    #     output_field=CharField()
    # )

    # 1. return the average income per each restaurant type
    # Solution:
    result = Restaurant.objects.values_list('restaurant_type').annotate(
        average_income=Avg('sales__income')
    ).order_by('-average_income')
    print([r for r in result])

    # 2. return the restaurants with a total rating of above 10
    #  Solution:
    result = Restaurant.objects.annotate(
        total_rating=Sum('ratings__rating')
    ).filter(total_rating__gt=10).values_list('name', 'total_rating')

    print([r for r in result])

    # 3. return the restaurants whose sales are above the average sales of all sales
    #  Solution:
    overall_avg = Sale.objects.aggregate(avg_all=Avg('income'))
    print(overall_avg)

    result = Restaurant.objects.annotate(
        avg_sales=Avg('sales__income')
    ).filter(avg_sales__gt=overall_avg['avg_all']).values_list('name', 'avg_sales')

    print([r for r in result])