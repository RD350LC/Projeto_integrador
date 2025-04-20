from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_imoveis, name='listar_imoveis'),
    path('adicionar/', views.adicionar_imovel, name='adicionar_imovel'),
    path('<int:pk>/editar/', views.editar_imovel, name='editar_imovel'),
    path('<int:pk>/excluir/', views.excluir_imovel, name='excluir_imovel'),
    path('<int:pk>/', views.detalhar_imovel, name='detalhar_imovel'),
    path('favoritos/', views.listar_favoritos, name='listar_favoritos'),
    path('<int:pk>/favoritar/', views.adicionar_favorito, name='adicionar_favorito'),
]
