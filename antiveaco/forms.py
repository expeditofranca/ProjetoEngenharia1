from django import forms
from .models import Divida
from .models import Endereco
from .models import Cliente

class DividaForm(forms.ModelForm):
    class Meta:
        model = Divida
        fields = ['cpf_funcionario', 'cliente', 'valor', 'num_notafiscal', 'status']

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['logradouro', 'numero', 'bairro', 'cidade', 'estado', 'cep']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'profissao', 'renda_familiar', 'status_cliente']