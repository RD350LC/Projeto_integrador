from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Imovel, Favorito
from .forms import ImovelForm
from django.core.paginator import Paginator

def listar_imoveis(request):
    imoveis_list = Imovel.objects.all()

    # Simplified filters
    filtros = {
        'preco__gte': request.GET.get('preco_min'),
        'preco__lte': request.GET.get('preco_max'),
        'cidade__icontains': request.GET.get('cidade'),
        'tipo__icontains': request.GET.get('tipo'),
    }
    filtros = {key: value for key, value in filtros.items() if value}
    imoveis_list = imoveis_list.filter(**filtros)

    paginator = Paginator(imoveis_list, 10)  # 10 imóveis por página
    page_number = request.GET.get('page')
    imoveis = paginator.get_page(page_number)
    return render(request, 'imoveis/listar_imoveis.html', {"imoveis": imoveis, "filtros": filtros})

@login_required
def adicionar_imovel(request):
    if not hasattr(request.user, 'corretor'):
        raise PermissionDenied("Somente corretores podem adicionar imóveis.")
    if request.method == 'POST':
        form = ImovelForm(request.POST, request.FILES)
        if form.is_valid():
            imovel = form.save()
            # Handle multiple file uploads
            for file in request.FILES.getlist('imagens'):
                imovel.imagens.create(arquivo=file)
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
            imovel = form.save()
            # Handle multiple file uploads
            for file in request.FILES.getlist('imagens'):
                imovel.imagens.create(arquivo=file)
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

@login_required
def listar_favoritos(request):
    favoritos = Favorito.objects.filter(usuario=request.user)
    return render(request, 'imoveis/listar_favoritos.html', {'favoritos': favoritos})

@login_required
def adicionar_favorito(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk)
    Favorito.objects.get_or_create(usuario=request.user, imovel=imovel)
    return redirect('listar_imoveis')
