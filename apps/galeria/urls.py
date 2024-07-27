from django.urls import path
from apps.galeria.views import index, imagem, buscar, buscartag, curtir, maisviews, novas, surpresa
from apps.galeria.views import nova_imagem, editar_imagem, deletar_imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:id>', imagem, name='imagem'),
    path('buscar/', buscar, name='buscar'),
    path('buscartag/<str:tag>', buscartag, name='buscartag'),
    path('curtir/<int:id>', curtir, name='curtir'),
    path('maisviews/', maisviews, name='maisviews'),
    path('novas/', novas, name='novas'),
    path('surpresa/', surpresa, name='surpresa'),
    path('nova-imagem/', nova_imagem, name='nova_imagem'),
    path('editar-imagem/<int:id>', editar_imagem, name='editar_imagem'),
    path('deletar-imagem/<int:id>', deletar_imagem, name='deletar_imagem'),
]
