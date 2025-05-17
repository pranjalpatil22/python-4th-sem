from django.shortcuts import render, redirect, get_object_or_404
from .models import Flight, Passenger, CheckIn
from .forms import FlightForm, PassengerForm, CheckInForm
import random


def home(request):
    return render(request, 'airport/home.html')


# FLIGHT VIEWS

def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'airport/flight_list.html', {'flights': flights})

def flight_add(request):
    form = FlightForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('flight_list')
    return render(request, 'airport/flight_form.html', {'form': form})

def flight_edit(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    form = FlightForm(request.POST or None, instance=flight)
    if form.is_valid():
        form.save()
        return redirect('flight_list')
    return render(request, 'airport/flight_form.html', {'form': form})

def flight_delete(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == 'POST':
        flight.delete()
        return redirect('flight_list')
    return render(request, 'airport/flight_confirm_delete.html', {'flight': flight})


# PASSENGER VIEWS

def passenger_list(request):
    passengers = Passenger.objects.all()
    return render(request, 'airport/passenger_list.html', {'passengers': passengers})   

def passenger_add(request):
    form = PassengerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('passenger_list')
    return render(request, 'airport/passenger_form.html', {'form': form})

def passenger_edit(request, pk):
    passenger = get_object_or_404(Passenger, pk=pk)
    form = PassengerForm(request.POST or None, instance=passenger)
    if form.is_valid():
        form.save()
        return redirect('passenger_list')
    return render(request, 'airport/passenger_form.html', {'form': form})

def passenger_delete(request, pk):
    passenger = get_object_or_404(Passenger, pk=pk)
    if request.method == 'POST':
        passenger.delete()
        return redirect('passenger_list')
    return render(request, 'airport/passenger_confirm_delete.html', {'passenger': passenger})


# CHECK-IN VIEWS

def checkin_list(request):
    checkins = CheckIn.objects.all()
    return render(request, 'airport/checkin_list.html', {'checkins': checkins})

def checkin_add(request):
    form = CheckInForm(request.POST or None)
    if form.is_valid():
        checkin = form.save(commit=False)
        
        # Assign auto seat number (basic logic — can be improved)
        existing = CheckIn.objects.filter(flight=checkin.flight).count()
        checkin.seat_number = existing + 1
        checkin.save()
        return redirect('checkin_list')
    return render(request, 'airport/checkin_form.html', {'form': form})


def checkin_delete(request, pk):
    checkin = get_object_or_404(CheckIn, pk=pk)
    if request.method == 'POST':
        checkin.delete()
        return redirect('checkin_list')
    return render(request, 'airport/checkin_confirm_delete.html', {'checkin': checkin})

