from django.shortcuts import render

def listar_categorias(request):
    categorias = [
        {"nome": "Residencial", "descricao": "Imóveis para moradia"},
        {"nome": "Comercial", "descricao": "Imóveis para negócios"},
    ]
    return render(request, 'categoria/listar_categorias.html', {"categorias": categorias})

# Create your views here.
