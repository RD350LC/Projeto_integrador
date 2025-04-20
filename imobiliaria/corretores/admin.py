from django.contrib import admin
from .models import Corretor

@admin.register(Corretor)
class CorretorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'creci')
    search_fields = ('nome', 'email', 'creci')
    list_filter = ('creci',)
