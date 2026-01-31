from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

from sellers.models import Seller

from datetime import datetime



def past_date_validator(self, input_date: datetime):
        if input_date <= datetime.now():
            raise ValidationError("End date can't be in the past", code="past")


class Product(models.Model):
    COLOR_CHOICES = [
        ("Black", "Black"), ("White", "White"), ("Gray", "Gray"), ("Red", "Red"), ("Blue", "Blue"),
        ("Green", "Green"), ("Yellow","Yellow"), ("Gold", "Gold"), ("Silver", "Silver"), ("Mixed", "Mixed")
    ]
    CATEGORY_CHOICES = [
        ("Computer", "Computer"), ("Telephone", "Telephone"), ("Earphone", "Earphone")
    ]

    product_name = models.CharField(max_length=100, unique=True, db_index=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    available_colors = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    used = models.BooleanField(default=False)

    promotion_date_ends = models.DateField(
        validators=[past_date_validator]
    )
    added_at = models.DateTimeField(default=timezone.now)

    seller = models.ForeignKey(Seller, null=True, on_delete=models.SET_NULL)

    def __repr__(self):
        return f"(name={self.product_name}, category={self.category}, price={self.price})"

        
    def set_colors(self, colors_list: list) -> None:
        """
        Save list as comma-separated values
        """
        self.available_colors = ",".join(colors_list) if colors_list else ""

    def get_colors(self) -> list:
        """
        Retrieve colors as a list
        """
        return self.available_colors.split(",") if self.colors else []