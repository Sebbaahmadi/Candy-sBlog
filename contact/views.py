from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse

# Create your views here.
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mess=request.POST.get('message')

        contactV=Contact(name=name, email=email, message=mess) 
        contactV.save()
        return HttpResponse("<h1> Thanks you</h1>")
    else:
        return render(request, 'contact/contact.html')