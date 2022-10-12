from django.db import models
from customers.models import Customer
from purchases.models import Purchase

# Create your models here.
class Sale (models.Model):
    SALES_ITEMS = [
        [item.Item, item.Item] for item in Purchase.objects.all()
    ]


    CUSTOMER_CHOICES = [

        [customer.Full_Name, customer.Full_Name] for customer in Customer.objects.all()

    ]

    PAYMENT_METHODS = (
        ('Cash', 'Cash'),
        ('Bank', 'Bank'),
        ('M-Pesa', 'M-pesa'),
        ('Credit Card', 'Credit Card')
    )

    Sales_ID = models.AutoField(primary_key = True)
    Item  = models.CharField(max_length=200, choices = SALES_ITEMS )  
    Quantity = models.IntegerField(default = 0)
    Price = models.IntegerField(default = 0)
    payment_method = models.CharField(max_length = 200, choices=PAYMENT_METHODS, default= 'Cash')
    customer = models.CharField(max_length = 250, choices = CUSTOMER_CHOICES, default= Customer.objects.all()[0].Full_Name)


class sale_transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    date = models.DateField('transacation date')
    amount = models.IntegerField(default=0)
    payment_method = models.CharField(max_length=200)