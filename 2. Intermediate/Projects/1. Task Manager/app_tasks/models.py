from django.db import models
from django.contrib.auth.models import User, AbstractUser

from datetime import date


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, unique=True)
    profile_image = models.ImageField(upload_to="profiles/", null=True, blank=True)


class Day(models.Model):
    class WeekDayChoices(models.TextChoices):
        MONDAY = "Monday"
        TUESDAY = "Tuesday"
        WEDNESDAY = "Wednesday"
        THURSDAY = "Thursday"
        FRIDAY = "Friday"

    date = models.DateField(default=date.today)
    focus_time_goal = models.PositiveIntegerField()
    day_of_week = models.CharField(choices=WeekDayChoices.choices)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="days")


class Task(models.Model):
    class TaskCategories(models.TextChoices):
        EVENT = "Event"
        TASK = "Task"
        ROUTINE = "Routine"

    class TaskStatuses(models.TextChoices):
        PENDING = "Pending"
        PROGRESSING = "Progressing"
        DONE = "Done"
        CANCELLED = "Cancelled"

    name = models.CharField(max_length=100)
    category = models.CharField(choices=TaskCategories.choices, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=TaskStatuses.choices, max_length=20)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="tasks")
    day = models.ManyToManyField(to=Day, through="Schedule")


class Schedule(models.Model):
    day = models.ForeignKey(to=Day, on_delete=models.CASCADE, related_name="schedules")
    task = models.ForeignKey(to=Task, on_delete=models.CASCADE, related_name="schedules")
    requires_focus = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task.name} - {self.day}"
    
