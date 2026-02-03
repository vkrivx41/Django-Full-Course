from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection, models
from django.db.models.functions import  Concat
from django.db.models import Q, F, Value, CharField, Count, Subquery
from django.db import transaction

from pprint import pprint
from datetime import date
import random

from core.models import Product, Restaurant, Rating, Sale, Staff, StaffRestaurant
from core.choices import RestaurantTypeChoices


def run():
    with transaction.atomic():
        product = Product.objects.select_for_update(
            # nowait=True,  # will raise an error claiming not access to a locked row
            # skip_locked=True,  # will raise a DoesNotExist error pretending the row doesn't exist
        ).get(name='Jumper')
        product.number_in_stock += 10
        product.save()

    print(product.number_in_stock)

    