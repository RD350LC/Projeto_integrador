from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),  # Certifique-se de que a URL está correta
    path('sobre/', views.sobre, name='sobre'),  # Nova rota para a página "Sobre"
]
