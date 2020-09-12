from django.shortcuts import render
from django.conf import settings
from coinbase.wallet.client import Client
from django.http import HttpResponse, JsonResponse


from rest_framework import viewsets
from .serializers import PriceInMinutesSerializer
from .models import PriceInMinutes

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


# API_KEY=os.environ.get('API_KEY')
# API_SECRET=os.environ.get('API_SECRET')

def get_spot():
  # client = Client(API_KEY, API_SECRET, api_version='2020-08-25')
  # price = client.get_spot_price(currency='USD')
  # value = price.amount

  response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
  usd = response.json()['bpi']['USD']['rate_float']
  gdp = response.json()['bpi']['GBP']['rate_float']
  eur = response.json()['bpi']['EUR']['rate_float']
  timestamp = response.json()['time']['updated']

  return [usd, gdp, eur, timestamp]




def fetcher():
  setter = 0
  checker = 1
  ws = websocket.WebSocket()
  ws.connect('ws://localhost:8000/ws/priceData/')
  while True:
    start = time.time()
    print(threading.enumerate())
    if checker == 1:
      arr = get_spot()
      # if value == setter:
      #   end = time.time()
      #   ws.send(json.dumps({"value": None}))
      #   time.sleep(30.0 - (end-start))
      #   continue
      print(arr)
      data = PriceInMinutes(timestamp=arr[3], USD=float(arr[0]), GDP=float(arr[1]), EUR=float(arr[2]))
      data.save()
      setter = arr
      checker = 0
      ws.send(json.dumps({"value": arr}))
      end = time.time()
      time.sleep(30.0 - (end-start))
    else:
      ws.send(json.dumps({"value": [None]}))
      checker = 1
      time.sleep(60.0 - (datetime.datetime.now().second + datetime.datetime.now().microsecond/1000000))


t = threading.Timer(60.0 - (datetime.datetime.now().second + datetime.datetime.now().microsecond/1000000), fetcher).start()

