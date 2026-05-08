from django.test import TestCase
from ...models import Cliente, Endereco


class ClienteModelTest(TestCase):

    def setUp(self):
        # endereço fake para os testes
        self.endereco = Endereco.objects.create(
            logradouro="Rua A",
            numero="123",
            bairro="Centro",
            cidade="Natal",
            estado="RN",
            cep="59000000"
        )

    def test_relacionamento_endereco(self):
        cliente = Cliente.objects.create(
            nome="Ana",
            telefone="84966666666",
            cpf="55566677788",
            profissao="Arquiteta",
            renda_familiar=9000,
            endereco=self.endereco
        )

        # testando o relacionamento entre Cliente e Endereco
        self.assertEqual(cliente.endereco.logradouro, "Rua A")