# Generated by Django 4.1 on 2022-10-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_remove_sale_amount_alter_sale_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Bank', 'Bank'), ('M-Pesa', 'M-pesa'), ('Credit Card', 'Credit Card')], max_length=200),
        ),
    ]
