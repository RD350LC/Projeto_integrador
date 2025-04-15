from django.shortcuts import render

def pagina_inicial(request):
    # Renderiza o template correto
    return render(request, 'frontend/pagina_inicial.html')

# Create your views here.
