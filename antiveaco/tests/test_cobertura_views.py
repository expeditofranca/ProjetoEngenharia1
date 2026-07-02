from django.test import TestCase
from django.urls import reverse
from antiveaco.models import Cliente, Divida, Endereco, Pagamento
from decimal import Decimal

class ViewsRefatoradasTests(TestCase):
    def setUp(self):
        # 1. Criação do Endereço usando os campos exatos do models.py
        self.endereco = Endereco.objects.create(
            logradouro="Rua Falsa",
            numero="123",
            bairro="Centro",
            cidade="Caicó",
            estado="RN",
            cep="00000000"
        )
        
        # 2. Criação do Cliente preenchendo os dados
        self.cliente = Cliente.objects.create(
            cpf="11122233344", 
            nome="João da Silva", 
            telefone="84999999999",
            profissao="Estudante/Desenvolvedor",
            renda_familiar=1500.0,
            endereco=self.endereco
        )
        
        # 3. Criação da Dívida
        self.divida = Divida.objects.create(
            cliente=self.cliente,
            cpf_funcionario="00000000000",
            num_notafiscal="123456",
            valor=Decimal('100.00'),
            saldo_restante=Decimal('100.00'),
            status='Pendente'
        )

# --- TESTE 1: Exclusão de Dívida no divida_manager ---
    def test_divida_manager_excluir(self):
        """Testa se o envio de POST com 'excluir' deleta a dívida"""
        # Agora estamos usando o nome correto definido no seu urls.py!
        url = reverse('excluir_divida', args=[self.divida.cod_divida]) 
        
        response = self.client.post(url, {'excluir': 'true'})
        
        # Verificamos se a dívida sumiu do banco de dados (0 restantes)
        self.assertEqual(Divida.objects.count(), 0)
    # --- TESTE 2: Pagamento Parcial caindo no ELSE ---
    def test_registrar_pagamento_parcial(self):
        """Testa se um pagamento menor que o saldo atualiza o status para Parcial"""
        url = reverse('registrar_pagamento') 
        
        # Adicionamos os campos que o PagamentoForm provavelmente exige
        response = self.client.post(url, {
            'divida': self.divida.cod_divida,
            'cliente': self.cliente.cpf,           # <-- Adicionado
            'data_pagamento': '2026-05-28',        # <-- Adicionado
            'status': 'Concluído',                 # <-- Adicionado
            'valor_pago': '40.00'
        })
        
        self.divida.refresh_from_db()
        
        # Verifica se o saldo caiu de 100 para 60 e o status mudou para Parcial
        self.assertEqual(self.divida.saldo_restante, Decimal('60.00'))
        self.assertEqual(self.divida.status, 'Parcial')
        self.assertEqual(Pagamento.objects.count(), 1)



# --- TESTE 4: Acessar a página de cadastrar dívida (GET) ---
    def test_divida_manager_get_cadastrar(self):
        """Testa se a página de cadastro de dívida carrega corretamente"""
        url = reverse('cadastrar_divida')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # --- TESTE 5: Acessar a página de atualizar dívida (GET) ---
    def test_divida_manager_get_atualizar(self):
        """Testa se a página de edição de dívida carrega corretamente"""
        url = reverse('atualizar_divida', args=[self.divida.cod_divida])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # --- TESTE 6: Buscar cliente na tela de pagamentos (GET) ---
    def test_registrar_pagamento_busca_cliente(self):
        """Testa se a busca por CPF na tela de pagamentos funciona"""
        url = reverse('registrar_pagamento')
        response = self.client.get(url, {'cpf_cliente': self.cliente.cpf})
        self.assertEqual(response.status_code, 200)
        # Verifica se o cliente buscado apareceu no contexto da página
        self.assertEqual(response.context['cliente'], self.cliente)

    # --- TESTE 7: Erro ao tentar pagar valor maior que a dívida ---
    def test_registrar_pagamento_valor_invalido(self):
        """Testa se o sistema bloqueia pagamentos maiores que o saldo"""
        url = reverse('registrar_pagamento')
        
        # A dívida tem saldo de 100, vamos tentar pagar 500
        response = self.client.post(url, {
            'divida': self.divida.cod_divida,
            'cliente': self.cliente.cpf,
            'data_pagamento': '2026-05-28',
            'status': 'Concluído',
            'valor_pago': '500.00' 
        })
        
        self.divida.refresh_from_db()
        
        # Verifica se o saldo continuou 100 intacto e não criou pagamento
        self.assertEqual(self.divida.saldo_restante, Decimal('100.00'))
        self.assertEqual(Pagamento.objects.count(), 0)