from django.db import models
from datetime import datetime


# Create your models here.
class Expense(models.Model):
    PAYMENT_METHODS = (
        ('Cash', 'Cash'),
        ('Bank', 'Bank'),
        ('M-Pesa', 'M-pesa'),
        ('Credit Card', 'Credit Card')
    )

    EXPENSE_CATEGORIES = (
        ('Administrative', 'Administrative'),
        ('Distribution', 'Distribution'),
        ('Transportation', 'Transportation' ),
        ('Salaries & Wages', 'Salaries & Wages'),
    )


    expense_id = models.IntegerField(primary_key=True)
    title = models.CharField('Expense Title', max_length=200)
    Amount = models.IntegerField('Expense amount', default=0)
    payment_method = models.CharField(max_length=200, choices=PAYMENT_METHODS, default = 'Cash')
    expense_category = models.CharField(max_length=200, choices=EXPENSE_CATEGORIES, default='Administrative')
    Date = models.DateField('Date incurred', default = datetime.now().strftime("%Y-%m-%d"))
    


