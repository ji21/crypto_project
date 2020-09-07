from django.contrib import admin

# Register your models here.
from .models import Profile
from .models import Transaction
from .models import Wallet


admin.site.register(Profile)
admin.site.register(Transaction)
admin.site.register(Wallet)
