# Generated by Django 5.0 on 2024-01-08 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_book_package_address_book_package_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_package',
            name='pid',
        ),
    ]