# Generated by Django 4.1 on 2022-09-27 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_alter_expense_payment_method_alter_expense_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='payment_option',
            field=models.CharField(choices=[('Administrative', 'Administrative'), ('Distribution', 'Distribution'), ('Transportation', 'Transportation'), ('Salaries & Wages', 'Salaries & Wages')], default='Administrative', max_length=200),
        ),
        migrations.AlterField(
            model_name='expense',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Expense_transaction',
        ),
    ]
