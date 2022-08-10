from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    texto = models.CharField(max_length=500)
    imagen = models.CharField(max_length=40)
    fecha = models.DateTimeField
    
class Cripto(models.Model):
    nombre = models.CharField(max_length=40)
    iso = models.CharField(max_length=3)
    precio = models.IntegerField()
    lenguaje = models.CharField(max_length=15)
    stable = models.IntegerField()
    
class Nft(models.Model):
    nombre = models.CharField(max_length=40)
    iso = models.CharField(max_length=3)
    precio = models.IntegerField()

    

    
    
    

