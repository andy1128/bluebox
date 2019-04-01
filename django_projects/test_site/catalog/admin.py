from django.contrib import admin
from catalog.models import Movie, Director, Genre

# Register your models here. Code bellow imports the models and then calls admin.site.register to register each of them.
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Genre)

