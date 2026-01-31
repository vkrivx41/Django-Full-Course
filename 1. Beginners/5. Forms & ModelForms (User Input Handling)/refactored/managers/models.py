from django.db import models
from django.core.exceptions import ValidationError

from datetime import date


class Manager(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=90, unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    date_joined = models.DateField(default=date.today)
    permissions = models.JSONField(default=list)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                models.functions.Lower("username"),
                name="unique_name_cons",
            )
        ]

    def clean_phone_number(self):
        if len(self.phone_number) != 10:
            raise ValidationError({
                'phone_number': "Phone number must be 10 digits."
            })
        
        if not self.phone_number.isdigit():
            raise ValidationError({
                'phone_number': "Phone number must be digits."
            })
        
    def save(self, *args, **kwargs):
        self.full_clean()

        return super().save(args, kwargs)