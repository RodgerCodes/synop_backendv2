from django import forms
from .models import Station, User

class NewStation(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['station_name','station_number', 'district']

class NewUser(forms.ModelForm):
    class Meta:
        model = User
        fields= ['email', 'name', 'password', 'station', 'is_staff', 'is_superuser']


class ReassignForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['station']

class EditStationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['station_number']