from .views import UserValidView, EmailValidView, LoginView, ResetView, RegView, EmailVerficationView, LogoutView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  path('register/', csrf_exempt(RegView.as_view()), name="register"),
  path('login/', csrf_exempt(LoginView.as_view()), name="login"),
  path('reset-password/', ResetView.as_view(), name="reset"),
  path('logout/', LogoutView.as_view(), name="logout"),
  path('validate-username/', csrf_exempt(UserValidView.as_view()), name="validate-username"),
  path('validate-email/', csrf_exempt(EmailValidView.as_view()), name="validate-email"),
  path('activate/<uid>/<token>', EmailVerficationView.as_view(), name="activate"),
  path('error/<uid>/<token>', EmailVerficationView.as_view(), name="error")
]
