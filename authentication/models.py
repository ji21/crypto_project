from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
  full_name = models.CharField(max_length=20)
  phone = models.CharField(max_length=20, blank=True, null=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
