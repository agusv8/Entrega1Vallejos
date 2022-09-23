from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=60)
    codigo = models.IntegerField()
    vto = models.DateField()

class Empleados(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    cargos = models.CharField(max_length=60)

class Aspirantes(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    ingreso = models.DateField()
