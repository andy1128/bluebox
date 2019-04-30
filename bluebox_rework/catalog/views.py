from django.shortcuts import render
#Connects the database to the website. Need code to actually display data.
from catalog.models import Movie
from catalog.forms import CheckoutForm


# Create your views here.
# def index(request):
#     return render(request, 'catalog/index.html')

def Index(request):
    if request.method == 'GET': #If the form is submitted
        search_query = request.GET.get('search_box', None) #Obtain the value from the search box and asssign it to search_query
        print(search_query)
    return render(request, 'catalog/index.html')

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lastName = form.cleaned_data['lastName']
            CCVNumber = form.cleaned_data['CCVNumber']
            expirationDate = form.cleaned_data['expirationDate']
            print(name, lastName, CCVNumber, expirationDate)

    form = CheckoutForm()
    return render(request, 'catalog/checkout.html', {'form': form})

def viewpage(request):
    return render(request, 'catalog/viewpage.html')