from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.contrib.auth.models import User
from authentication.models import Profile

#for email
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from validate_email import validate_email

#to do json.loads()
import json

#uid and token modules
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator

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
    confirm = request.POST['confirm']

    if User.objects.filter(username=username).exists():
      messages.error(request, 'Username has already been taken. Please choose another one.')
      return render(request, 'authenticate/register.html')
    else:
      if email=="":
        messages.error(request, 'Please fill in all required fields.')
      # elif User.objects.filter(email=email).exists():
      #   messages.error(request, 'Email already in use. Please use another email.')
      elif password=="":
        messages.error(request, 'Please fill in all required fields.')
      elif len(password) < 7:
        messages.error(request, 'Your password must be at least six characters long.')
      elif confirm=="":
        messages.error(request, 'Please fill in all required fields.')
      elif password!=confirm:
        messages.error(request, 'Your passwords must match.')
      else:
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.is_active = False
        user.save()

        #sending activation email

        email_subject = 'Activate your account.'

        domain_name = get_current_site(request).domain
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)

        #return reverse()... can be used to render a new page with a dynamic id,
        #but in our case we used it to generate a dynamic string instead

        link = reverse('activate', kwargs={'uid': uid, 'token': token})
        activate_url = "http://" + domain_name + link


        email_body = f'Hello {full_name}, please click on the link below to activate your bytimise account.\n' + activate_url
        e = EmailMessage(
            email_subject,
            email_body,
            'noreply4@testing.com',
            [email],
        )
        e.send(fail_silently=False)
        # send_mail(email_subject, email_body, 'jeffreyip54@gmail.com', [email], fail_silently=False)
        messages.success(request, 'Your account has been successfully created. Please activate it through your email and login.')
      return render(request, 'authenticate/register.html')


#encode uid and get token from ...
class EmailVerficationView(View):
  def get(self, request, uid, token):
    try:
      id = force_text(urlsafe_base64_decode(uid))
      user=User.objects.get(pk=id)
      email = user.email
      if not token_generator.check_token(user, token):
        messages.error(request, 'Your token has expired. Please enter your email below to resend an activation code.')
        return render(request, 'authenticate/error.html')
      elif user.is_active:
        messages.success('Your account is already activated. Please log in.')
        return render(request, 'login')
      user.is_active = True
      user.save()
      messages.success(request, 'Your account has been successfully activated.')
      return redirect('login')
    except Exception as ex:
      pass
    return redirect('register')



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
