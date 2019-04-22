from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    last = models.CharField(max_length=200, verbose_name='Last')
    userName = models.CharField(max_length=200, verbose_name='User Name')
    password = models.CharField(max_length=50, verbose_name='Password')
    CCVNumber = models.IntegerField(verbose_name='CCV Number')
    expirationDate = models.DateField(verbose_name='Expiration Date')
    DOB = models.DateField(verbose_name='Date of Birth')

    #__str__() method to return a human-redable string for each object.
    def __str__(self):
        return self.name


    