from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    help = "A command for greeting a person"

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('name', type=str, help='The name of the person')  # positional (always required)
        parser.add_argument('--times', '-t', type=int, default=1, help='The number of times to loop')

    def handle(self, *args, **kwargs):
        name: str = kwargs['name']
        times: int = kwargs['times']

        for _ in range(times):
            self.stdout.write(f"Hello, {name}")