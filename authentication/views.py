from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.contrib.auth.models import User
from validate_email import validate_email
import json
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

    if str(username).isalnum():
      return JsonResponse({'username_valid': True})
    elif User.objects.filter(username=username).exists():
      return JsonResponse({'username_error': 'Username has already been taken.'}, status=400)
    return JsonResponse({'username_error': 'Username should not contain any non-alphanumerical characters.'}, status=400)

class EmailValidView(View):
  def post(self, request):
    data=json.loads(request.body)
    email = data['email']

    if validate_email(email):
      return JsonResponse({'email_valid': True})
    elif User.objects.filter(email=email).exists():
      return JsonResponse({'email_error': 'Email has already been taken.'}, status=400)
    return JsonResponse({'email_error': 'Email format is invalid.'}, status=400)
