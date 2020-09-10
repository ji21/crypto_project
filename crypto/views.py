from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
# from django.contrib.auth.decorators import login_required

# import requests
# Create your views here.

# print(os.environ.get('API_KEY'))

# class HomeView(View):
#   def get(self, request):
#     return render(request, 'crypto/home.html')

# @login_required(login_url='/authenticate/login')
def home(request):
  return render(request, 'crypto/home.html')

class ChartsView(View):
  def get(self, request):
    return render(request, 'crypto/charts.html')

class LandingView(View):
  def get(self, request):
    return render(request, 'crypto/landing.html')
