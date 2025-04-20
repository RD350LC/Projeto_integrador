from django.urls import path
from . import views

app_name = 'corretores'

urlpatterns = [
    path('', views.listar_corretores, name='listar_corretores'),
    path('<int:pk>/', views.detalhar_corretor, name='detalhar_corretor'),
    path('adicionar/', views.adicionar_corretor, name='adicionar_corretor'),
    path('<int:pk>/editar/', views.editar_corretor, name='editar_corretor'),
    path('<int:pk>/excluir/', views.excluir_corretor, name='excluir_corretor'),
]
