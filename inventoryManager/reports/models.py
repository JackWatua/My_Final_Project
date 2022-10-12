from pyexpat import model
from django.db import models
from authenticator.models import User
from datetime import datetime

# Create your models here.
class Report (models.Model):
    REPORT_TYPES = (
        ("Task Report", "Task Report"),
        ("Product Report", "Product Report"),
        ("Employee Report", "Employee Report"),
        ("Financial Report", "Financial Report")
    )
    Report_ID = models.IntegerField(primary_key=True)
    Report_title = models.CharField(max_length=200)
    Report_Type = models.CharField(max_length=200, choices=REPORT_TYPES, default= "Task Report")
    File = models.FileField(upload_to= "reports", default="test.txt")
    Date_Created = models.DateField('Date report created', default = datetime.now().strftime("%Y-%m-%d"))