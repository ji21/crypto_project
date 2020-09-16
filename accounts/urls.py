from django.urls import path
from .views import AccountView, TransactionHistoryView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
  path('', csrf_exempt(AccountView.as_view()), name="accounts"),
  path('transaction-history/<int:id>/', csrf_exempt(TransactionHistoryView.as_view()), name="transaction-history")
]
