from django.shortcuts import render
from django.conf import settings

import os
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()
# Create your views here.

API_KEY = env('API_KEY')

API_SECRET = env('API_SECRET')

print(API_SECRET)

def get_spot():
  # API_KEY=os.environ.get('API_KEY')
  # API_SECRET=os.environ.get('API_SECRET')
  client = Client(API_KEY, API_SECRET, api_version='2020-08-25')
  currency_code = 'USD'
  price = client.get_spot_price(currency=currency_code)
  # rates = client.get_exchange_rates(currency='BTC')
  price_str = json.dumps(price)
  return HttpResponse(price_str)
