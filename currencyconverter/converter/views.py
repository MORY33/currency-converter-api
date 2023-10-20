from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics, filters
from .models import Currency
from .serializers import CurrencySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from drf_yasg.utils import swagger_auto_schema


class CurrencyViewSet(viewsets.ModelViewSet):
    '''
        Currencies viewset
    '''

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['destination_code']
    ordering_fields = ['destination_code', 'exchange_rate']
    lookup_field = ['destination_code']

    @swagger_auto_schema(
        operation_description="Get a list of all available currencies",
        responses={200: 'List of currencies'}
    )
    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Get a list of all available exchange rates",
        responses={200: 'List of currencies'}
    )
    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        base_code = self.kwargs.get('base_currency')
        destination_code = self.kwargs.get('target_currency')
        try:
            currency = Currency.objects.get(base_code=base_code, destination_code=destination_code)
        except Currency.DoesNotExist:
            raise NotFound(detail="exchange rate not found")

        serializer = CurrencySerializer(currency)
        return Response(serializer.data, status=status.HTTP_200_OK)

