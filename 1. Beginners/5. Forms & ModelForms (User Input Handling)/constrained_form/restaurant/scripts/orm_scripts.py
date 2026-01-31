from restaurant.models import Restaurant, Rating, Sale
from django.contrib.auth.models import User
from django.db import connection
from django.db.utils import IntegrityError

from ..choices import RestaurantType

# def set_wal_mode():  
#     with connection.cursor() as cursor:  
#         cursor.execute("PRAGMA journal_mode=WAL;")  

def run():
    user = User.objects.get(username="joe")
    restaurant = Restaurant.objects.all().first()

    rating = Rating(
        user=user,
        restaurant=restaurant,
        rating=4
    )

    # rating.full_clean()
    try:
        rating.save()
        print(rating)
    except IntegrityError as error:
        print(f"ERROR: {str(error)}")
        
    Restaurant.objects.create(
        name=restaurant.name.upper(),
        latitude=50,
        longitude=-89,
        restaurant_type=RestaurantType.CHININESE,
    )

    connection.close()