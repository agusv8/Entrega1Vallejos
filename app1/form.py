from socket import fromshare
from django import forms

class Formularioempleado(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    cargo = forms.CharField()

class Formularioproducto(forms.Form):
    nombre = forms.CharField()
    codigo = forms.IntegerField()
    vto = forms.DateField()

class Formularioaspirante(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    ingreso = forms.DateField()