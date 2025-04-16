from django.db import models

class Imovel(models.Model):
    titulo = models.CharField(max_length=100, default="Título padrão")
    descricao = models.TextField(default="Descrição padrão")
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    foto = models.ImageField(upload_to='imoveis/fotos/', blank=True, null=True, max_length=255)
    endereco = models.OneToOneField('Endereco', on_delete=models.CASCADE, null=True, blank=True, default=1)
    caracteristicas = models.ManyToManyField('Caracteristicas', blank=True)

    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

class Caracteristicas(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Característica"
        verbose_name_plural = "Características"
