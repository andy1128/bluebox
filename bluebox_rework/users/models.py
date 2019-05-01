from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    lastName = models.CharField(max_length=200, verbose_name='Last Name')
    email = models.CharField(max_length=50, verbose_name='E-Mail')
    userName = models.CharField(max_length=200, verbose_name='User Name')
    password = models.CharField(max_length=50, verbose_name='Password')
    CCVNumber = models.IntegerField(verbose_name='CCV Number')
    expirationDate = models.DateField(verbose_name='Expiration Date')
    DOB = models.DateField(verbose_name='Date of Birth')

    #__str__() method to return a human-redable string for each object.
    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    name = models.CharField(max_length=200, verbose_name='Name')
    lastName = models.CharField(max_length=200, verbose_name='Last Name')
    email = models.CharField(max_length=50, verbose_name='E-Mail')
    userName = models.CharField(max_length=200, verbose_name='User Name')
    CCVNumber = models.IntegerField(verbose_name='CCV Number')
    expirationDate = models.DateField(verbose_name='Expiration Date')
    purchase_date = models.DateField(verbose_name='Date of Purchase')
    sd_price = models.CharField(max_length=10, verbose_name='Price of SD Movie', null=False)
    hd_price = models.CharField(max_length=10, verbose_name='Price of HD Movie', null=False)

    #__str__() method to return a human-redable string for each object.
    def __str__(self):
        return self.name
