# Generated by Django 4.1 on 2022-09-27 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0005_alter_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
