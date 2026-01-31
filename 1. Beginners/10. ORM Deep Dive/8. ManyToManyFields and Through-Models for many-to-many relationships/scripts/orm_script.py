from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection, models

from pprint import pprint
from datetime import date

from core.models import Restaurant, Rating, Sale, Staff, StaffRestaurant
from core.choices import RestaurantTypeChoices


def run():
    # all, add, count, set, remove, clear, filter
    restaurant1, restaurant2 = Restaurant.objects.all()[4:6]
    staff = Staff.objects.get(id=1)
    
    # StaffRestaurant.objects.create(staff=staff, restaurant=restaurant1, salary=20_000, date_joined=date(2019, 5, 6))
    # StaffRestaurant.objects.create(staff=staff, restaurant=restaurant2, salary=54_000, date_joined=date(2023, 11, 19))

    staff_restaurants = StaffRestaurant.objects.filter(staff__name=staff.name)
    print([s.restaurant for s in staff_restaurants])

    staff.restaurants.add(restaurant1, through_defaults={
        'salary': 29_500,
        'date_joined': date(2025, 1, 3)
    })

    staff_restaurants = StaffRestaurant.objects.filter(staff=staff)
    print([s.salary for s in staff_restaurants])
    