from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.inicio, name="inico"),
    path('aspirantes/',views.aspirantes, name="aspirantes"),
    path('empleados/',views.empleados, name="empleados"),
    path('productos/',views.productos, name="productos"),
    path('crearaspirante/',views.formaspirante, name="crearaspirante"),
    path('crearproducto/',views.formproducto, name="crearproducto"),
    path('crearempleado/',views.formempleado, name="crearempleado"),
    path('busquedaemp/',views.buscarempleado, name="busquedaemp"),
    path('busquedaasp/',views.busquedaaspirante, name="busquedaasp"),
    path('busquedapro/',views.busquedaproducto, name="busquedapro"),
    path('resuemp/',views.resuemp, name="resuemp"),
    path('resuasp/',views.resuasp, name="resuasp"),
    path('resupro/',views.resupro, name="resupro"),
  
]