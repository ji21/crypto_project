from django.db import models
from django.utils import timezone

# Create your models here.

class PriceInMinutes(models.Model):
  timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  market_price = models.IntegerField(blank=False)

class HistorialData(models.Model):
  market_price = models.IntegerField(blank=False)
  date = models.DateField(auto_now_add=False)
