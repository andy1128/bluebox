from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from users.forms import RegisterForm, PaymentForm, LoginForm, ForgotForm
from catalog.forms import IndexForm
from django.contrib.auth import authenticate, login
from users.models import Users

# This function obtains the data submitted by the user, passes the data through the .is_valid class which makes sure the data is consistent with the backend
# and prints the data to command prompt, thus demonstrating that we are currently receiving user data.
def Register(request):
        if request.method == 'POST':
                formRegister = RegisterForm(request.POST)
                formPayment = PaymentForm(request.POST)
                if formRegister.is_valid() and formPayment.is_valid(): #.is_valid() is a method that checks to make sure that the data is correct.
                        name = formRegister.cleaned_data['name'] # cleaned data are stored in variables that can be called. 
                        lastName = formRegister.cleaned_data['lastName']
                        email = formRegister.cleaned_data['email']
                        userName = formRegister.cleaned_data['userName']
                        password = formRegister.cleaned_data['password']
                        DOB = formRegister.cleaned_data['DOB']
                        cardNum = formPayment.cleaned_data['cardNum']
                        expirationDate = formPayment.cleaned_data['expirationDate']
                        ccvNum = formPayment.cleaned_data['ccvNum']
                        formRegister.save() # This method pushes data into the database
                        formPayment.save()
                        return HttpResponseRedirect('login.html')
                else:
                        return render(request, 'users/register.html', {'formRegister': formRegister, 'formPayment': formPayment} )

        formRegister = RegisterForm()
        formPayment = PaymentForm()
        return render(request, 'users/register.html', {'formRegister': formRegister, 'formPayment': formPayment})

def Login(request):
        if request.method == 'POST':
                form = LoginForm(request.POST)
                if form.is_valid():
                        userName = form.cleaned_data['userName']
                        password = form.cleaned_data['password']
                        testVar = userName # get user input from website
                        testVar2 = password # get user input from website

                for i in Users.objects.all():
                        if testVar == i.userName and testVar2 == i.password:
                                return HttpResponseRedirect('/bluebox/index')
                        else:
                                return render(request, 'users/login.html', {'form': form})

        form = LoginForm()
        return render(request, 'users/login.html', {'form': form} )

def Forgot(request):
        if request.method == 'POST':
                form = ForgotForm(request.POST)
                if form.is_valid():
                        email = form.cleaned_data['email']
                        testVar = email
                
                for i in Users.objects.all():
                        if testVar == i.email:
                                return HttpResponseRedirect('login.html')
                        else:
                                return render(request, 'users/forgot.html', {'form': form})
        form = ForgotForm()
        return render(request, 'users/forgot.html', {'form': form} )


