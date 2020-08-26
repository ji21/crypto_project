from django.shortcuts import render
from django.http import HttpResponse
from coinbase.wallet.client import Client
from django.http import JsonResponse
from django.views import View
import json
import os
import environ
env = environ.Env()
# reading .env file
environ.Env.read_env()
# import requests
# Create your views here.

print(os.environ.get('API_KEY'))


def home_view(request):
  # url = "https://blockchain.info/ticker"
  # ex_rate = json.loads(requests.get(url))
  return render(request, 'crypto/home.html')

#how do i use get spot() to render it onto home.html??

def get_spot():
  API_KEY=os.environ.get('API_KEY')
  API_SECRET=os.environ.get('API_SECRET')
  client = Client(API_KEY, API_SECRET, api_version='2020-08-25')
  currency_code = 'USD'
  price = client.get_spot_price(currency=currency_code)
  # rates = client.get_exchange_rates(currency='BTC')
  price_str = json.dumps(price)
  return HttpResponse(price_str)
