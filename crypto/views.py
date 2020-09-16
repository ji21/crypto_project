from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from accounts.models import Account, Transaction
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
        active = False
        active_account = None
        market_buy_price = False
        btc_bought = False
        for account in account_set:
          if account.active:
            active_account = account
            active = True
            market_buy_price = round(account.transactions.latest("timestamp").btc_buy_price, 4)
            btc_bought = round(account.transactions.latest("timestamp").btc_bought, 2)
            break

        context = {
          'accounts': account_set,
          'active': active,
          'active_account': active_account,
          'market_buy_price': market_buy_price,
          'btc_bought': btc_bought
        }
      return render(request, 'crypto/charts.html', context)
    else:
      return render(request, 'crypto/charts.html')

  def post(self, request):
    data = json.loads(request.body)
    account_id = data['account_id']
    account = Account.objects.get(pk=account_id)
    balance = account.balance

    try:
      try:
        amount_invested = float(data['amount_invested'])
        current_price = float(data['current_price'])
        print("this is balance", balance)
        print(type(balance))
        # btc_bought = amount_invested/current_price
        # print(type(amount_invested))
        # print(int(amount_invested)/current_price)
        btc_bought = amount_invested/current_price
        # print(amount_invested)
        # print(type(amount_invested))
        # print(current_price)
        # print(type(current_price))
        # print(balance)
        # print(type(balance))
        # print(btc_bought)
        # print(type(btc_bought))
        balance = float(balance) - amount_invested
        if balance >= 0:
          transaction = Transaction(account=account, btc_buy_price=current_price, usd_invested=amount_invested, btc_bought=btc_bought)
          transaction.save()
          account.new_balance = balance
          account.active = True
          account.save()
          print("balance again............", balance)
          return JsonResponse({'amount_invested': amount_invested, 'new_balance': balance, 'btc_bought': btc_bought})
        else:
          return JsonResponse({'balance': None}, status=400)
      except:

        amount_sold = float(data['amount_sold'])
        current_price = float(data['current_price'])
        transaction = Transaction.objects.filter(account=account).latest('timestamp')
        buy_price = float(transaction.btc_buy_price)
        # print("trans buy price", buy_price)
        # print(type(buy_price))
        # print("current sell price", current_price)
        # print(type(current_price))
        btc_earned = current_price - buy_price
        # print(btc_earned)
        # print(type(btc_earned))
        usd_invested = float(transaction.usd_invested)
        btc_bought = float(transaction.btc_bought)
        usd_gained = ((current_price/buy_price) * usd_invested) - usd_invested
        # print(".................", usd_gained)
        # print("balance when sold", balance)
        transaction.btc_sell_price = current_price
        transaction.btc_earned = btc_earned
        transaction.usd_gained = usd_gained
        transaction.in_progress = False
        # transaction.update(btc_sell_price=current_price, btc_earned=btc_earned, usd_gained=usd_gained)
        transaction.save()
        print("..........balance", balance)
        print(type(balance))
        print("..........used_gained", usd_gained)
        print(type(usd_gained))
        new_balance = float(balance) + usd_gained
        account.balance = new_balance
        account.new_balance = new_balance
        account.active = False
        account.save()
        usd_gained = round(usd_gained, 2)
        btc_bought = round(btc_bought, 3)
        current_price = round(current_price, 4)
        return JsonResponse({'balance': balance, 'new_balance': new_balance, 'usd_gained': usd_gained, 'usd_invested': usd_invested, 'btc_bought': btc_bought, 'current_price': current_price})
    except:
      return JsonResponse({'balance': balance})

class LandingView(View):
  def get(self, request):
    return render(request, 'crypto/landing.html')







