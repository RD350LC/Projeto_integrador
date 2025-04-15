from django.db import models

class Corretor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    creci = models.CharField(max_length=20, unique=True)  # Unique identifier for real estate agents in Brazil

    class Meta:
        verbose_name = "Corretor"
        verbose_name_plural = "Corretores"
