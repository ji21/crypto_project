from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from coinbase.wallet.client import Client
from django.views import View
# from django.contrib.auth.decorators import login_required

import json
import os
import environ
env = environ.Env()
# reading .env file
environ.Env.read_env()
# import requests
# Create your views here.

# print(os.environ.get('API_KEY'))

# class HomeView(View):
#   def get(self, request):
#     return render(request, 'crypto/home.html')

# @login_required(login_url='/authenticate/login')
def home(request):
  return render(request, 'crypto/home.html')

#how do i use get spot() to render it onto home.html??


class LogoutView(View):
  def post(self, request):
    auth.logout(request)
    return redirect('home')


