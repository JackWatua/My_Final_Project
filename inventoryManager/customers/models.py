from django.db import models








# Create your models here.

class Customer(models.Model):
    High = 1
    Modetare = 2
    Low = 3

    CUSTOMER_PRIORITY = (
        (High, 'High'),
        (Modetare,'Moderate'),
        (Low, 'Low')
    )
    Customer_ID = models.IntegerField(primary_key=True)
    Full_Name = models.CharField(max_length=200, null=False)
    Email_Address = models.EmailField('Enter email', null=False)
    Phone = models.IntegerField()
    customer_priority = models.IntegerField(choices=CUSTOMER_PRIORITY, default = 1)