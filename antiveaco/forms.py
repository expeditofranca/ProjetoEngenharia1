from django import forms
from .models import Divida
from .models import Endereco
from .models import Cliente
from .models import Divida, Pagamento

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
class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['divida', 'valor_pago']
