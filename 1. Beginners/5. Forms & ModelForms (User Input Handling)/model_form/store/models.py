from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

from datetime import date

from .choices import ProductCategories


def validate_promotion_date(input_date: date):
    if input_date < date.today():
        raise ValidationError("Promotion ends date can't be in the past.")


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    product_category = models.CharField(max_length=200, choices=ProductCategories.choices)
    product_price = models.PositiveIntegerField()
    warrant_months = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(24)]
    )
    is_used = models.BooleanField(default=False)
    promotion_ends_date = models.DateField(
        default=date.today,
        validators=[validate_promotion_date]
    )

    def __repr__(self):
        return self.product_name