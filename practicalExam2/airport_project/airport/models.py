from django.db import models

# Create your models here.


from django.db import models
from django.utils import timezone

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_time = models.DateTimeField()

    def __str__(self):
        return f"{self.flight_number} ({self.origin} → {self.destination})"

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class CheckIn(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=5)
    checkin_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.passenger.name} checked in to {self.flight.flight_number}"

