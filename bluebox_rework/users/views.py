from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from users.forms import RegisterForm, LoginForm, ForgotForm

# This function obtains the data submitted by the user, passes the data through the .is_valid class which makes sure the data is consistent with the backend
# and prints the data to command prompt, thus demonstrating that we are currently receiving user data.
def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lastName = form.cleaned_data['lastName']   
            email = form.cleaned_data['email']
            userName = form.cleaned_data['userName']
            password = form.cleaned_data['password']
            CCVNumber = form.cleaned_data['CCVNumber']
            expirationDate = form.cleaned_data['expirationDate']
            DOB = form.cleaned_data['DOB']
            print(name, lastName, email, userName, password, CCVNumber, expirationDate, DOB)

    form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(email, password)
    form = LoginForm()
    return render(request, 'users/login.html', {'form': form} )

def Forgot(request):
    if request.method == 'POST':
        form = ForgotForm(request.POST)
        if form.is_valid:
            email = form.cleaned_data['email']
            print(email)
    form = ForgotForm()
    return render(request, 'users/forgot.html', {'form': form} )


