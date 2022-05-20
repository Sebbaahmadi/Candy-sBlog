from django.urls import path 
from . import views

urlpatterns = [
    path('About', views.about, name='About'),
    path('', views.Home, name='Home'),
]