from django.urls import path
from . import views

urlpatterns = [
    path('signin/', view=views.sinin, name='sinin'),
    path('', view=views.home, name='home'),
]