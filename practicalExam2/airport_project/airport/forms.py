from django import forms
from .models import Flight, Passenger, CheckIn

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = '__all__'

class CheckInForm(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = ['passenger', 'flight']
