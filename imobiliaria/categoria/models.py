from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
