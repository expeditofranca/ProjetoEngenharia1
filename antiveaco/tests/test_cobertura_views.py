from django.test import TestCase
from django.urls import reverse
from antiveaco.models import Cliente, Divida, Endereco, Pagamento
from decimal import Decimal

class ViewsRefatoradasTests(TestCase):
    def setUp(self):
        # 1. Criamos dados de mentira no banco de dados de teste
        # Ajuste os campos do Endereco conforme os campos obrigatórios do seu models.py
        self.endereco = Endereco.objects.create(
            cep="00000000", rua="Rua Falsa", numero="123", bairro="Centro", cidade="Caicó", uf="RN"
        )
        
        self.cliente = Cliente.objects.create(
            cpf="11122233344", nome="João da Silva", endereco=self.endereco
        )
        
        self.divida = Divida.objects.create(
            cliente=self.cliente,
            valor=Decimal('100.00'),
            saldo_restante=Decimal('100.00'),
            status='Pendente',
            # Coloque uma data válida se for obrigatório no seu model
            # data_vencimento="2026-12-31" 
        )

    # --- TESTE 1: Exclusão de Dívida no divida_manager ---
    def test_divida_manager_excluir(self):
        """Testa se o envio de POST com 'excluir' deleta a dívida"""
        # Supondo que a url no seu urls.py se chame 'divida_manager' (ou algo similar, ajuste se necessário)
        # Passamos o pk da dívida na URL, como a view exige
        url = f"/divida_manager/{self.divida.pk}/" # Ajuste para a sua URL real ou use reverse()
        
        # Simulamos o clique no botão excluir
        response = self.client.post(url, {'excluir': 'true'})
        
        # Verificamos se a dívida sumiu do banco de dados (0 restantes)
        self.assertEqual(Divida.objects.count(), 0)
        # Verifica se redirecionou para pesquisar_divida
        self.assertRedirects(response, reverse('pesquisar_divida'), fetch_redirect_response=False)

    # --- TESTE 2: Pagamento Parcial caindo no ELSE ---
    def test_registrar_pagamento_parcial(self):
        """Testa se um pagamento menor que o saldo atualiza o status para Parcial"""
        url = reverse('registrar_pagamento') # Ajuste se o nome na sua urls.py for diferente
        
        # Simulamos o form de pagamento enviando 40 reais
        response = self.client.post(url, {
            'divida': self.divida.pk,
            'valor_pago': '40.00'
        })
        
        # Puxa a dívida atualizada do banco
        self.divida.refresh_from_db()
        
        # Verifica se o saldo caiu de 100 para 60 e o status mudou para Parcial
        self.assertEqual(self.divida.saldo_restante, Decimal('60.00'))
        self.assertEqual(self.divida.status, 'Parcial')
        self.assertEqual(Pagamento.objects.count(), 1)

    # --- TESTE 3: Pagar Tudo ---
    def test_registrar_pagamento_pagar_tudo(self):
        """Testa se o botão Pagar Tudo quita todas as dívidas pendentes do cliente"""
        url = reverse('registrar_pagamento')
        
        # Simulamos o clique no botão de pagar tudo
        response = self.client.post(url, {
            'pagar_tudo': 'true',
            'cpf_cliente': self.cliente.cpf
        })
        
        self.divida.refresh_from_db()
        
        # Verifica se a dívida zerou e o status foi para Pago
        self.assertEqual(self.divida.saldo_restante, Decimal('0.00'))
        self.assertEqual(self.divida.status, 'Pago')
        self.assertEqual(Pagamento.objects.count(), 1)