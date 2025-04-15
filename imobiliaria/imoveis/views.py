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

# Create your views here.
