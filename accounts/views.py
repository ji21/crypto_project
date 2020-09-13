from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
import json
# Create your views here.
class AccountView(View):
  def get(self, request):
    return render(request, 'accounts/accounts.html')

  def post(self, request):
    data = json.loads(request.body)
    name = data['name']
    return JsonResponse({'success': name})

class InfoView(View):
  def get(self, request):
    return render(request, 'accounts/info.html')
