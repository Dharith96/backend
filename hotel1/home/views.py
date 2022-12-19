from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sinin(request):
    return render(request=request, template_name='templates/signin.html')

def home(request):
    return render(request=request, template_name='templates/home.html')