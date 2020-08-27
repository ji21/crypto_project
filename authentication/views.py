from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
# Create your views here.
class LoginView(View):
  def get(self, request):
    return render(request, 'authenticate/login.html')


class RegView(View):
  def get(self, request):
    return render(request, 'authenticate/register.html')

class UserValidView(View):
  def post(self, request):
    data = json.loads(request.body)
    username = data['username']

    if not str(username).isalnum():
      return JsonResponse({'username_error': 'username should only contain alphabets or numbers'})
    return JsonResponse({'username_valid', True})
