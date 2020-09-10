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
  setter = 0
  checker = 1
  ws = websocket.WebSocket()
  ws.connect('ws://localhost:8000/ws/priceData/')
  while True:
    start = time.time()
    print(threading.enumerate())
    if checker == 1:
      value = get_spot(key, secret)
      # if value == setter:
      #   end = time.time()
      #   ws.send(json.dumps({"value": None}))
      #   time.sleep(30.0 - (end-start))
      #   continue
      data = PriceInMinutes(market_price=float(value))
      data.save()
      setter = value
      checker = 0
      ws.send(json.dumps({"value": value}))
      end = time.time()
      time.sleep(30.0 - (end-start))
    else:
      ws.send(json.dumps({"value": None}))
      checker = 1
      end = time.time()
      time.sleep(30.0 - (end-start))


t = threading.Timer(5, fetcher, [API_KEY, API_SECRET]).start()

# def a():
#   ws = websocket.WebSocket()
#   ws.connect('ws://localhost:8000/ws/priceData/')
#   while True:
#     print(threading.enumerate())
#     ws.send(json.dumps({"value": 60}))
#     time.sleep(40)
# t = threading.Timer(5, a).start()

# ws = websocket.WebSocket()
# ws.connect('ws://localhost:8000/ws/priceData/')

# for i in range(100):
#   ws.send(json.dumps({"value": value}))







