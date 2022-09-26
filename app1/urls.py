from django.urls import path
from app1 import views
app_name = '<app1>'

urlpatterns = [
    path('',views.inicio, name="inico"),
    path('aspirantes/',views.aspirantes, name="aspirantes"),
    path('empleados/',views.empleados, name="empleados"),
    path('productos/',views.productos, name="productos"),
    path('crearaspirante/',views.formaspirante, name="crearaspirante"),
    path('crearproducto/',views.formproducto, name="crearproducto"),
    path('crearempleado/',views.formempleado, name="crearempleado"),
    path('busquedaemp/',views.buscarempleado, name="busquedaemp"),
    path('busquedaasp/',views.buscaraspirante, name="busquedaasp"),
    path('busquedapro/',views.buscarproducto, name="busquedapro"),
    path('resuemp/',views.busquedaempleado, name="resuemp"),
    path('resuasp/',views.busquedaaspirante, name="resuasp"),
    path('resupro/',views.busquedaproducto, name="resupro"),
  
]