from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection

from pprint import pprint

from core.models import Restaurant, Rating, Sale
from core.choices import RestaurantTypeChoices


def run():
    restaurant = Restaurant.objects.first()

    # we've changed the reverse manager 'related_name'
    print(restaurant.ratings.all())
    print(restaurant.sales.all())

    pprint(connection.queries)