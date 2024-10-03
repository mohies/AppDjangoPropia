from django.urls import path
from . import views
urlpatterns = [
    path('',views.juegos_list,name='juegos_list'),
    path('juego',views.juegos_list,name='juegos_list'),
    path('personaje',views.personajes_list,name='personajes_list'),
    path('nivel',views.niveles_list,name='niveles_list'),
]