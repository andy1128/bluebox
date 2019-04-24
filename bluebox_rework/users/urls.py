from django.urls import path
from users import views

#URL Patterns
urlpatterns = [
    path('login/', views.login, name = 'bluebox-login'),
    path('login/register.html', views.register, name = 'bluebox-register'),
    path('login/forgot.html', views.forgot, name = 'bluebox-forgot'),
    path('test/testRegister.html', views.testRegister, name = 'test'),
    path('test/testLogin.html', views.testLogin, name = 'Test Login' ),
    path('test/testForgot.html', views.testForgot, name = 'Test Forgot'),

]
  