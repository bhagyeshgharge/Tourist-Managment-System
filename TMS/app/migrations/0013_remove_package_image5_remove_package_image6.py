# Generated by Django 5.0 on 2024-01-05 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_package_enddate_package_startdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='Image5',
        ),
        migrations.RemoveField(
            model_name='package',
            name='Image6',
        ),
    ]
