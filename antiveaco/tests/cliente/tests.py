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

    # testando a criação de um cliente com dados válidos
    def test_criacao_cliente(self):
        cliente = Cliente.objects.create(
            nome="João Silva",
            telefone="84999999999",
            cpf="12345678901",
            profissao="Professor",
            renda_familiar=3500.50,
            endereco=self.endereco
        )

        # verificando se os campos foram salvos corretamente
        self.assertEqual(cliente.nome, "João Silva")
        self.assertEqual(cliente.telefone, "84999999999")
        self.assertEqual(cliente.cpf, "12345678901")
        self.assertEqual(cliente.profissao, "Professor")
        self.assertEqual(cliente.renda_familiar, 3500.50)
        self.assertTrue(cliente.status_cliente)