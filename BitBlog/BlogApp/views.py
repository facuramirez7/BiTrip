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


