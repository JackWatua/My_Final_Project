from django.db import models

# Create your models here.

#create a new user model that captures the business owner's details
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(help_text='User Email')
    phone = models.IntegerField(default=0)
    password = models.CharField(max_length=100)