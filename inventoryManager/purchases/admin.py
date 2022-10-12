from django.contrib import admin
from .models import Purchase, purchaseTransaction
# Register your models here.

admin.site.register(Purchase)
admin.site.register(purchaseTransaction)
