from django.shortcuts import render
from django.http import HttpResponse

def listar_vendas(request):
    vendas = [
        {"cliente": "João", "imovel": "Apartamento 101", "valor": "R$ 500.000"},
        {"cliente": "Maria", "imovel": "Casa 202", "valor": "R$ 750.000"},
    ]
    return render(request, 'vendas/listar_vendas.html', {"vendas": vendas})

# Create your views here.
