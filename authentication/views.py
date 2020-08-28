from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from validate_email import validate_email
from .models import Profile
import json
# Create your views here.
class LoginView(View):
  def get(self, request):
    return render(request, 'authenticate/login.html')


class RegView(View):
  def get(self, request):
    return render(request, 'authenticate/register.html')

  def post(self, request):

    username = request.POST['username']
    email = request.POST['email']
    full_name = request.POST['fullname']
    password = request.POST['password']
    phone = request.POST['phone']

    if not User.objects.filter(username=username).exists():
      if not User.objects.filter(email=email).exists():
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        messages.success(request, 'Your account has been successfully created.')
        return render(request, 'authenticate/register.html')
      else:
        messages.error(request, 'Email already in use. Please use another email.')
    if User.objects.filter(username=username).exists():
      messages.error(request, 'Username has already been taken. Please choose another one.')
    return render(request, 'authenticate/register.html')



class UserValidView(View):
  def post(self, request):
    data = json.loads(request.body)
    username = data['username']

    if not str(username).isalnum():
      return JsonResponse({'username_error': 'Username should not contain any non-alphanumerical characters.'}, status=400)
    elif User.objects.filter(username=username).exists():
      return JsonResponse({'username_error': 'Username has already been taken.'}, status=400)
    return JsonResponse({'username_valid': True})


class EmailValidView(View):
  def post(self, request):
    data=json.loads(request.body)
    email = data['email']

    if User.objects.filter(email=email).exists():
      return JsonResponse({'email_error': 'Email has already been taken.'}, status=400)
    elif validate_email(email):
      return JsonResponse({'email_valid': True})
    return JsonResponse({'email_error': 'Email format is invalid.'}, status=400)
