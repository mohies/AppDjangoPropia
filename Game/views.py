from django.shortcuts import render
from .models import *



# Registro de modelos en el admin



def juegos_list(request):
   
    juegos= Juego.objects.all()
    return render(request,'Game/juegos_list.html',{"juegos_mostrar":juegos}) #template no hace falta porque esta sen settings

def personajes_list(request):
   
    personajes= Personaje.objects.all()
    return render(request,'Game/personajes_list.html',{"personajes_mostrar":personajes}) #template no hace falta porque esta sen settings

def niveles_list(request):
   
    niveles= Nivel.objects.all()
    return render(request,'Game/niveles_list.html',{"niveles_mostrar":niveles}) #template no hace falta porque esta sen settings


    