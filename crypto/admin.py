from django.contrib import admin

# Register your models here.
from crypto.models import User
from crypto.models import Transaction
from crypto.models import Wallet

class TransactionAdmin(admin.ModelAdmin):
  readonly_fields = ('created',)


admin.site.register(User)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Wallet)
