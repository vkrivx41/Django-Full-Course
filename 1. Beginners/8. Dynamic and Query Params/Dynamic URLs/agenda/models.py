from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

from datetime import date

from .choices import AgendaTypeChoices, AgendaColorChoices

# This class creates the CURRENT_DATE function from PostgreSQL, MySQL, and more
class CurrentDate(models.Func):  
    function = 'CURRENT_DATE'  
    template = '%(function)s'  


class Agenda(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    type = models.CharField(max_length=20, choices=AgendaTypeChoices)
    color = models.CharField(max_length=20, choices=AgendaColorChoices)
    due_date = models.DateField()
    created_at = models.DateField(default=timezone.now)
    accomplished = models.BooleanField(default=False)

    class Meta:
        ordering: list = ['due_date', 'name']

        constraints: list = [
            models.CheckConstraint(
                name='valid_due_date',
                check=models.Q(due_date__gt=CurrentDate()),
                violation_error_message="Due Date Must Be After Creation Date."
            )
        ]

    def __str__(self) -> str:
        return f"{self.name}, due <{self.due_date}>"
    
    def clean(self) -> None:
        super().clean()

        if self.due_date <= date.today():
            raise ValidationError({'due_date': "Due Date Must Be After Creation Date."})
        
    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        super().save(*args, **kwargs)