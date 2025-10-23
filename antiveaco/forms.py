from django import forms
from .models import Divida, Pagamento

class DividaForm(forms.ModelForm):
    class Meta:
        model = Divida
        fields = ['cpf_funcionario', 'cliente', 'valor', 'num_notafiscal', 'status']

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['divida', 'valor_pago']