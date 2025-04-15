from django.db import models
from vendas.models import Venda

class Relatorio(models.Model):
    titulo = models.CharField(max_length=100)
    data_criacao = models.DateField(auto_now_add=True)
    vendas = models.ManyToManyField(Venda, blank=True)
