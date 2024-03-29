# Generated by Django 5.0 on 2024-01-07 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_delete_bookpackage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60)),
                ('Email', models.CharField(max_length=60)),
                ('Phone_No', models.CharField(max_length=60)),
                ('Address', models.CharField(max_length=200)),
                ('Place', models.CharField(max_length=60)),
                ('Country', models.CharField(max_length=60)),
                ('Price', models.FloatField()),
                ('Total_Person', models.IntegerField(default=1)),
                ('Total_Price', models.FloatField()),
            ],
        ),
    ]
