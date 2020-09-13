from django.contrib import admin

# Register your models here.
from .models import Transaction
from .models import Account


admin.site.register(Transaction)
admin.site.register(Account)
