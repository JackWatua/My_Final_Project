# Generated by Django 4.1 on 2022-09-26 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_customer_customer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='Priority',
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_priority',
            field=models.IntegerField(choices=[(1, 'High'), (2, 'Moderate'), (3, 'Low')], default=1),
        ),
    ]
