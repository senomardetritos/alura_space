from django.urls import path
from galeria.views import index, imagem, buscar, buscartag, curtir, maisviews, novas, surpresa

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:id>', imagem, name='imagem'),
    path('buscar/', buscar, name='buscar'),
    path('buscartag/<str:tag>', buscartag, name='buscartag'),
    path('curtir/<int:id>', curtir, name='curtir'),
    path('maisviews/', maisviews, name='maisviews'),
    path('novas/', novas, name='novas'),
    path('surpresa/', surpresa, name='surpresa'),
]
