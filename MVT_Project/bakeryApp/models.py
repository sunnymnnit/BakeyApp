from django.db import models
from django.contrib.auth.models import AbstractUser

class BakeryCards(models.Model):
    cardId=models.IntegerField(default=0)
    title=models.TextField(max_length=100)
    description=models.TextField(max_length=300)
    image=models.TextField(max_length=600,default="")
    rate=models.IntegerField()

class MyCart(models.Model):
    cardId=models.IntegerField(default=0)
    userId=models.IntegerField(default=0)
    numberOfItems=models.IntegerField()

class UserDetails(models.Model):
    userId=models.IntegerField(default=0)
    name=models.TextField(max_length=100)
    email=models.TextField(max_length=100)
    password=models.TextField(max_length=100)
    address=models.TextField(max_length=100)
    mobile=models.TextField(max_length=13)


class User(AbstractUser):
    address = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
