from django.urls import path
from catalog import views

#URL routing of website to the main page
urlpatterns = [
    path('index/', views.index, name='bluebox-home' ),
  ]