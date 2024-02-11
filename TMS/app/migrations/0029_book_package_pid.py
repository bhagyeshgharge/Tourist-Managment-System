# Generated by Django 5.0 on 2024-01-08 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_remove_book_package_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_package',
            name='pid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.package'),
            preserve_default=False,
        ),
    ]