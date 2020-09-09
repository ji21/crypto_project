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

API_KEY=os.environ.get('API_KEY')
API_SECRET=os.environ.get('API_SECRET')

def get_spot(key, secret, num):
  print("this is previous number", num)
  start = time.time()
  client = Client(API_KEY, API_SECRET, api_version='2020-08-25')
  price = client.get_spot_price(currency='USD')
  # rates = client.get_exchange_rates(currency='BTC')
  value = price.amount
  print("now this is current value", value)
  print(value, datetime.datetime.now())
  if value == num:
    print("if clause")
    print("-------------")
    # sleep(5)
    # get_spot(key, secret, value)
    t = threading.Timer(5, get_spot, [key,secret, value]).start()
    return 0
  else:
    print("else clause")
    end = time.time()
    print('shifted time', end-start)
    print("---------")
    # data = PriceInMinutes(market_price=value)
    # data.save()
    t = threading.Timer(60 - (end-start), get_spot, [key, secret, value]).start()
    return 0



get_spot(API_KEY, API_SECRET, 0)




