# Generated by Django 4.1 on 2022-09-28 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0010_purchase_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='Date',
        ),
        migrations.AddField(
            model_name='purchase',
            name='purchase_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
