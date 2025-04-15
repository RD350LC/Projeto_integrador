from django.shortcuts import render

def listar_relatorios(request):
    relatorios = [
        {"titulo": "Relatório de Janeiro", "data": "01/02/2023"},
        {"titulo": "Relatório de Fevereiro", "data": "01/03/2023"},
    ]
    return render(request, 'relatorios/listar_relatorios.html', {"relatorios": relatorios})
