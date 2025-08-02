from django.db import models
from django.contrib.auth.models import User
class todo(models.Model):
    task=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(null=True,default=None)
    

# Create your models here.
