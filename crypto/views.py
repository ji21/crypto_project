from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from accounts.models import Account
import json
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
    user = self.request.user
    print("....................................>", user)
    if not user.is_anonymous:
      account_set = user.accounts.all()
      if len(account_set) == 0:
        context = {
          'accounts': False
        }
      else:
        context = {
          'accounts': account_set
        }
      return render(request, 'crypto/charts.html', context)
    else:
      return render(request, 'crypto/charts.html')

  def post(self, request):
    data = json.loads(request.body)
    account_id = data['id']
    account = Account.objects.get(pk=account_id)
    balance = account.balance

    return JsonResponse({'balance': balance})


class LandingView(View):
  def get(self, request):
    return render(request, 'crypto/landing.html')



