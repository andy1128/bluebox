from django.urls import path
from catalog import views

#URL routing of website to the main page
urlpatterns = [
    path('index/', views.Index, name='bluebox-index'),
    path('index/checkout.html', views.checkout, name='bluebox-checkout'),
    path('index/viewpage.html', views.viewpage, name='bluebox-viewpage'),
    path('index/logout.html', views.logout, name='bluebox-logout'),
  ]