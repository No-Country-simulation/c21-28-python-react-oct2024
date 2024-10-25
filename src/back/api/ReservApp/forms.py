from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput,PasswordInput
from django.contrib.auth.forms  import AuthenticationForm

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    
    class Meta:
        model= User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        
        help_texts = {k:'' for k in fields}

class LoginForm(AuthenticationForm):
    username= forms.CharField(widget=TextInput())
    password= forms.CharField(widget=PasswordInput())