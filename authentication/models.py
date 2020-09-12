from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
  preferred_name = models.CharField(max_length=20)
  phone = models.CharField(max_length=20, blank=True, null=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


class Account(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts', null=True)
  balance = models.DecimalField(blank=True, max_digits=20, decimal_places=2, null=True)

class Transaction(models.Model):
  account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions', null=True)
  amount_bought = models.IntegerField(blank=False)
  timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  #auto_now_add = True sets the current UTC time upon creation
  market_price_buy_usd = models.IntegerField(blank=False, null=True)
  market_price_buy_gdp = models.IntegerField(blank=False, null=True)
  market_price_buy_eur = models.IntegerField(blank=False, null=True)
  market_price_sell_usd = models.IntegerField(blank=True, null=True)
  market_price_sell_gdp = models.IntegerField(blank=True, null=True)
  market_price_sell_eur = models.IntegerField(blank=True, null=True)
  amount_earned_btc = models.IntegerField(blank=True, null=True)
  amount_earned_usd = models.IntegerField(blank=True, null=True)
  amount_earned_gdp = models.IntegerField(blank=True, null=True)
  amount_earned_eur = models.IntegerField(blank=True, null=True)


class Wallet(models.Model):
  account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)
  balance = models.IntegerField()




