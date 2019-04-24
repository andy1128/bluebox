from django.urls import path
from catalog import views

#URL routing of website to the main page
urlpatterns = [
    path('index/', views.index, name='bluebox-home' ),
    path('index/testIndex.html', views.testIndex, name='bluebox-test'),
    path('index/checkout.html', views.checkout, name='bluebox-checkout'),
  ]