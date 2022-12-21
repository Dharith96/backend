from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sinin(request):
    return render(request=request, template_name='templates/signin.html')

def home(request):
    return render(request=request, template_name='templates/home.html')

def contactus(request):
    return render(request=request, template_name='templates/contactus.html')

def lasvegas(request):
    return render(request=request, template_name='templates/lasvegas.html')

def signup(request):
    return render(request=request, template_name='templates/signup.html')

def detail(request, location_id):
    return HttpResponse("<h2> You're looking at the Location id :  %s. </h2>" % location_id)
