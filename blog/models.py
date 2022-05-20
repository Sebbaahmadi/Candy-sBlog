from email.mime import image
from re import T
from django.db import models

# Create your models here.

class Blog (models.Model):
    title=models.CharField(max_length=250 , null=True)
    text=models.TextField(null=True)
    
    

    
