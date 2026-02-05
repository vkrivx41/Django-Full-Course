from django.db import models
from django.utils import timezone



class Seller(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13, unique=True)
    email = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class ProductCategories(models.TextChoices):
        ELECTRONICS = "electronics", "Electronics"
        APPLIANCE = "appliance", "Appliance"
        BEAUTY = "beauty", "Beauty"
        CLOTHING = "clothing", "Clothing"
        TRAVEL = "travel", "Travel"

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=ProductCategories.choices)
    number_in_stock = models.PositiveIntegerField()
    date_posted = models.DateField(default=timezone.now)
    seller = models.ForeignKey(to=Seller, on_delete=models.DO_NOTHING, related_name='products')


    def __str__(self):
        return f"{self.name} - {self.number_in_stock}"
    