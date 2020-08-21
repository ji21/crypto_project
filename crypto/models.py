from django.db import models

# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  # transaction = models.ForeignKey(Transaction, on_delete=model.CASCADE)
  email = models.EmailField(max_length=40)
  # phone = PhoneNumberField(null=False, blank=False, unique=True)
  api_code = models.CharField(max_length=200, blank=True)


class Transaction(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  amount = models.IntegerField()
  fee = models.IntegerField()
  to = models.CharField(max_length=100)

class Wallet(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  balance = models.IntegerField()
  # password =
