# Generated by Django 4.1 on 2022-09-28 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_delete_vendor_transaction'),
        ('purchases', '0011_remove_purchase_date_purchase_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='vendor',
            field=models.ForeignKey(choices=[], on_delete=django.db.models.deletion.CASCADE, to='vendors.vendor'),
        ),
    ]