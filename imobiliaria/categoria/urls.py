from django.urls import path
from . import views

app_name = 'categoria'

urlpatterns = [
    path('', views.listar_categorias, name='listar_categorias'),
]
