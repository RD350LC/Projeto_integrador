from django import forms
from .models import Corretor

class CorretorForm(forms.ModelForm):
    class Meta:
        model = Corretor
        fields = ['nome', 'email', 'telefone', 'creci']
