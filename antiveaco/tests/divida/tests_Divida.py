from django.test import TestCase
from django.urls import reverse

from antiveaco.models import Cliente, Divida, Endereco


class DividaTestCase(TestCase):

    def setUp(self):

        self.endereco = Endereco.objects.create(
            logradouro="Rua A",
            numero="10",
            bairro="Centro",
            cidade="Campina Grande",
            estado="PB",
            cep="58400-000"
        )

        self.cliente = Cliente.objects.create(
            nome="Arthur",
            telefone="83999999999",
            cpf="12345678901",
            profissao="Estudante",
            renda_familiar=2000,
            endereco=self.endereco
        )

        self.divida = Divida.objects.create(
            cpf_funcionario="11111111111",
            cliente=self.cliente,
            valor=500,
            status="Pendente",
            num_notafiscal="NF123"
        )

    # -------------------------
    # TESTES NO MODEL
    # -------------------------

    def test_criar_divida(self):
        self.assertEqual(self.divida.valor, 500)
        self.assertEqual(self.divida.status, "Pendente")

    def test_divida_associada_cliente(self):
        self.assertEqual(self.divida.cliente.nome, "Arthur")

    # -------------------------
    # TESTES NOVIEW - LISTAR
    # -------------------------

    def test_listar_dividas(self):
        response = self.client.get(reverse('pesquisar_divida'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Arthur")

    # -------------------------
    # TESTES NO VIEW - CADASTRAR
    # -------------------------

    def test_cadastrar_divida_invalido(self):
        """Testa se o sistema bloqueia cadastro com dados incompletos"""
        response = self.client.post(
            reverse('cadastrar_divida'),
            {
                'cpf_funcionario': '',
                'valor': 300
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Divida.objects.count(), 1)

    # -------------------------
    # TESTES NO VIEW - ATUALIZAR
    # -------------------------

    def test_atualizar_divida(self):

        response = self.client.post(
            reverse('atualizar_divida', args=[self.divida.cod_divida]),
            {
                'cpf_funcionario': '11111111111',
                'cliente': self.cliente.cpf,
                'valor': 800,
                'status': 'Parcial',
                'num_notafiscal': 'NF123'
            }
        )

        self.divida.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.divida.valor, 800)
        self.assertEqual(self.divida.status, "Parcial")

    # -------------------------
    # TESTES NO VIEW - EXCLUIR
    # -------------------------

    def test_excluir_divida(self):

        response = self.client.post(
            reverse('excluir_divida', args=[self.divida.cod_divida]),
            {
                'excluir': True
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Divida.objects.count(), 0)
    
    def test_pesquisar_divida_filtro(self):
        """Testa se o filtro por status funciona na pesquisa"""
        # Busca apenas dívidas com status 'Pendente'
        response = self.client.get(reverse('pesquisar_divida'), {'status': 'Pendente'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Arthur")