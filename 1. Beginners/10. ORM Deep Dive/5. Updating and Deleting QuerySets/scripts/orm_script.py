from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection

from pprint import pprint

from core.models import Restaurant, Rating, Sale
from core.choices import RestaurantTypeChoices


def run():
    restaurant = Restaurant.objects.first()
    restaurants = Restaurant.objects.filter(name__icontains="resto")
    
    # print(restaurants.update(
    #     date_opened=timezone.now() - timezone.timedelta(weeks=3, days=17),
    #     latitude=-71
    # ))

    print(restaurants.delete())

    pprint(connection.queries)