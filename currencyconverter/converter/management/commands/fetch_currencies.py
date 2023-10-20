from django.core.management.base import BaseCommand
from ..utils import CurrencyFetcher
from ...models import Currency

class Command(BaseCommand):
    help = 'Update currency rates'
    def handle(self, *args, **kwargs):
        CurrencyFetcher.fetch_currency_rates()
        self.stdout.write(self.style.SUCCESS('Successfully updated currency rates'))
