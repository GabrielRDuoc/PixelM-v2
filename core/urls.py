from django.urls import path
from .views import *
#para agregar nuevas path de url hay que agregar una coma al diccionario urlpatterns y seguir el formato descrito
urlpatterns ={
    path('', index,name="index")
     
}