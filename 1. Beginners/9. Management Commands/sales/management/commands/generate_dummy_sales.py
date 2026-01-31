from django.core.management.base import BaseCommand

from sales.models import Sales

import random
from datetime import date, timedelta



class Command(BaseCommand):
    help = "This command generates dummy sales data"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of rows to generate.')

    def handle(self, *args, **options):
        count: int = options.get('count', 1)

        for _ in range(count):
            Sales.objects.create(
                income=random.uniform(100, 999),
                expenditure=random.uniform(100, 999),
                created_at=date.today() - timedelta(days=random.randint(1, 100))
            )

        self.stdout.write(self.style.SUCCESS(f'Added {count} rows of sales data.'))