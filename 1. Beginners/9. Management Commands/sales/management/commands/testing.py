from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "A command for testing if commands works"

    def handle(self, *args, **kwargs):
        self.stdout.write("Testing Command")