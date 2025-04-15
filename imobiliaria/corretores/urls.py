from django.urls import path
from . import views

app_name = 'corretores'

urlpatterns = [
    path('', views.listar_corretores, name='listar_corretores'),
]
