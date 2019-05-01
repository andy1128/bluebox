from django.db import models


# Create your models here.
class Card(models.Model):
    cardNum = models.IntegerField(verbose_name='Card Number')
    expirationDate = models.DateField(verbose_name='Expiration Date')
    ccvNum = models.IntegerField(max_length=3, verbose_name='CCV Num')

class Transaction(models.Model):
    transactionID = models.IntegerField(verbose_name='Transaction ID')
    title = models.CharField(max_length=200, verbose_name='Title')
    name = models.CharField(max_length=200, verbose_name='Name')
    lastName = models.CharField(max_length=200, verbose_name='Last Name')
    email = models.CharField(max_length=50, verbose_name='E-Mail')
    userName = models.CharField(max_length=200, verbose_name='User Name')
    cardNum = models.IntegerField(verbose_name='Card Number')
    expirationDate = models.DateField(verbose_name='Expiration Date')
    purchaseDate = models.DateField(verbose_name='Date of Purchase')
    sd_price = models.CharField(max_length=10, verbose_name='Price of SD Movie', null=False)
    hd_price = models.CharField(max_length=10, verbose_name='Price of HD Movie', null=False)

    #__str__() method to return a human-redable string for each object.
    def __str__(self):
        return self.transactionID

class Users(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    lastName = models.CharField(max_length=200, verbose_name='Last Name')
    email = models.CharField(max_length=50, verbose_name='E-Mail')
    userName = models.CharField(max_length=200, verbose_name='User Name')
    password = models.CharField(max_length=50, verbose_name='Password')
    cardNum = models.ForeignKey(to=Card, verbose_name='Card Number', on_delete=models.CASCADE)
    DOB = models.DateField(verbose_name='Date of Birth')
    transactionID = models.ForeignKey(to=Transaction, verbose_name='Transaction ID', on_delete=models.CASCADE)

    #__str__() method to return a human-redable string for each object.
    def __str__(self):
        return self.name
    




