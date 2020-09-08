from django.contrib import admin
from .models import PriceInMinutes, HistoricalData
# Register your models here.

admin.site.register(PriceInMinutes)
admin.site.register(HistoricalData)
