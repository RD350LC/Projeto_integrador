from django.shortcuts import render

def listar_clientes(request):
    clientes = [
        {"nome": "João Silva", "email": "joao@email.com", "telefone": "123456789"},
        {"nome": "Maria Oliveira", "email": "maria@email.com", "telefone": "987654321"},
    ]
    return render(request, 'clientes/listar_clientes.html', {"clientes": clientes})

# Create your views here.
