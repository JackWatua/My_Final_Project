from django.contrib import admin
from .models import Sale, sale_transaction
# Register your models here.
admin.site.register(Sale)
admin.site.register(sale_transaction)
