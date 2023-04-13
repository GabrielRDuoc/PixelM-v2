from django.shortcuts import render

# Create your views here. aca se debe crear una nueva funcion para la nueva landig
def index(request):
    return render(request, 'core/index.html')
