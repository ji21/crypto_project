from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Preferences(models.Model):
  USD = 'USD'
  GBP = 'GBP'
  EUR = 'EUR'
  currencies = [
    (USD, 'USD'),
    (GBP, 'GBP'),
    (EUR, 'EUR')
  ]
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  currency = models.CharField(max_length=5, choices=currencies, default='USD')
