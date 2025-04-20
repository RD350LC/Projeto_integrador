from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_vendas, name='listar_vendas'),
    path('adicionar/', views.adicionar_venda, name='adicionar_venda'),
    path('<int:pk>/editar/', views.editar_venda, name='editar_venda'),
    path('<int:pk>/excluir/', views.excluir_venda, name='excluir_venda'),
]
