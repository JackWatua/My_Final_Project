# Generated by Django 4.1 on 2022-10-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0020_alter_purchasetransaction_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasetransaction',
            name='purchase_date',
            field=models.DateField(default='2022-10-08'),
        ),
    ]
