from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from datetime import datetime

from .choices import ProductCategories

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200, choices=ProductCategories.choices)
    product_price = models.PositiveIntegerField()
    warrant_months = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(24)]
    )
    is_used = models.BooleanField(default=False)
    promotion_ends_date = models.DateField(default=datetime.now)

    def __repr__(self):
        return self.product_name