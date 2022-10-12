from django.db import models
from vendors.models import Vendor

from datetime import datetime

# Create your models here.

class Purchase(models.Model):
    PAYMENT_METHODS = (
        ('Cash', 'Cash'),
        ('Bank', 'Bank'),
        ('M-Pesa', 'M-pesa'),
        ('Credit Card', 'Credit Card')
    )
    VENDOR_CHOICES = [
        [v.Full_Name, v.Full_Name] for v in Vendor.objects.all()
    ]
    
    Purchase_ID = models.IntegerField(primary_key=True)
    Item = models.CharField(max_length=200, null=False)
    Quantity = models.IntegerField(default=0)
    Price = models.IntegerField(default=0)
    vendor = models.CharField(max_length=200, choices=VENDOR_CHOICES)
    payment_method = models.CharField(max_length=200, choices=PAYMENT_METHODS, default='Cash')


class purchaseTransaction (models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    Item = models.CharField(max_length=200, null=False)
    Quantity = models.IntegerField(default=0)
    purchase_date = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))
    Price = models.IntegerField(default=0)
    payment_method = models.CharField(max_length=200)