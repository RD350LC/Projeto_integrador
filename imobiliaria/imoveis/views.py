from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Imovel
from .forms import ImovelForm  # Assuming a form for Imovel exists

def listar_imoveis(request):
    imoveis = Imovel.objects.all()
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
    
    imovel = get_object_or_404(Imovel, pk=pk)
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
    
    imovel = get_object_or_404(Imovel, pk=pk)
    if request.method == 'POST':
        imovel.delete()
        return redirect('listar_imoveis')
    
    return render(request, 'imoveis/excluir_imovel.html', {'imovel': imovel})

def detalhar_imovel(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk)
    return render(request, 'imoveis/detalhar_imovel.html', {'imovel': imovel})
