# Generated by Django 5.0 on 2024-01-08 12:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_remove_book_package_pid_remove_book_package_uid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='book_package',
            name='pid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.package'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book_package',
            name='uid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
