from django.urls import path
from users import views

#URL Patterns
urlpatterns = [
    path('login.html', views.Login, name = 'Login Page' ),
    path('register.html', views.Register, name = 'Register Page'),
    path('forgot.html', views.Forgot, name = 'Forgot Page'),
]
