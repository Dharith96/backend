from django.db import models

class Location(models.Model) :
    city = models.CharField(max_length=250)
    def __str__(self) : 
       return self.city
    

class Hotels(models.Model) :
    Location = models.ForeignKey(Location, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=500)


