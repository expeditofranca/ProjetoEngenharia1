from django.test import TestCase
from django.db.utils import IntegrityError

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

    def test_cpf_unico(self):
        Cliente.objects.create(
            nome="Cliente 1",
            telefone="11111111111",
            cpf="12312312312",
            profissao="Médico",
            renda_familiar=7000,
            endereco=self.endereco
        )

        outro_endereco = Endereco.objects.create(
            logradouro="Rua B",
            numero="456",
            bairro="Lagoa Nova",
            cidade="Natal",
            estado="RN",
            cep="59000001"
        )

        # tentando criar outro cliente com o mesmo CPF deve gerar um erro de integridade
        with self.assertRaises(IntegrityError):
            Cliente.objects.create(
                nome="Cliente 2",
                telefone="22222222222",
                cpf="12312312312",  # CPF repetido
                profissao="Advogado",
                renda_familiar=8000,
                endereco=outro_endereco
            )
