from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Imovel
from .forms import ImovelForm  # Assuming a form for Imovel exists

def listar_imoveis(request):
    imoveis = [
        {"titulo": "Apartamento 101", "preco": "R$ 500.000"},
        {"titulo": "Casa 202", "preco": "R$ 750.000"},
    ]
    return render(request, 'imoveis/listar_imoveis.html', {"imoveis": imoveis})

@login_required
def adicionar_imovel(request):
    if not hasattr(request.user, 'corretor'):
        raise PermissionDenied("Somente corretores podem adicionar imóveis.")
    
    if request.method == 'POST':
        form = ImovelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_imoveis')
    else:
        form = ImovelForm()
    
    return render(request, 'imoveis/adicionar_imovel.html', {'form': form})

@login_required
def editar_imovel(request, pk):
    if not hasattr(request.user, 'corretor'):
        raise PermissionDenied("Somente corretores podem editar imóveis.")
    
    imovel = Imovel.objects.get(pk=pk)
    if request.method == 'POST':
        form = ImovelForm(request.POST, request.FILES, instance=imovel)
        if form.is_valid():
            form.save()
            return redirect('listar_imoveis')
    else:
        form = ImovelForm(instance=imovel)
    
    return render(request, 'imoveis/editar_imovel.html', {'form': form, 'imovel': imovel})

@login_required
def excluir_imovel(request, pk):
    if not hasattr(request.user, 'corretor'):
        raise PermissionDenied("Somente corretores podem excluir imóveis.")
    
    imovel = Imovel.objects.get(pk=pk)
    if request.method == 'POST':
        imovel.delete()
        return redirect('listar_imoveis')
    
    return render(request, 'imoveis/excluir_imovel.html', {'imovel': imovel})

# Create your views here.
