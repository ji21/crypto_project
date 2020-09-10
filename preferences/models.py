from django.db import models
from django.contrib.auth.models import User
import pytz
# Create your models here.
class Preferences(models.Model):
  TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
