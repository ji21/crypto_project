from .models import PriceInMinutes
from rest_framework import serializers

class PriceInMinutesSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = PriceInMinutes
    fields = ('timestamp', 'USD')

