from django.shortcuts import render

def pagina_inicial(request):
    return render(request, 'frontend/pagina_inicial.html')