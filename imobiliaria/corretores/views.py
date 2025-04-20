from django.shortcuts import render, get_object_or_404, redirect
from .models import Corretor
from .forms import CorretorForm

def listar_corretores(request):
    corretores = Corretor.objects.all()
    return render(request, 'corretores/listar_corretores.html', {"corretores": corretores})

def detalhar_corretor(request, pk):
    corretor = get_object_or_404(Corretor, pk=pk)
    return render(request, 'corretores/detalhar_corretor.html', {"corretor": corretor})

def adicionar_corretor(request):
    if request.method == 'POST':
        form = CorretorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('corretores:listar_corretores')
    else:
        form = CorretorForm()
    return render(request, 'corretores/adicionar_corretor.html', {'form': form})

def editar_corretor(request, pk):
    corretor = get_object_or_404(Corretor, pk=pk)
    if request.method == 'POST':
        form = CorretorForm(request.POST, instance=corretor)
        if form.is_valid():
            form.save()
            return redirect('corretores:listar_corretores')
    else:
        form = CorretorForm(instance=corretor)
    return render(request, 'corretores/editar_corretor.html', {'form': form, 'corretor': corretor})

def excluir_corretor(request, pk):
    corretor = get_object_or_404(Corretor, pk=pk)
    if request.method == 'POST':
        corretor.delete()
        return redirect('corretores:listar_corretores')
    return render(request, 'corretores/excluir_corretor.html', {'corretor': corretor})
