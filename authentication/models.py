from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
  preferred_name = models.CharField(max_length=20)
  phone = models.CharField(max_length=20, blank=True, null=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


class Account(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts', null=True)

class Transaction(models.Model):
  account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions', null=True)
  amount_bought = models.IntegerField(blank=False)
  transaction_fee = models.IntegerField(blank=True, null=True, editable=True)
  created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  #auto_now_add = True sets the current UTC time upon creation
  market_price_buy = models.IntegerField(blank=False)
  market_price_sell = models.IntegerField(blank=True, null=True)
  amount_earned = models.IntegerField(blank=True, null=True)
  #market price is the exchange rate at the time of creation

class Wallet(models.Model):
  account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)
  balance = models.IntegerField()




