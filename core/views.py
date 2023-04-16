from django.shortcuts import render, redirect
from .models import Usuario
from .forms import ClientForm


# Create your views here. aca se debe crear una nueva funcion para la nueva landig

#class usuario:
#    def _init_(self, correo, contraseña):
#        self.correo=correo
#        self.contraseña=contraseña


def index(request):
    return render(request, 'core/index.html')

def Contacto(request):
     return render(request, 'core/Contacto.html')


def iniciarsesion(request):
     return render(request, 'core/iniciarsesion.html')

def productos(request):
    return render(request, 'core/productos.html')

def Crearcuenta(request):
    return render(request, 'core/Crearcuenta.html')

def EditarPerfil(request):
    return render(request, 'core/EditarPerfil.html')

def carritoCompras(request):
    return render(request, 'core/carritoCompras.html')

def form_cliente(request):
    datos = {
        'form': ClientForm()
    }
    if request.method=='POST':
        formulario= ClientForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
    return render(request, 'core/Crearcuenta.html', datos)

    
