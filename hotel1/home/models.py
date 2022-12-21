import datetime

from django.db import models
from django.utils import timezone

class Location(models.Model) :
    city = models.CharField(max_length=250, default="New York")
    check_in = models.DateTimeField(default='2022-12-22', verbose_name='Check-in date')
    check_out = models.DateTimeField(default='2023-12-22', verbose_name='Check-out date')
    guest = models.IntegerField(default=0)
    def __str__(self) : 
       return self.city
    

class Hotels(models.Model) :
    Location = models.ForeignKey(Location, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=500)
    def __str__(self) : 
       return self.hotel_name


