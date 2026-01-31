from django.db import models


class PermissionChoices(models.TextChoices):
    READ = "RD", "Read"
    CREATE = "CR", "Create"
    MODIFY = "MD", "Modify"
    DELETE = "DL", "Delete"