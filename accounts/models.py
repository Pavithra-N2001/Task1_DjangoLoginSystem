from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_doctor=models.BooleanField(default=False)
    is_patient=models.BooleanField(default=False)
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    image = models.ImageField()
    uname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=8)
    address=models.CharField(max_length=100)
    
class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    image = models.ImageField()
    uname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=8)
    address=models.CharField(max_length=100)


