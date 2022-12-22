import datetime

from django.db import models
from django.utils import timezone

class City(models.Model):
    cityname=models.CharField(max_length=250, default="Chicago")
    check_in = models.DateTimeField(default='2022-12-22', verbose_name='Check-in date')
    check_out = models.DateTimeField(default='2023-12-22', verbose_name='Check-out date')
    guest = models.IntegerField(default=0)
    def __str__(self) : 
       return self.cityname
    
class Hotel(models.Model):
    city=models.ForeignKey(City, on_delete=models.CASCADE)
    hotelname=models.CharField(max_length=250)
    def __str__(self):
        return self.hotelname

class Room(models.Model):
    ROOM_TYPE = ( 
    ("1", "One Queen"), 
    ("2", "Two Queen"),
    ("3","One King"),    
    ) 
    hotel=models.ForeignKey(City, on_delete=models.CASCADE)
    roomname=models.CharField(max_length=50,choices = ROOM_TYPE)
    def __str__(self):
        return self.roomname
