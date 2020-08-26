from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
class loginView(View):
  def get(self, request):
    return render(request, 'authenticate/login.html')


class regView(View):
  def get(self, request):
    return render(request, 'authenticate/register.html')
