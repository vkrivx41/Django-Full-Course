from django.db import models

class RestaurantType(models.TextChoices):
    INDIAN = "IN", "Indian"
    CHININESE = "CH", "Chinese"
    ITALIC = "IT", "Italic"
    MEXICAN = "MX", "Mexican"
    FASTFOOD = "FF", "Fast Food"
    OTHER = "OT", "Other"