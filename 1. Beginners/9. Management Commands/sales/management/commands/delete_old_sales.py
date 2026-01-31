from django.core.management.base import BaseCommand

from sales.models import Sales

import random
from datetime import date, timedelta



class Command(BaseCommand):
    help = "This command delete old sales data"

    def add_arguments(self, parser):
        parser.add_argument('time', type=int, help='The time from which we will delete the previous ones in days.')

    def handle(self, *args, **options):
        target_time: int = options.get('time', 1)

        old_sales = Sales.objects.filter(
            created_at__lte=date.today() - timedelta(days=target_time)
        )

        count = old_sales.delete()
        
        if count[0] > 0:
            self.stdout.write(self.style.SUCCESS(f'Deleted {count[0]} rows of old sales data.'))
        else:
            self.stderr.write(self.style.WARNING('There was no rows to delete'))