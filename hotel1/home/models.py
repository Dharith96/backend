from django.db import models

# Create your models here.

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
