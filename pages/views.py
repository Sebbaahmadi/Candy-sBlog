from django.shortcuts import render

# Create your views here.
def Home(request):
    return render (request, 'pages/Home.html')

def about(request):
    return render(request,'pages/about.html')

