from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_relatorios, name='listar_relatorios'),
]
