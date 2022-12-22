from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import City, Hotel, Room
import datetime
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .forms import signupform



# Create your views here.

def sinin(request):
    return render(request=request, template_name='templates/signin.html')

def home(request):
    return render(request=request, template_name='templates/home.html')

def contactus(request):
    return render(request=request, template_name='templates/contactus.html')

def lasvegas(request):
    return render(request=request, template_name='templates/lasvegas.html')

def hawaii(request):
    return render(request=request, template_name='templates/hawaii.html')

def newyork(request):
    return render(request=request, template_name='templates/newyork.html')

def losangeles(request):
    return render(request=request, template_name='templates/losangeles.html')

def chicago(request):
    return render(request=request, template_name='templates/chicago.html')

def signup(response):
    if response.method == "POST":
        form = signupform(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = signupform()

    return render(response, 'templates/signup.html', {"form": form})

def detail(request, location_id):
    return HttpResponse("<h2> You're looking at the Location id :  %s. </h2>" % location_id)
    
