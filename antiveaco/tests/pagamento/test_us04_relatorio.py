from django.test import TestCase
from django.urls import reverse
from antiveaco.models import Cliente, Divida, Endereco, Pagamento

class RelatorioPagamentoTestCase(TestCase):

    def setUp(self):
        # 1. Preparando o Endereço
        self.endereco = Endereco.objects.create(
            logradouro="Rua A", 
            numero="10", 
            bairro="Centro",
            cidade="Caicó", 
            estado="RN", 
            cep="59300-000"
        )

        # 2. Preparando o Cliente
        self.cliente = Cliente.objects.create(
            nome="Maria da Guia", 
            telefone="84999999999", 
            cpf="10987654321",
            profissao="Comerciante", 
            renda_familiar=3000, 
            endereco=self.endereco
        )

        # 3. Preparando a Dívida base
        self.divida = Divida.objects.create(
            cpf_funcionario="11111111111", 
            cliente=self.cliente, 
            valor=500,
            saldo_restante=300,
            status="Pendente", 
            num_notafiscal="NF123"
        )

        # 4. Criando o registro de um Pagamento
        self.pagamento = Pagamento.objects.create(
            divida=self.divida,
            cliente=self.cliente,
            valor_pago=200,
            status="Concluído"
        )

    # ---------------------------------------------------------
    # TESTES DA US04 - RELATÓRIO DE PAGAMENTO
    # ---------------------------------------------------------

    def test_gerar_relatorio_com_sucesso(self):
        """TA04.01 - Deve carregar a página e exibir os dados do pagamento"""
        response = self.client.get(reverse('lista_pagamentos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Maria da Guia")
        self.assertContains(response, "200.00")

    def test_gerar_relatorio_sem_dados(self):
        """TA04.02 - Deve exibir mensagem caso não haja pagamentos"""
        Pagamento.objects.all().delete()
        response = self.client.get(reverse('lista_pagamentos'))
        self.assertEqual(response.status_code, 200)