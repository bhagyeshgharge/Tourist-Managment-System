# Generated by Django 5.0 on 2024-01-06 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_bookpackage_total_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='Total_Person',
            field=models.IntegerField(default=1),
        ),
    ]
