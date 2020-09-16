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





class PriceInMinutesViewSet(viewsets.ModelViewSet):
  queryset = PriceInMinutes.objects.all()
  serializer_class = PriceInMinutesSerializer




def get_spot():
  response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
  usd = response.json()['bpi']['USD']['rate_float']
  return usd



def fetcher():
  checker = 1
  ws = websocket.WebSocket()
  ws.connect('ws://localhost:8000/ws/priceData/')
  while True:
    start = time.time()
    print(threading.enumerate())
    if checker == 1:
      current_price = get_spot()
      print(current_price)
      data = PriceInMinutes(USD=current_price)
      data.save()
      checker = 0
      ws.send(json.dumps({"value": current_price}))
      end = time.time()
      time.sleep(30.0 - (end-start))
    else:
      ws.send(json.dumps({"value": None}))
      checker = 1
      time.sleep(60.0 - (datetime.datetime.now().second + datetime.datetime.now().microsecond/1000000))


t = threading.Timer(60.0 - (datetime.datetime.now().second + datetime.datetime.now().microsecond/1000000), fetcher).start()

