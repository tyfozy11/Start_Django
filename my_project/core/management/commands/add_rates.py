from parsing import parse
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        parse.add_rates()