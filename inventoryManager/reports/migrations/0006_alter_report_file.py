# Generated by Django 4.1 on 2022-10-12 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_alter_report_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='File',
            field=models.FileField(default='test.txt', upload_to='reports'),
        ),
    ]