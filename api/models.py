from django.db import models
from django.utils import timezone

# Create your models here.

class PriceInMinutes(models.Model):
  timestamp = models.DateTimeField(auto_now_add=True, blank=False, null=True)
  USD = models.DecimalField(blank=False, max_digits=15, decimal_places=2, null=True)

