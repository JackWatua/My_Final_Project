# Generated by Django 4.1 on 2022-09-27 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0003_remove_purchase_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 9, 27, 17, 18, 42, 703689, tzinfo=datetime.timezone.utc)),
        ),
    ]
