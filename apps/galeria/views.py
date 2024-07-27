from django.shortcuts import render, redirect, get_object_or_404
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages
from random import choice
from datetime import datetime


def index(request):
    if request.user.is_authenticated:
        fotos = Fotografia.objects.order_by('id').filter(publicada=True)
    else:
        fotos = None
    return render(request, 'galeria/index.html', {'cards': fotos})


def imagem(request, id):
    if request.user.is_authenticated:
        fotografia = get_object_or_404(Fotografia, pk=id)
        fotografia.views = fotografia.views + 1
        fotografia.save()
    else:
        fotografia = None
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})


def buscar(request):
    if not request.user.is_authenticated:
        return redirect('index')
    fotos = Fotografia.objects.order_by('-data').filter(publicada=True)
    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            fotos = fotos.filter(nome__icontains=nome_buscar)
    return render(request, 'galeria/index.html', {'cards': fotos})


def buscartag(request, tag):
    if not request.user.is_authenticated:
        return redirect('index')
    fotos = Fotografia.objects.order_by(
        '-data').filter(publicada=True, categoria=tag)
    return render(request, 'galeria/index.html', {'cards': fotos})


def curtir(request, id):
    if not request.user.is_authenticated:
        return redirect('index')
    fotografia = get_object_or_404(Fotografia, pk=id)
    fotografia.likes = fotografia.likes + 1
    fotografia.save()
    fotos = Fotografia.objects.order_by('-data').filter(publicada=True)
    return redirect('/')


def maisviews(request):
    if not request.user.is_authenticated:
        return redirect('index')
    fotos = Fotografia.objects.order_by('-views').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotos})


def novas(request):
    if not request.user.is_authenticated:
        return redirect('index')
    fotos = Fotografia.objects.order_by('-data').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotos})


def surpresa(request):
    if not request.user.is_authenticated:
        return redirect('index')
    pks = Fotografia.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    fotografia = get_object_or_404(Fotografia, pk=random_pk)
    fotografia.views = fotografia.views + 1
    fotografia.save()
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})


def nova_imagem(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        form.instance.usuario = request.user
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova imagem cadastrada')
            return redirect('index')
    else:
        form = FotografiaForms()
        return render(request, 'galeria/nova_imagem.html', {'form': form})


def editar_imagem(request, id):
    if not request.user.is_authenticated:
        return redirect('index')
    foto = Fotografia.objects.get(id=id)
    form = FotografiaForms(instance=foto)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=foto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem editada com sucesso')
            return redirect('index')

    return render(request, 'galeria/editar_imagem.html', {'form': form, 'id': id})


def deletar_imagem(request, id):
    if not request.user.is_authenticated:
        return redirect('index')
    foto = Fotografia.objects.get(id=id)
    foto.delete()
    messages.success(request, 'Imagem deletada com sucesso')
    return redirect('index')
