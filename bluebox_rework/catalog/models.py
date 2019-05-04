from django.db import models
# Used to generate Urls by reversing the URL pattern.
from django.urls import reverse 
from django.contrib.auth.models import User
from users.models import Transaction
from django.forms import ModelForm

# SEARCH_CHOICES = (
#     ('Title', 'Description',)
# )

# Create your models here.
# Model representing a movie.
class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    year = models.IntegerField(verbose_name='Year')
    director = models.CharField(max_length=200, verbose_name="Director")
    actors = models.CharField(max_length=1000, verbose_name="Actors")
    link = models.URLField(verbose_name='Youtube Link')
    genre = models.CharField(max_length=100, verbose_name="Genre" )
    img = models.CharField(max_length=300, verbose_name="Image" )
    img_r = models.CharField(max_length=300, verbose_name="Image R" )
    hd_link = models.URLField(verbose_name='HD Link')
    sd_price = models.CharField(max_length=10, verbose_name='Price of SD Movie')
    hd_price = models.CharField(max_length=10, verbose_name='Price of HD Movie')
    transactionID = models.ForeignKey(to=Transaction, verbose_name='Transaction ID', on_delete=models.CASCADE, null=True)


    # __str__() method to return a human-redable string for each object.
    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this movie."""
        return reverse('movie-detail', args=[str(self.id)])

#class SearchForm(ModelForm):
#     class Meta:
#         model = Movies



