from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection, models

from pprint import pprint

from core.models import Restaurant, Rating, Sale
from core.choices import RestaurantTypeChoices


def run():
    ratings = Rating.objects.filter(restaurant__name__icontains="chinese", rating__gte=4)
    print(ratings)

    pprint(connection.queries)