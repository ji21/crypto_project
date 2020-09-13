from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Account(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts', null=True)
  balance = models.DecimalField(blank=True, max_digits=20, decimal_places=2, null=True, default=15000.00)
  name = models.CharField(max_length=16, null=True)
  date = models.DateField(default=now)

  def __str__(self):
    return self.name


class Transaction(models.Model):
  account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions', null=True)
  amount_bought = models.IntegerField(blank=False)
  timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  #auto_now_add = True sets the current UTC time upon creation
  market_price_buy_usd = models.IntegerField(blank=False, null=True)
  market_price_buy_gbp = models.IntegerField(blank=False, null=True)
  market_price_buy_eur = models.IntegerField(blank=False, null=True)
  market_price_sell_usd = models.IntegerField(blank=True, null=True)
  market_price_sell_gbp = models.IntegerField(blank=True, null=True)
  market_price_sell_eur = models.IntegerField(blank=True, null=True)
  amount_earned_btc = models.IntegerField(blank=True, null=True)
  amount_earned_usd = models.IntegerField(blank=True, null=True)
  amount_earned_gbp = models.IntegerField(blank=True, null=True)
  amount_earned_eur = models.IntegerField(blank=True, null=True)
