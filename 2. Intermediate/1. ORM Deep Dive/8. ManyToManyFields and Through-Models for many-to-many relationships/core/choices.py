from django.db import models


class RestaurantTypeChoices(models.TextChoices):
    INDIAN = "IN", "Indian"
    CHINESE = "CH", "Chinese"
    ITALIAN = "IT", "Italian"
    GREEK = "GR", "Greek"
    MEXICAN = "MX", "Mexican"
    FASTFOOD = "FF", "Fastfood"
    OTHER = "OT", "Other"