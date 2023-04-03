import imp
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class NewTask(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task =models.CharField(max_length=20)
    completed =models.BooleanField(default=False)
    data = models.DateTimeField(auto_now=True)
    date_create = models.DateTimeField(auto_now_add=True)  