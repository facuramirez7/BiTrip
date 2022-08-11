from django.shortcuts import render, redirect
from django.http import HttpResponse

from BlogApp.models import Noticia, Cripto, Nft
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

def index(request):
    return render(request, "BlogApp/index.html")


