from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from .models import Account
from django.views import View
import json
# Create your views here.
class AccountView(View):
  def get(self, request):
    account_set = self.request.user.accounts.all()
    if len(account_set) == 0:
      context = {
        'accounts': False
      }
    else:
      context = {
        'accounts': account_set
      }
    return render(request, 'accounts/accounts.html', context)

  def post(self, request):
    data = json.loads(request.body)
    print(self.request.user)
    name = data['name']

    check = Account.objects.filter(name=name)

    print("...............", check)

    if len(check) > 1:
      name = name + f' ({len(check)})'

    account = Account(user=self.request.user, name=name)
    account.save()
    return JsonResponse({'success': 'good'})

  def delete(self, request):
    data = json.loads(request.body)
    print(data['id'])
    account_id = data['id']
    Account.objects.get(pk=account_id).delete()
    return JsonResponse({'success': 'account deleted'})

class InfoView(View):
  def get(self, request):
    return render(request, 'accounts/info.html')
