from django.shortcuts import render
from app1.form import FormularioEditarUsuario, Formularioempleado, Formularioproducto, Formularioaspirante, FormularioRegistro, AvatarFormulario
from django.http import HttpResponse
from app1.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView

def inicio(request):
    return render(request, "app1/inicio.html")
@login_required
def empleados(request):
    return render(request, "app1/Empleados_list.html")
@login_required
def aspirantes(request):
    return render(request, "app1/aspirantes.html")
@login_required
def productos(request):
    return render(request, "app1/productos_list.html")
@login_required
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
@login_required
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
@login_required
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
@login_required
def buscarempleado(request):
      return render(request, "app1/buscarempleado.html")
@login_required
def buscarproducto(request):
      return render(request, "app1/buscarproducto.html")
@login_required
def buscaraspirante(request):
      return render(request, "app1/buscaraspirante.html")
@login_required
def busquedaempleado(request):
      if request.GET["cargos"]:
            busqueda = request.GET["cargos"]
            empleado =  Empleados.objects.filter(cargos__icontains=busqueda)
            return render(request, "app1/resultadosemp.html", {"empleado":empleado, "busqueda":busqueda})
      else:
            mensaje = "No enviaste datos"
      
      return HttpResponse(mensaje)
@login_required
def busquedaaspirante(request):
      if request.GET["nombre"]:
            busqueda2 = request.GET["nombre"]
            aspirante = Aspirantes.objects.filter(nombre__icontains=busqueda2)
            return render (request, "app1/resultadosasp.html", {"aspirante":aspirante, "busqueda2":busqueda2})
      else:
            respuesta = "No enviaste datos"
      return HttpResponse (respuesta)
@login_required
def busquedaproducto(request):
      if request.GET["nombre"]:
            busqueda3 = request.GET["nombre"]
            producto = Productos.objects.filter(nombre__icontains=busqueda3)
            return render (request, "app1/resultadospro.html", {"producto":producto, "busqueda3":busqueda3})
      else:
            respuesta = "No enviaste datos"
      return HttpResponse (respuesta)

def iniciar_sesion(request):
      if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                  usuario = form.cleaned_data.get("username")
                  contra = form.cleaned_data.get("password")

                  user = authenticate(username=usuario, password=contra) 

                  if user != None:
                        login(request, user)
                        return render (request, "app1/bienvenido.html", {"mensaje":f"Hola {user}"})
            else:
                  return render (request, "app1/bienvenido.html", {"mensaje":f"Datos incorrectos!"})
      
      else:
            form = AuthenticationForm()
      
      return render (request, "app1/login.html", {"formu3":form})

def registro(request):
      if request.method == "POST":
            formu = FormularioRegistro(request.POST)

            if formu.is_valid():
                  nombreUsuario = formu.cleaned_data["username"]
                  formu.save()

                  return render(request, "app1/usuariocreado.html", {"mensaje2": f"Usuario {nombreUsuario} creado!"})

      else:
            formu = FormularioRegistro()

      return render (request, "app1/registro.html", {"formu4":formu})

class EmpleadosLista(ListView):
      model = Empleados
class EmpleadoDetalle(DetailView):
      model = Empleados
class EmpleadosUpdate(UpdateView):
      model = Empleados
      success_url = "/app1/empleados/"
      fields = ["nombre","edad", "cargos"]
      def get(self, request, **kwargs):
        if not self.request.user.has_perm("app1.view_aspirantes"):
            return render(request, "app1/adminrequired.html")
        self.object = self.get_object()
        contexto = self.get_context_data(object=self.object)
        return self.render_to_response(contexto)
class EmpleadosBorrar(DeleteView):
      model = Empleados
      success_url = "/app1/empleados/"
      def get(self, request, **kwargs):
        if not self.request.user.has_perm("app1.view_aspirantes"):
            return render(request, "app1/adminrequired.html")
        self.object = self.get_object()
        contexto = self.get_context_data(object=self.object)
        return self.render_to_response(contexto)


class ProductosLista(ListView):
      model = Productos
class ProductosDetalle(DetailView):
      model = Productos
class ProductosUpdate(UpdateView):
      model = Productos
      success_url = "/app1/productos/"
      fields = ["nombre","codigo", "vto"]
class ProductosBorrar(DeleteView):
      model = Productos
      success_url = "/app1/productos/"

class AspirantesLista(ListView):
      model = Aspirantes
class AspirantesDetalle(DetailView):
      model = Aspirantes
class AspirantesUpdate(UpdateView):
      model = Aspirantes
      success_url = "/app1/aspirantes/"
      fields = ["nombre","edad", "ingreso"]
      def get(self, request, **kwargs):
        if not self.request.user.has_perm("app1.view_aspirantes"):
            return render(request, "app1/adminrequired.html")
        self.object = self.get_object()
        contexto = self.get_context_data(object=self.object)
        return self.render_to_response(contexto)
class AspirantesBorrar(DeleteView):
      model = Aspirantes
      success_url = "/app1/aspirantes/"
      def get(self, request, **kwargs):
        if not self.request.user.has_perm("app1.view_aspirantes"):
            return render(request, "app1/adminrequired.html")
        self.object = self.get_object()
        contexto = self.get_context_data(object=self.object)
        return self.render_to_response(contexto)

@login_required
def editarUsuario(request):
      usuarioConectado = request.user
      
      if request.method == "POST":
            formEdicion = FormularioEditarUsuario(request.POST)
            if formEdicion.is_valid():
                  info = formEdicion.cleaned_data
                  usuarioConectado.email = info["email"]
                  usuarioConectado.password1 = info["password1"]
                  usuarioConectado.password2 = info["password2"]
                  usuarioConectado.first_name = info["first_name"]
                  usuarioConectado.last_name = info["last_name"]

                  usuarioConectado.save()
                  return render(request, "app1/inicio.html")
      else:
            formEdicion = FormularioEditarUsuario(initial = {"email":usuarioConectado.email, "nombre": usuarioConectado.first_name, "apellido":usuarioConectado.last_name})
      contexto = {"formEdicion":formEdicion, "UsuarioNombre":usuarioConectado}
      return render(request, "app1/editarUsuario.html", contexto)

@login_required
def crearAvatar(request):
    if request.method == "POST":
        miformulario = AvatarFormulario(request.POST, request.FILES)
        if miformulario.is_valid():
            usuarioActual = User.objects.get(username=request.user)
            avatar = Avatar(user = usuarioActual, imagen=miformulario.cleaned_data["imagen"])
            avatar.save()
            return render(request, "app1/inicio.html")
    else:
        miformulario = AvatarFormulario()
    return render(request, "app1/crearavatar.html", {"miformulario":miformulario})

def acerca(request):
      return render(request, "app1/acercademi.html")

def cuenta(request):
      return render(request, "app1/cuenta.html")