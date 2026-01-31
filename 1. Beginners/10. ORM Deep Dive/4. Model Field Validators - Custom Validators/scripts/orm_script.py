from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection

from pprint import pprint

from core.models import Restaurant, Rating, Sale
from core.choices import RestaurantTypeChoices


def run():
    restaurant1 = Restaurant.objects.all()[2]
    user1 = User.objects.first()

    rating = Rating(
        user=user1,
        restaurant=restaurant1,
        rating=-13
    )

    rating.full_clean()
    rating.save()

