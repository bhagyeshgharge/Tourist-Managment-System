# Generated by Django 5.0 on 2024-01-05 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_package_image_alter_package_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='Image6',
            field=models.ImageField(default=None, upload_to='image'),
        ),
    ]