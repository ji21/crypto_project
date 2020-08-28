from .views import UserValidView, EmailValidView, LoginView, RegView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  path('register/', RegView.as_view(), name="register"),
  path('login/', LoginView.as_view(), name="login"),
  path('validate-username/', csrf_exempt(UserValidView.as_view()), name="validate-username"),
  path('validate-email/', csrf_exempt(EmailValidView.as_view()), name="validate-email")
]
