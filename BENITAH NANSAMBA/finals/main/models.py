from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Login(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=128,default='temporary_default_password',null=True)
    
    def __str__(self):
        return self.user.username
    

class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=256)