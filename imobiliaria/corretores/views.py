from django.shortcuts import render

def listar_corretores(request):
    corretores = [
        {"nome": "Carlos Souza", "creci": "12345", "telefone": "123456789"},
        {"nome": "Ana Lima", "creci": "67890", "telefone": "987654321"},
    ]
    return render(request, 'corretores/listar_corretores.html', {"corretores": corretores})
