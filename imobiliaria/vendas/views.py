from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Venda
from .forms import VendaForm

def listar_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'vendas/listar_vendas.html', {"vendas": vendas})

def adicionar_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vendas')
    else:
        form = VendaForm()
    return render(request, 'vendas/adicionar_venda.html', {'form': form})

def editar_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    if request.method == 'POST':
        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():
            form.save()
            return redirect('listar_vendas')
    else:
        form = VendaForm(instance=venda)
    return render(request, 'vendas/editar_venda.html', {'form': form, 'venda': venda})

def excluir_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    if request.method == 'POST':
        venda.delete()
        return redirect('listar_vendas')
    return render(request, 'vendas/excluir_venda.html', {'venda': venda})
