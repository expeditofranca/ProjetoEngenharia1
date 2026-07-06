from django import forms
from django.utils import timezone
from .models import Divida
from .models import Endereco
from .models import Cliente
from .models import Divida, Pagamento

class DividaForm(forms.ModelForm):
    class Meta:
        model = Divida
        fields = ['cpf_funcionario', 'cliente', 'valor', 'num_notafiscal', 'status', 'data_divida', 'data_vencimento']

        widgets = {
            'data_divida': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_vencimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
        }

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['logradouro', 'numero', 'bairro', 'cidade', 'estado', 'cep']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'profissao', 'renda_familiar', 'status_cliente']
class PagamentoForm(forms.Form):
    dividas = forms.ModelMultipleChoiceField(
        queryset=Divida.objects.none(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input ms-2'}),
        label="Selecione as Dívidas"
    )
    valor_pago = forms.DecimalField(
        max_digits=10, 
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )
    data_pagamento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        initial=timezone.now
    )
