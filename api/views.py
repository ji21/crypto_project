from django.shortcuts import render
from django.conf import settings
from coinbase.wallet.client import Client
from django.http import HttpResponse, JsonResponse


from rest_framework import viewsets
from .serializers import PriceInMinutesSerializer, HisotircalDataSerializer
from .models import PriceInMinutes, HistoricalData

import datetime
import time
import threading

import json
import os
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()
# Create your views here.


class PriceInMinutesViewSet(viewsets.ModelViewSet):
  queryset = PriceInMinutes.objects.all()
  serializer_class = PriceInMinutesSerializer

class HistoricalDataViewSet(viewsets.ModelViewSet):
  queryset = HistoricalData.objects.all()
  serializer_class = HisotircalDataSerializer


def get_spot():
  start = time.time()

  API_KEY=os.environ.get('API_KEY')
  API_SECRET=os.environ.get('API_SECRET')
  API_KEY = env('API_KEY')
  API_SECRET = env('API_SECRET')
  client = Client(API_KEY, API_SECRET, api_version='2020-08-25')
  price = client.get_spot_price(currency='USD')
  # rates = client.get_exchange_rates(currency='BTC')
  price_str = json.dumps(price)

  end = time.time()

  print('shifted time', end-start)

  print(price_str, datetime.datetime.now())

  print("---------")

  t = threading.Timer(60 - (end-start),get_spot).start()

get_spot()




