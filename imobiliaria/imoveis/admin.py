from django.contrib import admin
from .models import Imovel, Endereco, Caracteristicas

admin.site.register(Imovel)
admin.site.register(Endereco)
admin.site.register(Caracteristicas)
