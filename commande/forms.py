from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Filtre(forms.Form):
    alimentation=forms.BooleanField(required=False)
    informatique=forms.BooleanField(required=False)
    sante=forms.BooleanField(required=False)
    autre=forms.BooleanField(required=False)
