from django import forms
from .models import Imovel

class ImovelForm(forms.ModelForm):
    imagens = forms.FileField(
        widget=forms.ClearableFileInput(),
        required=False
    )

    class Meta:
        model = Imovel
        fields = ['titulo', 'descricao', 'preco', 'cidade', 'tipo', 'foto']
