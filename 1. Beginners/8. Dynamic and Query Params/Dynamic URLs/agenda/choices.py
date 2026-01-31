from django.db import models


class AgendaTypeChoices(models.TextChoices):
    TASK = "task", "Task"
    EVENT = "event", "Event"
    BD = "bd", "Birthday"
    HOLIDAY = "holiday", "Holiday"


class AgendaColorChoices(models.TextChoices):
    RED = "red", "Red"
    BLUE = "blue", "Blue"
    YELLOW = "yellow", "Yellow"
    GREEN = "green", "Green"
    PINK = "pink", "Pink"