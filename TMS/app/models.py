from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Admin_Reg(models.Model):
    Name=models.CharField(max_length=60)
    NameUser=models.CharField(max_length=60)
    Email=models.CharField(max_length=60)
    Password=models.CharField(max_length=60)

class Package(models.Model):
    Place=models.CharField(max_length=60)
    Country=models.CharField(max_length=60)
    State=models.CharField(max_length=60)
    Price=models.FloatField()
    Days=models.CharField(max_length=60)
    Night=models.CharField(max_length=60)
    Description=models.CharField(max_length=2000)
    is_active=models.BooleanField(default=True)
    Image=models.ImageField(upload_to='image')
    Image2=models.ImageField(upload_to='image')
    Image3=models.ImageField(upload_to='image')
    Image4=models.ImageField(upload_to='image')
    StartDate=models.CharField(max_length=60,default=None)
    EndDate=models.CharField(max_length=60, default=    None)
    Total_Person = models.IntegerField(default=1)


class Book_Package(models.Model):
    # uid=models.ForeignKey(User,on_delete=models.CASCADE)
    # pid=models.ForeignKey(Package,on_delete=models.CASCADE)
    Name=models.CharField(max_length=60)
    Email=models.CharField(max_length=60)
    Phone_No=models.CharField(max_length=60)
    Address=models.CharField(max_length=200)
    Place=models.CharField(max_length=60)
    Country=models.CharField(max_length=60)
    Price = models.FloatField()
    Total_Person = models.IntegerField(default=1)
    Total_Price = models.FloatField()



class Contact(models.Model):
    Name=models.CharField(max_length=60)
    Email=models.CharField(max_length=60)
    Phone_No=models.CharField(max_length=60)
    Request=models.CharField(max_length=200)
    

    