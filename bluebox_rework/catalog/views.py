from django.shortcuts import render
#Connects the database to the website. Need code to actually display data.
from catalog.models import Movies


# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')

def testIndex(request):
    if request.method == 'GET': #If the form is submitted
        search_query = request.GET.get('search_box', None) #Obtain the value from the search box and asssign it to search_query
        print(search_query)
    return render(request, 'catalog/testIndex.html')

