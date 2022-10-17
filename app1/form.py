from django import forms
from app1.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Formularioempleado(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    cargos = forms.CharField()

class Formularioproducto(forms.Form):
    nombre = forms.CharField()
    codigo = forms.IntegerField()
    vto = forms.DateField()

class Formularioaspirante(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    ingreso = forms.DateField()

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    password1 = forms.CharField(label="Ingrese una contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)
    class Meta():
        model = User 
        fields = ["username", "email", "nombre", "apellido", "password1", "password2"]

class FormularioEditarUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese una contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Escriba su nombre")
    last_name = forms.CharField(label="Escriba su apellido")
    class Meta():
        model = User 
        fields = ["email", "password1", "password2", "first_name", "last_name"]

class AvatarFormulario(forms.ModelForm):
    
    class Meta:

        model = Avatar

        fields = ["imagen"]