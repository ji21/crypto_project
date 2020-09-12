from django.db import models
from django.utils import timezone

# Create your models here.

class PriceInMinutes(models.Model):
  timestamp = models.CharField(max_length = 30, blank=False, null=True)
  USD = models.DecimalField(blank=False, max_digits=15, decimal_places=2, null=True)
  GDP = models.DecimalField(blank=False, max_digits=15, decimal_places=2, null=True)
  EUR = models.DecimalField(blank=False, max_digits=15, decimal_places=2, null=True)
