# Generated by Django 4.1 on 2022-09-27 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_expense_payment_option_alter_expense_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='payment_option',
            new_name='expense_category',
        ),
    ]