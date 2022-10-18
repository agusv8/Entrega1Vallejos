from distutils.command.upload import upload
from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User

class Productos(models.Model):
    def __str__(self):
        return (f"Producto {self.nombre}, {self.codigo}")
    nombre = models.CharField(max_length=60)
    codigo = models.IntegerField()
    vto = models.DateField()

class Empleados(models.Model):
    def __str__(self):
        return (f"Empleado {self.nombre}, {self.cargos}")
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    cargos = models.CharField(max_length=60)

class Aspirantes(models.Model):
    def __str__(self):
        return (f"Aspirante {self.nombre}, {self.ingreso}")
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    ingreso = models.DateField()

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
