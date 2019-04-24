from django.urls import path
from users import views

#URL Patterns
urlpatterns = [
    path('test/testRegister.html', views.testRegister, name = 'test'),
    path('test/testLogin.html', views.testLogin, name = 'Test Login' ),
    path('test/testForgot.html', views.testForgot, name = 'Test Forgot'),
]
  