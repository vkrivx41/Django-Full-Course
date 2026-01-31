from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

from agenda.models import Agenda

from datetime import date, timedelta


def run():
    try:
        ag1 = Agenda.objects.create(
            name="Agenda X",
            type="event",
            color="green",
            due_date=date.today() - timedelta(days=45)
        )
        
        print(ag1)
        ag1.save()
    except (IntegrityError, ValidationError) as error:
        print(f"ERROR: {str(error)}")