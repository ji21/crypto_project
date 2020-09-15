from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Account(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts', null=True)
  balance = models.DecimalField(blank=True, max_digits=20, decimal_places=2, null=True, default=15000.00)
  new_balance = models.DecimalField(blank=True, max_digits=20, decimal_places=2, null=True)
  name = models.CharField(max_length=16, null=True)
  date = models.DateField(default=now)
  original_name = models.CharField(max_length=16, null=True)
  active = models.BooleanField(default=False)

  def __str__(self):
    return self.name


class Transaction(models.Model):
  account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions', null=True)
  btc_buy_price = models.DecimalField(blank=True, max_digits=20, decimal_places=10, null=True)
  btc_sell_price = models.DecimalField(blank=True, max_digits=20, decimal_places=10, null=True)
  btc_bought = models.DecimalField(blank=True, max_digits=20, decimal_places=10, null=True)
  timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  #auto_now_add = True sets the current UTC time upon creation
  usd_invested = models.DecimalField(blank=True, max_digits=20, decimal_places=10, null=True)
  gbp_invested = models.DecimalField(blank=True, max_digits=20, decimal_places=10, null=True)
  eur_invested = models.DecimalField(blank=True, max_digits=20, decimal_places=10, null=True)
  usd_gained = models.DecimalField(blank=True, max_digits=20, decimal_places=10, null=True)
  gbp_gained = models.DecimalField(blank=True, max_digits=20, decimal_places=10, null=True)
  eur_gained = models.DecimalField(blank=True, max_digits=20, decimal_places=10, null=True)
  btc_earned = models.DecimalField(blank=True, max_digits=20, decimal_places=10, null=True)
  in_progress = models.BooleanField(default=True)
