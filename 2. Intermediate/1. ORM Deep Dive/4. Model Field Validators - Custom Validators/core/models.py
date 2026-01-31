from django.db import models
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

    def __str__(self) -> str:
        return f"Restaurant: {self.name}"
    


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
        return f"{self.restaurant.name} -> {self.income}"