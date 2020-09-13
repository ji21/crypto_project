from django.urls import path
from .views import AccountView, DetailView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
  path('', csrf_exempt(AccountView.as_view()), name="accounts"),
  path('details/', DetailView.as_view(), name="details")
]
