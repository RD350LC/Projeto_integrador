from django.db import models
from django.contrib.auth.models import User

class Imovel(models.Model):
    titulo = models.CharField(max_length=100, default="Título padrão")
    descricao = models.TextField(default="Descrição padrão")
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    foto = models.ImageField(upload_to='imoveis/fotos/', blank=True, null=True, max_length=255)
    endereco = models.OneToOneField('Endereco', on_delete=models.CASCADE, null=True, blank=True, default=1)
    caracteristicas = models.ManyToManyField('Caracteristicas', blank=True)
    tipo = models.CharField(max_length=50, choices=[('Casa', 'Casa'), ('Apartamento', 'Apartamento'), ('Comercial', 'Comercial')], default='Casa')
    cidade = models.CharField(max_length=100, default='Default City')  # Add default value

    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"

class ImagemImovel(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='imoveis/imagens/')

    class Meta:
        verbose_name = "Imagem do Imóvel"
        verbose_name_plural = "Imagens dos Imóveis"

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

class Favorito(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"
