from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

from django.db.models.functions import Lower
from django.core.validators import MinValueValidator, MaxValueValidator

from .choices import RestaurantType


class Restaurant(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True
    )
    website = models.URLField(default="")
    date_opened = models.DateField(null=True)
    latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    restaurant_type = models.CharField(max_length=2, choices=RestaurantType.choices)
    capacity = models.PositiveSmallIntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = [Lower("name")]
        get_latest_by = "date_opened"

        constraints: list = [
            models.CheckConstraint(
                name="valid_latitude",
                check=Q(latitude__gte=-90, latitude__lte=90),
                violation_error_message="Latitude must be in the range -90 and 90"
            ),
            models.CheckConstraint(
                name="valid_longitude",
                check=Q(latitude__gte=-180, latitude__lte=180),
                violation_error_message="Longitude must be in the range -180 and 180"
            ),
            models.UniqueConstraint(
                Lower("name"),
                name="unique_name_cons",
            )
        ]

    def __str__(self) -> str:
        return f"{self.name} - {self.restaurant_type}"
    

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="restaurant")
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self) -> str:
        return f"Rating: {self.rating}"
    
    class Meta:
        constraints: list = [
            models.CheckConstraint(
                name="valid_rating_cons",
                check=Q(rating__gte=1, rating__lte=5),
                violation_error_message="Rating Invalid: Choose a valid number"
            ),
            models.UniqueConstraint(
                name="user_resto_uniq_cons",
                fields=["user", "restaurant"]
            )
        ]
    

class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name="sale")
    income = models.DecimalField(max_digits=8, decimal_places=2)
    expenditure = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()