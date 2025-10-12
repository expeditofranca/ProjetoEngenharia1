from django import forms
from .models import Divida

class DividaForm(forms.ModelForm):
    class Meta:
        model = Divida
        fields = ['cpf_funcionario', 'cliente', 'valor', 'num_notafiscal', 'status']