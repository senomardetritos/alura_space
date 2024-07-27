from django.shortcuts import render, redirect, get_object_or_404
from galeria.models import Fotografia
from random import choice


def index(request):
    fotos = Fotografia.objects.order_by('id').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotos})


def imagem(request, id):
    fotografia = get_object_or_404(Fotografia, pk=id)
    fotografia.views = fotografia.views + 1
    fotografia.save()
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})


def buscar(request):
    fotos = Fotografia.objects.order_by('-data').filter(publicada=True)
    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            fotos = fotos.filter(nome__icontains=nome_buscar)
    return render(request, 'galeria/buscar.html', {'cards': fotos})


def buscartag(request, tag):
    fotos = Fotografia.objects.order_by('-data').filter(publicada=True)
    if tag:
        fotos = fotos.filter(categoria=tag)
    return render(request, 'galeria/buscar.html', {'cards': fotos})


def curtir(request, id):
    fotografia = get_object_or_404(Fotografia, pk=id)
    fotografia.likes = fotografia.likes + 1
    fotografia.save()
    fotos = Fotografia.objects.order_by('-data').filter(publicada=True)
    return redirect('/')


def maisviews(request):
    fotos = Fotografia.objects.order_by('-views').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotos})


def novas(request):
    fotos = Fotografia.objects.order_by('-data').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotos})


def surpresa(request):
    pks = Fotografia.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    fotografia = get_object_or_404(Fotografia, pk=random_pk)
    fotografia.views = fotografia.views + 1
    fotografia.save()
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})
