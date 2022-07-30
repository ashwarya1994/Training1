from django.urls import path
from apptwo import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name = 'help'),
    path('google/', views.google, name = 'google'),
    path('user/', views.users, name = 'user')

]
