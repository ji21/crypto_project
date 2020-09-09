from django.db import models
from django.utils import timezone

# Create your models here.

class PriceInMinutes(models.Model):
  timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  market_price = models.DecimalField(blank=False, max_digits=15, decimal_places=2)

class HistoricalData(models.Model):
  market_price = models.DecimalField(blank=False, max_digits=15, decimal_places=2)
  date = models.DateField(auto_now_add=False)
