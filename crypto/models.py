from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  # transaction = models.ForeignKey(Transaction, on_delete=model.CASCADE)
  email = models.EmailField(max_length=40)
  # phone = PhoneNumberField(null=False, blank=False, unique=True)
  api_code = models.CharField(max_length=200, blank=True, null=True)


class Transaction(models.Model):
  seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller', null=True)
  buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer', null=True)
  amount = models.IntegerField(blank=False)
  transaction_fee = models.IntegerField(blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  #auto_now_add = True sets the current UTC time upon creation
  market_price = models.IntegerField(blank=False)
  #market price is the exchange rate at the time of creation

class Wallet(models.Model):
  owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  balance = models.IntegerField()
  # password =
