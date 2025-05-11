from django.urls import path
from . import views

urlpatterns = [
    path('manutencao/', views.manutencao_predial, name='manutencao_predial'),
]