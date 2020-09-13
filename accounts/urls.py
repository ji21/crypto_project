from django.urls import path
from .views import AccountView, InfoView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
  path('', csrf_exempt(AccountView.as_view()), name="accounts"),
  path('info/', InfoView.as_view(), name="info")
]
