from django.urls import path
from catalog import views

#URL routing of website to the main page
urlpatterns = [
    path('index/', views.Index, name='bluebox-index'),
    path('index/checkout.html', views.checkout, name='bluebox-checkout'),
  ]