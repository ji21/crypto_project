from django.shortcuts import render
from django.conf import settings
from coinbase.wallet.client import Client
from django.http import HttpResponse, JsonResponse


from rest_framework import viewsets
from .serializers import PriceInMinutesSerializer, HisotircalDataSerializer
from .models import PriceInMinutes, HistoricalData

from .consumers import PriceConsumer

import datetime
import time
import threading

import json
import os
import environ

import requests
import redis
import websocket





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

def get_spot(key, secret):
  # print("number of threads", threading.active_count())
  # print("this is ALL THE thread", threading.enumerate())
  # print("current thread---->", threading.current_thread())
  # start = time.time()
  client = Client(API_KEY, API_SECRET, api_version='2020-08-25')
  price = client.get_spot_price(currency='USD')
  value = price.amount
  # print("now this is current value", value)
  print(value, datetime.datetime.now())
  return value
  # if value == num:
  #   end = time.time()
  #   t = threading.Timer(30.0 - (end-start), get_spot, [key, secret, value]).start()
  #   return 0
  # else:
  #   print("---------")
  #   data = PriceInMinutes(market_price=float(value))
  #   data.save()

  #   t = threading.Timer(60.0 - (end-start), get_spot, [key, secret, value]).start()



# get_spot(API_KEY, API_SECRET, 0)
# print("look at this first thread", threading.current_thread())
API_KEY=os.environ.get('API_KEY')
API_SECRET=os.environ.get('API_SECRET')

def fetcher(key, secret):
  ws = websocket.WebSocket()
  ws.connect('ws://localhost:8000/ws/priceData/')
  setter = 0
  while True:
    print(threading.enumerate())
    start = time.time()
    value = get_spot(key, secret)
    if value == setter:
      end = time.time()
      time.sleep(30.0)
      continue
    print(value)
    data = PriceInMinutes(market_price=float(value))
    data.save()
    ws.send(json.dumps({"value": value}))
    setter = value
    end = time.time()
    time.sleep(60.0 - (end-start))


print("bilibala")
t = threading.Timer(5, fetcher, [API_KEY, API_SECRET]).start()



