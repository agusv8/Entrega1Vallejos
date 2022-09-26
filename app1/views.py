from mailbox import NoSuchMailboxError
from django.shortcuts import render
from app1.form import *
from django.http import HttpResponse
from app1.models import *

def inicio(request):
    return render(request, "app1/inicio.html")

def empleados(request):
    return render(request, "app1/empleados.html")

def aspirantes(request):
    return render(request, "app1/aspirantes.html")

def productos(request):
    return render(request, "app1/productos.html")

def formempleado(request):
      if request.method == "POST":
            
            formulario1 = Formularioempleado(request.POST)
            if formulario1.is_valid():
                  info = formulario1.cleaned_data
                  empleadof = Empleados(nombre = info["nombre"], edad = info["edad"], cargos = info["cargos"])
                  empleadof.save()
                  return render (request, "app1/empleadocreado.html")

      else: 
            formulario1 = Formularioempleado()
            
      return render (request, "app1/crearempleado.html", {"formempleado":formulario1})

def formproducto(request):
      if request.method == "POST":
            
            formulario2 = Formularioproducto(request.POST)
            if formulario2.is_valid():
                  info = formulario2.cleaned_data
                  productof = Productos(nombre = info["nombre"], codigo = info["codigo"], vto = info["vto"])
                  productof.save()
                  return render (request, "app1/productocreado.html")

      else: 
            formulario2 = Formularioproducto()
            
      return render (request, "app1/crearproducto.html", {"formproducto":formulario2})

def formaspirante(request):
      if request.method == "POST":
            
            formulario3 = Formularioaspirante(request.POST)
            if formulario3.is_valid():
                  info = formulario3.cleaned_data
                  aspirantef = Aspirantes(nombre = info["nombre"], edad = info["edad"], ingreso = info["ingreso"])
                  aspirantef.save()
                  return render (request, "app1/aspirantecreado.html")

      else: 
            formulario3 = Formularioaspirante()
            
      return render (request, "app1/crearaspirante.html", {"formaspirante":formulario3})


def busquedaempleado(request):
      if request.GET["cargos"]:
            busqueda = request.GET["cargos"]
            empleado =  Empleados.objects.filter(cargos__icontains=busqueda)
            return render(request, "app1/resultadosemp.html", {"empleado":empleado, "busqueda":busqueda})
      else:
            mensaje = "No enviaste datos"
      
      return HttpResponse(mensaje)

def busquedaaspirante(request):
      if request.GET["nombre"]:
            busqueda2 = request.GET["nombre"]
            aspirante = Aspirantes.objects.filter(nombre__icontains=busqueda2)
            return render (request, "app1/resultadosasp.html", {"aspirante":aspirante, "busqueda2":busqueda2})
      else:
            respuesta = "No enviaste datos"
      return HttpResponse (respuesta)


def busquedaproducto(request):
      if request.GET["codigo"]:
            busqueda3 = request.GET["codigo"]
            producto = Productos.objects.filter(codigo__icontains=busqueda3)
            return render (request, "app1/resultadospro.html", {"producto":producto, "busqueda3":busqueda3})
      else:
            respuesta = "No enviaste datos"
      return HttpResponse (respuesta)


def resuemp(request):
      return render(request, "app1/resultadosemp.html")

def resuasp(request):
      return render(request, "app1/resultadosasp.html")

def resupro(request):
      return render(request, "app1/resultadospro.html")
