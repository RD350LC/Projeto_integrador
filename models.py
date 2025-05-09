from django.db import models

class Imovel(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, default="Descrição padrão")
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome