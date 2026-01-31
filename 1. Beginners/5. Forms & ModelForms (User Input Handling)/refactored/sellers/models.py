from django.db import models


class Seller(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=90, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    categories = models.JSONField()
    profit = models.FloatField(max_length=4)
    contract = models.CharField(max_length=30)

    CONTRACT_CHOICES = [
        ("full", "Full time"),
        ("single", "Single time"),
        ("partial", "Partial time"),
    ]

    CATEGORY_CHOICES = [
        ("Computer", "Computer"), ("Telephone", "Telephone"), ("Earphone", "Earphone")
    ]