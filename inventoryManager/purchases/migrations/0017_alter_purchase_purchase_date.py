# Generated by Django 4.1 on 2022-09-28 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0016_alter_purchase_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase_date',
            field=models.DateField(default='2022/09/28'),
        ),
    ]