from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class mydb(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    grade=models.IntegerField()
class verify(models.Model):
    user_name=models.CharField(max_length=50,primary_key=True)
    password=models.IntegerField()
class users(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=12)
    gmail=models.EmailField()
    
