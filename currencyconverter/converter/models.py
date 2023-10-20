from django.db import models


class Currency(models.Model):
    destination_code = models.CharField(max_length=3, primary_key=True)
    base_code = models.CharField(max_length=3)
    exchange_rate = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.exchange_rate)
