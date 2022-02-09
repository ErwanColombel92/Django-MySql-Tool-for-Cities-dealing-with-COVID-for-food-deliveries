from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

Departements=( 
    ("1", "Ain"), 
    ("2", "Aisne"), 
    ("3", "Allier"), 
    ("75", "Paris"),
    ("78", "Yvelines"),
    ("91", "Essonne"),
    ("92", "Hauts-de-Seine"),
    ("93", "Seine-Saint-Denis"),
    ("94", "Val-de-Marne"),
    ("95", "Val d'Oise"),
    
    
)
class Activer(forms.Form):
    code = forms.IntegerField()

class InscriptionUser(UserCreationForm):
    email=forms.EmailField()
    
    class Meta:
        model=User
        fields=['last_name','first_name','username','password1','password2','email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        exclude=('compteActive','codeActivation','user')
        