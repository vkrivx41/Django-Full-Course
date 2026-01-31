from django.db import models


class Sales(models.Model):
    income = models.DecimalField(max_digits=6, decimal_places=2)
    expenditure = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateField()
