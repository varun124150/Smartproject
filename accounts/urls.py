from django.urls import path
from django.contrib import admin
from .views import register,home,loginPage
urlpatterns = [


   path('',home),
   path('register/',register, name='register'),
   path('login/',loginPage, name='login'),
    path('home/',home, name='home')



]
