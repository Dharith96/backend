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


class City(models.Model):
    cityname=models.CharField(max_length=250)
    def __str__(self):
        return self.cityname

class Hotel(models.Model):
    city=models.ForeignKey(City, on_delete=models.CASCADE)
    hotelname=models.CharField(max_length=250)
    def __str__(self):
        return self.hotelname

class Room(models.Model):
    hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room=models.CharField(max_length=250)
    def __str__(self):
        return self.room
