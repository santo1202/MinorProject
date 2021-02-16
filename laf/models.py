from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    Your_Name = models.CharField(max_length=70)
    Item_Lost = models.CharField(max_length=100, default='')
    Description_of_Item = models.CharField(max_length=34, default='')
    Email = models.CharField(max_length=100)
    Phone_No = models.CharField(max_length=12)
    Location_Lost = models.CharField(max_length=200)
    Date_Lost = models.DateTimeField( default=datetime.datetime.now())
    Photo = models.ImageField(upload_to="myimage")
    Date = models.DateTimeField(auto_now_add=True)

class Founder(models.Model):
    Your_Name = models.CharField(max_length=70)
    Item_Found = models.CharField(max_length=100, default='')
    Description_of_Item = models.CharField(max_length=34, default='')
    Email = models.CharField(max_length=100)
    Phone_No = models.CharField(max_length=12, default="")
    Location_Found = models.CharField(max_length=200)
    Date_Found = models.DateTimeField( default=datetime.datetime.now())
    Photo = models.ImageField(upload_to="myimage")
    Date = models.DateTimeField(auto_now_add=True)
  

