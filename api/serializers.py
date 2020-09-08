from .models import PriceInMinutes, HistoricalData
from rest_framework import serializers

class PriceInMinutesSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = PriceInMinutes
    fields = ['timestamp', 'market_price']

class HisotircalDataSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = HistoricalData
    fields = ['market_price', 'date']
