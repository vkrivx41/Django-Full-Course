from django.db import models
from django.contrib.auth.models import User

from .choices import RestaurantTypeChoices


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(default="")
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    restaurant_type = models.CharField(max_length=2, choices=RestaurantTypeChoices.choices)

    def __str__(self) -> str:
        return f"Restaurant: {self.name}"
    


class Rating(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE, related_name="ratings")
    rating = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"Rating: {self.rating}"
    
    

class Sale(models.Model):
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.SET_NULL, null=True, related_name="sales")
    income = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.restaurant.name} -> {self.income}"