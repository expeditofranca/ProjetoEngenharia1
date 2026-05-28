from django.test import TestCase
from django.db import IntegrityError

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

    # Verifica se um pagamento válido é criado corretamente
    def test_criar_pagamento_valido(self):
        pagamento = Pagamento.objects.create(
            divida=self.divida,
            cliente=self.cliente,
            valor_pago=100.00
        )

        self.assertIsNotNone(pagamento.cod_pagamento)
        self.assertEqual(pagamento.valor_pago, 100.00)

    # Testar a criação de um pagamento sem uma dívida associada (deve falhar)
    def test_pagamento_sem_divida(self):
        with self.assertRaises(IntegrityError):
            Pagamento.objects.create(
                cliente=self.cliente,
                valor_pago=100.00
            )
    
    # Testar o relacionamento entre pagamento e dívida
    def test_pagamento_associado_a_divida(self):
        pagamento = Pagamento.objects.create(
            divida=self.divida,
            cliente=self.cliente,
            valor_pago=50
        )

        self.assertEqual(pagamento.divida, self.divida)
        
    # Testar o status padrão do pagamento
    def test_status_padrao_pagamento(self):
        pagamento = Pagamento.objects.create(
            divida=self.divida,
            cliente=self.cliente,
            valor_pago=50
        )

        self.assertEqual(pagamento.status, "Concluído")

    # Testar a data de pagamento padrão
    def test_data_pagamento_padrao(self):
        pagamento = Pagamento.objects.create(
            divida=self.divida,
            cliente=self.cliente,
            valor_pago=50
        )

        self.assertIsNotNone(pagamento.data_pagamento)

    # Testar a criação de um pagamento sem um cliente associado (deve falhar)
    def test_pagamento_sem_cliente(self):
        with self.assertRaises(IntegrityError):
            Pagamento.objects.create(
                divida=self.divida,
                valor_pago=100
            )