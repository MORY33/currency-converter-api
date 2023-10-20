from rest_framework import serializers
from .models import Currency


class CurrencySerializer(serializers.ModelSerializer):

    destination_code = serializers.CharField()
    base_code = serializers.CharField()
    exchange_rate = serializers.FloatField()

    class Meta:
        model = Currency
        fields = '__all__'