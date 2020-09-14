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
    original_name = data['name']
    check = Account.objects.filter(original_name=original_name)
    name = ''
    print("...............", check)

    if len(check) > 0:
      name = original_name + f' ({len(check)})'
    else:
      name = original_name
    print(">>>>>>>>>>>>>>>>>>>>>>", original_name)
    print("........................", name)
    account = Account(user=self.request.user, name=name, original_name=original_name)
    account.save()
    return JsonResponse({'success': 'good'})

  def delete(self, request):
    data = json.loads(request.body)
    print(data['id'])
    account_id = data['id']
    Account.objects.get(pk=account_id).delete()
    return JsonResponse({'success': 'account deleted'})

class DetailView(View):
  def get(self, request):

    # id = data['id']
    # print("....................................>", request)
    return render(request, 'accounts/details.html')

  def post(self, request):
    data = json.loads(request.body)
    account_id = data['id']
    return self.get


