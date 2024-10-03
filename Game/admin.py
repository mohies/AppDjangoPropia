from django.contrib import admin
from .models import *

# Register your models here.

modelos=[Juego,Personaje,Nivel]

for model in modelos:
    admin.site.register(model)
