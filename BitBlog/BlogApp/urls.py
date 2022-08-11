from django.urls import path
from BlogApp import views

urlpatterns = [
    path('', views.index),
    
    #CRIPTOS¬
    path('cripto/index', views.index_c),
    path('cripto/listado', views.listado_c),
]