from django.shortcuts import render, redirect
from django.http import HttpResponse

from BlogApp.models import Noticia, Cripto, Nft
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.


#INDEX
def index(request):
    return render(request, "BlogApp/index.html")



#CRIPTOS
def index_c(request):
    return render(request, "BlogApp/criptos/index.html")

def listado_c(request):
    criptos = Cripto.objects.all()
    context = {
         "criptos": criptos
         }
    return render(request, "BlogApp/criptos/listado.html", context)

def create_c(request):
    return render(request, "BlogApp/criptos/create.html")

def create_cr(request):
    if(request.method == 'POST'):
        nombre = request.POST['nombre']
        iso = request.POST['iso']
        precio = request.POST['precio']
        lenguaje = request.POST['lenguaje']
        stable = request.POST['stable']
        cripto = Cripto(nombre = nombre,iso = iso,precio = precio,lenguaje = lenguaje,stable = stable)
        
        cripto.save()
        
        """ context = {
            "mensaje": 'Creado correctamente',
            'error' : 0
            } """
    """ else:
        context = {
            "mensaje": 'No se pudo crear  correctamente',
            'error' : 1
            } """
        
    return render(request, "BlogApp/criptos/index.html")


