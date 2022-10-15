from django.urls import path
from app1 import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.inicio, name="inicio"),
    path('aspirantes/',views.AspirantesLista.as_view(), name="aspirantes"),
    path('empleados/',views.EmpleadosLista.as_view(), name="empleados"),
    path('productos/',views.ProductosLista.as_view(), name="productos"),
    path('crearaspirante/',views.formaspirante, name="crearaspirante"),
    path('crearproducto/',views.formproducto, name="crearproducto"),
    path('crearempleado/',views.formempleado, name="crearempleado"),
    path('busquedaemp/',views.buscarempleado, name="busquedaemp"),
    path('busquedaasp/',views.buscaraspirante, name="busquedaasp"),
    path('busquedapro/',views.buscarproducto, name="busquedapro"),
    path('resuemp/',views.busquedaempleado, name="resuemp"),
    path('resuasp/',views.busquedaaspirante, name="resuasp"),
    path('resupro/',views.busquedaproducto, name="resupro"),
    path('login/', views.iniciar_sesion, name = "Login"),
    path('registro/', views.registro, name = "Registro"),
    path('logout/', LogoutView.as_view(template_name="app1/logout.html"), name = "cerrarsesion"),
    path('empleados/<int:pk>', views.EmpleadoDetalle.as_view(), name = "EmpleadoDetalle"),
    path('empleados/editar/<int:pk>', views.EmpleadosUpdate.as_view(), name = "EditarEmpleado"),
    path('empleados/borrar/<int:pk>', views.EmpleadosBorrar.as_view(), name = "BorrarEmpleado"),
    path('productos/<int:pk>', views.ProductosDetalle.as_view(), name = "ProductosDetalle"),
    path('productos/editar/<int:pk>', views.ProductosUpdate.as_view(), name = "EditarProductos"),
    path('productos/borrar/<int:pk>', views.ProductosBorrar.as_view(), name = "BorrarProductos"),
    path('aspirantes/<int:pk>', views.AspirantesDetalle.as_view(), name = "AspirantesDetalle"),
    path('aspirantes/editar/<int:pk>', views.AspirantesUpdate.as_view(), name = "EditarAspirantes"),
    path('aspirantes/borrar/<int:pk>', views.AspirantesBorrar.as_view(), name = "BorrarAspirantes"),
    path('editarUsuarios', views.editarUsuario, name = "editarUsuarios"),
]