from django.db import models
from django.db.models.functions import Lower
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

from .choices import RestaurantTypeChoices

import re


def validate_resto_includes_symbol(name: str) -> None:
    pattern = re.compile(r"[^a-zA-Z0-9\s]")

    if pattern.findall(name):
        raise ValidationError(
            message="Restaurant name must not include special symbols and characters",
            params={
                "name": name
            }
        )


class Restaurant(models.Model):

    class TypeChoices(models.TextChoices):
        INDIAN = "IN", "Indian"
        CHINESE = "CH", "Chinese"
        ITALIAN = "IT", "Italian"
        GREEK = "GR", "Greek"
        MEXICAN = "MX", "Mexican"
        FASTFOOD = "FF", "Fastfood"
        OTHER = "OT", "Other"


    name = models.CharField(
        max_length=100,
        validators=[validate_resto_includes_symbol]
    )
    website = models.URLField(default="")
    date_opened = models.DateField()
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)]
    )
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )
    restaurant_type = models.CharField(max_length=2, choices=RestaurantTypeChoices.choices)


    class Meta:
        ordering: list = [Lower("name"), "-date_opened"]
        get_latest_by: str = "date_opened"


    def __str__(self) -> str:
        return f"Restaurant: {self.name}"
    
    def save(self, *args, **kwargs) -> None:
        # get the model state as self._state and access the adding attr to check if it's already added or not
        # doesn't work with the QuerySet.update method, bcs it doesn't call the save method
        print(self._state.adding)
        super().save(*args, **kwargs)
    

class Staff(models.Model):
    name = models.CharField(max_length=50)
    restaurants = models.ManyToManyField(to=Restaurant, related_name="staff", through="StaffRestaurant")

    def __str__(self) -> str:
        return self.name
    

class StaffRestaurant(models.Model):
    staff = models.ForeignKey(to=Staff, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)
    salary = models.FloatField(null=True)
    date_joined = models.DateField(null=True)


class Rating(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE, related_name="ratings")
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self) -> str:
        return f"Rating: {self.rating}"
    
    

class Sale(models.Model):
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.SET_NULL, null=True, related_name="sales")
    income = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()

    def __str__(self) -> str:
        try:
            return f"{self.restaurant.name} -> {self.income}"
        except AttributeError as _:
            return f"{self.income}"    