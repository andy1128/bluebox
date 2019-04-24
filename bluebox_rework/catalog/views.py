from django.shortcuts import render
#Connects the database to the website. Need code to actually display data.
from catalog.models import Movies


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')

