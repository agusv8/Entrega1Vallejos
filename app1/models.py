from django.db import models

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
