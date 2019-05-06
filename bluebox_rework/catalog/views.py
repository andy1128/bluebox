from django.shortcuts import render
#Connects the database to the website. Need code to actually display data.
from catalog.models import Movie
from catalog.forms import CheckoutForm, IndexForm



# Create your views here.
# def index(request):
#     return render(request, 'catalog/index.html')

def Index(request):

    template_name = 'catalog/index.html'
    form = IndexForm()
    movies = Movie.objects.all()
    

    # print(movies)

    args = {'form': form, 'movies': movies}


    return render(request, template_name, args)
    if request.method == 'GET':
        formSearch = IndexForm(request.GET)
        if formSearch.is_valid():
            search = formSearch.cleaned_data['search']
            testVar = search
        testList = list()
        for i in Movie.objects.all():
            if testVar in i.title:
                testList.append(str(i.img_r))
            if testVar in i.year:
                testList.append(str(i.year))
            if testVar in i.director:
                if i.img_r not in testList:
                    testList.append(str(i.img_r))
            if testVar in i.actors:
                if i.img_r not in testList:
                    testList.append(str(i.img_r))
            if testVar in i.genre:
                if i.img_r not in testList:
                    testList.append(str(i.img_r))
            if i.title == "Good Will Hunting":
                print(testList)
            #return testList
            if len(testList) == 0:
                print("No movies avaialable")
    
   

    # formSearch = IndexForm()
    # return render(request, template_name, {'form': formSearch})

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