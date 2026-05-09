from django.test import TestCase
from antiveaco.models import Cliente, Endereco, Divida, Pagamento

class PagamentoModelTest(TestCase):

    # Configuração inicial para os testes
    def setUp(self):

        self.endereco = Endereco.objects.create(
            logradouro="Rua A",
            numero="123",
            bairro="Bairro A",
            cidade="Cidade A",
            estado="Estado A",
            cep="12345-678"
        )

        self.cliente = Cliente.objects.create(
            nome="Ana",
            telefone="840000000",
            cpf="00000000000",
            profissao="Professora",
            renda_familiar=5000.00,
            endereco=self.endereco
        )

        self.divida = Divida.objects.create(
            cliente=self.cliente,
            valor=200.00,
            data_divida="2023-01-01",
            status="Pendente",
            num_notafiscal="NF123"
        )