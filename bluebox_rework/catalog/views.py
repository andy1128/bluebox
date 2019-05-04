from django.shortcuts import render
#Connects the database to the website. Need code to actually display data.
from catalog.models import Movie
from catalog.forms import CheckoutForm, IndexForm



# Create your views here.
# def index(request):
#     return render(request, 'catalog/index.html')

def Index(request):

    template_name = 'catalog/index.html'

    # Waiting for juan to tell me where the form class for this is
    # form = Movie()

    # movies = Movie.objects.all()
    # movies.get(0)

    # args = {'form': form, 'movies': movies}

    # if request.method == 'GET': #If the form is submitted
    #     search_query = request.GET.get('search_box', None) #Obtain the value from the search box and asssign it to search_query
    #     print(search_query)
    # return render(request, template_name)
    if request.method == 'GET':
        form = IndexForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            print(search)
    form = IndexForm()
    return render(request, template_name, {'form': form})

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