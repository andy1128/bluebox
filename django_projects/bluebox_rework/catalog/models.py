from django.db import models
# Used to generate Urls by reversing the URL pattern.
from django.urls import reverse 
from django.contrib.auth.models import User

# Create your models here.
# Model representing a movie.
class Movies(models.Model):
    movie_title = models.CharField(max_length=200, verbose_name='Title')
    description = models.TextField(verbose_name='Movie Description')
    year = models.IntegerField(verbose_name='Year')
    actor = models.CharField(max_length=1000, verbose_name="Actors' Names")
    director = models.CharField(max_length=200, verbose_name='Director')
    link = models.URLField(verbose_name='Youtube Link')
    genre_name = models.CharField(max_length=100, verbose_name='Genre')

    
    # __str__() method to return a human-redable string for each object.
    def __str__(self):
        return self.movie_title

    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this movie."""
        return reverse('movie-detail', args=[str(self.id)])


