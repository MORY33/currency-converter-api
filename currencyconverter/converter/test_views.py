from django.test import TestCase
from rest_framework.test import APIClient
from converter.models import Currency


class CurrencyTestCase(TestCase):

    def setUp(self):    
        self.client = APIClient()

    def test_currency_list(self):
        Currency.objects.create(base_code="USD", destination_code="USD", exchange_rate=1)
        Currency.objects.create(base_code="USD", destination_code="AUD", exchange_rate=0.63)

        response = self.client.get("/currency/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_currency_retrieve(self):
        Currency.objects.create(base_code="USD", destination_code="EUR", exchange_rate=1.0589)

        response = self.client.get("/currency/EUR/USD/")
        self.assertEqual(response.status_code, 200)
