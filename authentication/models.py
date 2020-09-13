from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
  preferred_name = models.CharField(max_length=20)
  phone = models.CharField(max_length=20, blank=True, null=True)
  currency = models.CharField(max_length=5, blank=True, null=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)




