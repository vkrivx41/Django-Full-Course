from django.db import models


class TitleChoices(models.TextChoices):
    MANAGER = "manager", "Manager"
    COORDINATOR = "coordinator", "Coordinator" 
    EDITOR = "editor", "Editor" 
    SECRETARY = "secretary", "Secretary" 
    ACCOUNTANT = "accountant", "Accountant" 
    PROGRAMMER = "programmer", "Programmer"