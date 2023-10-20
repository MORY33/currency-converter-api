import yfinance as yf
from ..models import Currency

# Class that fetches data from yfinance
class CurrencyFetcher:
    @staticmethod
    def fetch_currency_rates(base_currency="USD"):
        tickers = yf.Tickers(f"EUR{base_currency}=X, GBP{base_currency}=X, AUD{base_currency}=X")
        data = tickers.history(period="1d")

        for ticker in data.columns.levels[1]:
            currency_code = ticker.split('=')[0][:3]
            rate = data['Close'][ticker].iloc[0]

            currency, created = Currency.objects.get_or_create(destination_code=currency_code)
            currency.exchange_rate = rate
            currency.base_code = base_currency
            currency.save()

        print("Currency rates updated successfully!")