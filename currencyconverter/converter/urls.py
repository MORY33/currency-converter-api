from django.urls import path, re_path
from .views import CurrencyViewSet

urlpatterns = [
    re_path(r'^(?P<target_currency>\w+)/(?P<base_currency>\w+)/$',
            CurrencyViewSet.as_view({'get': 'retrieve'}), name='currency-exchange-rate'),
    path('', CurrencyViewSet.as_view({'get': 'list'}), name='currency-list')
]
