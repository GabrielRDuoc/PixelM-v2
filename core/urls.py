from django.urls import path
from .views import *
#para agregar nuevas path de url hay que agregar una coma al diccionario urlpatterns y seguir el formato descrito
urlpatterns = [
    path('', index,name="index"),
    path('Contacto', Contacto, name="Contacto"),
    path('iniciarsesion/', iniciarsesion, name="iniciarsesion"),
    path('productos/', productos, name="productos"),
    path('Crearcuenta/', Crearcuenta, name="Crearcuenta"),
     path('EditarPerfil', EditarPerfil, name="EditarPerfil"),
    path('carritoCompras/', carritoCompras, name="carritoCompras")


]