from django.shortcuts import render, get_object_or_404, redirect
from .models import Relatorio
from .forms import RelatorioForm

def listar_relatorios(request):
    relatorios = Relatorio.objects.all()
    return render(request, 'relatorios/listar_relatorios.html', {"relatorios": relatorios})

def adicionar_relatorio(request):
    if request.method == 'POST':
        form = RelatorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_relatorios')
    else:
        form = RelatorioForm()
    return render(request, 'relatorios/adicionar_relatorio.html', {'form': form})

def editar_relatorio(request, pk):
    relatorio = get_object_or_404(Relatorio, pk=pk)
    if request.method == 'POST':
        form = RelatorioForm(request.POST, instance=relatorio)
        if form.is_valid():
            form.save()
            return redirect('listar_relatorios')
    else:
        form = RelatorioForm(instance=relatorio)
    return render(request, 'relatorios/editar_relatorio.html', {'form': form, 'relatorio': relatorio})

def excluir_relatorio(request, pk):
    relatorio = get_object_or_404(Relatorio, pk=pk)
    if request.method == 'POST':
        relatorio.delete()
        return redirect('listar_relatorios')
    return render(request, 'relatorios/excluir_relatorio.html', {'relatorio': relatorio})
