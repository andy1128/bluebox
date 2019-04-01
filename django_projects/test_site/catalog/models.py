from django.db import models
from django.urls import reverse # Used to generate Urls by reversing the URL pattern.

# Create your models here.
class Genre(models.Model):
    """Model representing a movie genre."""
    genre_name = models.CharField(max_length=200, verbose_name='Genre', help_text='Enter a movie genre (e.g. Horror)')

    # __str__() method to return a human-readable string for each object.
    def __str__(self):
        return self.genre_name


# Model representing a movie.
class Movie(models.Model):
    movie_title = models.CharField(max_length=200, verbose_name='Title')
    description = models.TextField(verbose_name='Movie Description')
    year = models.IntegerField(verbose_name='Year')
    actor = models.CharField(max_length=1000, verbose_name="Actors' Names")
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True )
    link = models.URLField(verbose_name='Youtube Link')
    genre_name = models.ManyToManyField(Genre, help_text='Select a genre for this movie ')

    
    # __str__() method to return a human-redable string for each object.
    def __str__(self):
        return self.movie_title

    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this movie."""
        return reverse('movie-detail', args=[str(self.id)])

# Model representing a director.
class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Return the url to access a particular director instance."""
        return reverse('director-detail', args=[str(self.id)])


    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
    
    
