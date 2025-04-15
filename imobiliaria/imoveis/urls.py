from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_imoveis, name='listar_imoveis'),
    path('adicionar/', views.adicionar_imovel, name='adicionar_imovel'),
]
