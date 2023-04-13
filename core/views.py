from django.shortcuts import render

# Create your views here. aca se debe crear una nueva funcion para la nueva landig
def index(request):
    return render(request, 'core/index.html')
def iniciarsesion(request):
    return render(request, 'core/iniciarsesion.html')
def contacto(request):
    return render(request, 'core/contacto.html')