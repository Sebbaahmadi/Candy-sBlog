from django.urls import path 
from .import views

urlpatterns = [
    path('Blog', views.blog, name='Blog'),
   
]