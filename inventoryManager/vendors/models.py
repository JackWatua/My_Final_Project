from django.db import models

# Create your models here.
class Vendor (models.Model):
    VENDOR_PRIORITY = [
        ["High", "High"],
        ["Moderate", "Moderate"],
        ["Low", "Low"],
    ]
    Vendor_ID = models.IntegerField(primary_key=True)
    Full_Name = models.CharField(max_length=200)
    Email_Address = models.EmailField('vendor\'s email')
    Phone = models.IntegerField('Vendor\'s phone number')
    Priority = models.CharField(max_length=200, choices=VENDOR_PRIORITY)





