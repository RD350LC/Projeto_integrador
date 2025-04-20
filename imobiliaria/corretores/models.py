from django.db import models
from django.core.validators import RegexValidator

class Corretor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="O telefone deve estar no formato '+999999999'.")],
    )
    creci = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Corretor"
        verbose_name_plural = "Corretores"
