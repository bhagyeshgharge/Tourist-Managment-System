# Generated by Django 5.0 on 2024-01-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_package_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='Image2',
            field=models.ImageField(default=None, upload_to='image'),
        ),
        migrations.AddField(
            model_name='package',
            name='Image3',
            field=models.ImageField(default=None, upload_to='image'),
        ),
        migrations.AddField(
            model_name='package',
            name='Image4',
            field=models.ImageField(default=None, upload_to='image'),
        ),
        migrations.AddField(
            model_name='package',
            name='Image5',
            field=models.ImageField(default=None, upload_to='image'),
        ),
        migrations.AddField(
            model_name='package',
            name='Image6',
            field=models.ImageField(default=None, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='package',
            name='Image',
            field=models.ImageField(default=None, upload_to='image'),
        ),
    ]
