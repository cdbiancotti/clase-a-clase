from django import forms
import django

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class FormularioEstudiante(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
        

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        help_texts = {k: '' for k in fields}