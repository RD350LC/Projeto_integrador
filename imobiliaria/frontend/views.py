from django.shortcuts import render

def pagina_inicial(request):
    return render(request, 'frontend/pagina_inicial.html')  # Certifique-se de que o caminho do template está correto

def sobre(request):
    return render(request, 'frontend/sobre.html')  # Certifique-se de que o caminho do template está correto

def contato(request):
    return render(request, 'frontend/contato.html')

# Create your views here.
