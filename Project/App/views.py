from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'App/index.html')

def aboutUs(request):
    return render(request, 'App/aboutUs.html')

def contactUs(request):
    return render(request, 'App/contactUs.html')

def gallery(request):
    return render(request, 'App/gallery.html')

def resources(request):
    return render(request, 'App/resources.html')