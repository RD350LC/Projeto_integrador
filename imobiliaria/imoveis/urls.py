from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_imoveis, name='listar_imoveis'),
    path('adicionar/', views.adicionar_imovel, name='adicionar_imovel'),
    path('editar/<int:pk>/', views.editar_imovel, name='editar_imovel'),
    path('excluir/<int:pk>/', views.excluir_imovel, name='excluir_imovel'),
]
