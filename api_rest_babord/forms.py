from django import forms
from django.utils.timezone import now
from api_rest_babord.models import *
from django.contrib.auth.models import User
from django_select2.forms import HeavySelect2Widget, ModelSelect2Widget,Select2Widget

def data(param):
    return {"q":"test"}

class ConcertForm(forms.ModelForm):

    class Meta:
        model = Concert
        fields = '__all__'
        exclude = ['groupe', 'valider']
    
    intitule = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'intitule du concert', 
            'class': 'form-control'
        }),
        max_length=100
    )
    
    date_debut = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={
            'placeholder': 'Date du début', 
            'class': 'form-control',
            'type': 'date',
        })
    )

    lieu = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Lieu du concert', 
            'class': 'form-control'
        })
    )

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = '__all__'
        exclude = ['groupe', 'valider']

    libelle = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'libelle de l\'album', 
            'class': 'form-control'
        }),
        max_length=100
    )

    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Description de l\'album', 
            'class': 'form-control'
        })
    )

    date_sortie = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={
            'placeholder': 'Date de sortie', 
            'class': 'form-control',
            'type': 'date',
        })
    )

    lieu = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Lieu de l\'album', 
            'class': 'form-control'
        })
    )