from django.conf import settings
from django.db import models
from django.utils import timezone

# Modelos
class Juego(models.Model):
    titulo = models.CharField(max_length=200)
    desarrollador = models.CharField(max_length=200)
    resena = models.TextField()
    fecha_lanzamiento = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo


class Personaje(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Nivel(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    dificultad = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
