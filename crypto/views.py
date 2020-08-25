from django.shortcuts import render
from django.http import HttpResponse
from coinbase.wallet.client import Client
import json
import os
import environ
env = environ.Env()
# reading .env file
environ.Env.read_env()
# import requests
# Create your views here.

print(os.environ.get('API_KEY'))

def loginView(request):
  return render(request, 'login.html')



def homeView(request):
  # url = "https://blockchain.info/ticker"
  # ex_rate = json.loads(requests.get(url))
  API_KEY=os.environ.get('API_KEY')
  API_SECRET=os.environ.get('API_SECRET')
  client = Client(API_KEY, API_SECRET, api_version='2020-08-25')
  currency_code = 'USD'
  price = client.get_spot_price(currency=currency_code)
  rates = client.get_exchange_rates(currency='BTC')
  a = json.dumps(price)
  b = json.dumps(rates)
  return HttpResponse(b)
