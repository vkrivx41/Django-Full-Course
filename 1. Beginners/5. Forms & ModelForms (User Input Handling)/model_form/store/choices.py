from django.db import models


class ProductCategories(models.TextChoices):
    COMPUTER = "computer", "Computer"
    PHONE = "phone", "Phone"
    EARPHONE = "earphone", "Earphone"
    SMARTWATCH = "smartwatch", "Smartwatch"