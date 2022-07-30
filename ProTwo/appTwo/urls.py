from django.contrib import admin
from appTwo import views
from django.urls import path

urlpatterns = [
    path('users/',views.users,name='NewUser'),
    path('thank/',views.thank,name='thank'),


]
