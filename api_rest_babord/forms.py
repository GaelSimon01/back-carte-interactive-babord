from django import forms
from django.utils.timezone import now
from api_rest_babord.models import *
from django.contrib.auth.models import User

class ConcertForm(forms.Form):
    
    intitule = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'intitule du concert', 'class': 'form-control'}),
        max_length=100
    )
    date_debut = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'placeholder': 'Date du début', 'class': 'form-control'})
    )