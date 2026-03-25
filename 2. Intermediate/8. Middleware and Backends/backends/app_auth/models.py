from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(
        max_length=13,
        unique=True,
        db_index=True
    )

    class Meta:
        indexes = [
            models.Index(fields=['email'], name='index_email'),
            models.Index(fields=['phone_number'], name='index_phone_number'),
        ]
