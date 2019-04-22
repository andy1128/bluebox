from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    userName = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    