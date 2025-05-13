from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),  # Certifique-se de que a URL está correta
    path('sobre/', views.contato, name='sobre'),  # Redirect 'sobre' to 'contato'
    path('contato/', views.contato, name='contato'),
    path('manutencao_predial/', views.manutencao_predial, name='manutencao_predial'),
]
