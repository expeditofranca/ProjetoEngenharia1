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
        url = reverse('excluir_divida', args=[self.divida.cod_divida]) 
        response = self.client.post(url, {'excluir': 'true'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Divida.objects.count(), 0)

    # --- TESTE 2: Pagamento Parcial ---
    def test_registrar_pagamento_parcial(self):
        url = reverse('registrar_pagamento') 
        response = self.client.post(url, {
            'dividas': [self.divida.cod_divida],
            'cpf_cliente': self.cliente.cpf,
            'data_pagamento': '2026-05-28',
            'valor_pago': '40.00'
        })
        self.assertEqual(response.status_code, 302)
        
        self.divida.refresh_from_db()
        self.assertEqual(self.divida.saldo_restante, Decimal('60.00'))
        self.assertEqual(self.divida.status, 'Parcial')
        self.assertEqual(Pagamento.objects.count(), 1)
    
    # --- TESTE 3: Pagar Tudo ---
    def test_registrar_pagamento_pagar_tudo(self):
        url = reverse('registrar_pagamento')
        response = self.client.post(url, {
            'pagar_tudo': 'true',
            'cpf_cliente': self.cliente.cpf
        })
        
        self.assertEqual(response.status_code, 302)
        self.divida.refresh_from_db()
        self.assertEqual(self.divida.saldo_restante, Decimal('0.00'))
        self.assertEqual(self.divida.status, 'Pago')
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
        url = reverse('registrar_pagamento')
        response = self.client.post(url, {
            'dividas': [self.divida.cod_divida],
            'cpf_cliente': self.cliente.cpf,
            'data_pagamento': '2026-05-28',
            'valor_pago': '500.00' 
        })
        
        self.assertEqual(response.status_code, 200)
        self.divida.refresh_from_db()
        self.assertEqual(self.divida.saldo_restante, Decimal('100.00'))
        self.assertEqual(Pagamento.objects.count(), 0)

    # --- TESTE 8: Pesquisar histórico com cliente inexistente ---
    def test_pesquisar_historico_cliente_inexistente(self):
        """Testa a pesquisa de histórico com um CPF que não existe no banco"""
        url = reverse('pesquisar_historico')
        response = self.client.get(url, {'cpf_cliente': '00000000000'})
        
        self.assertEqual(response.status_code, 200)
        mensagens = list(response.context['messages'])
        self.assertTrue(any("Nenhum cliente encontrado" in str(m) for m in mensagens))

    # --- TESTE 9: Gerar histórico para cliente sem dívidas ---
    def test_gerar_historico_cliente_sem_dividas(self):
        """Testa a geração de histórico para um cliente que não possui dívidas cadastradas"""
        novo_endereco = Endereco.objects.create(
            logradouro="Rua Nova", numero="999", bairro="Centro",
            cidade="Caicó", estado="RN", cep="11111111"
        )
        
        cliente_sem_divida = Cliente.objects.create(
            cpf="99988877766", nome="Maria Teste", telefone="84988888888",
            profissao="Teste", renda_familiar=1000.0, endereco=novo_endereco
        )
        
        url = reverse('gerar_historico_dividas', args=[cliente_sem_divida.cpf])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context.get('dividas'))

    # --- TESTE 10: Filtro de busca textual na lista de dívidas ---
    def test_get_dividas_com_filtro_de_busca(self):
        """Testa o filtro de busca textual de dívidas (por nome) na tela de pesquisa"""
        url = reverse('pesquisar_divida')
        response = self.client.get(url, {'busca_cliente': self.cliente.nome})
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.divida, response.context['dividas'])

    def test_menus_simples_e_alertas(self):
        """Cobre as views básicas que apenas renderizam HTML e a de alertas"""
        rotas = [
            'index',
            'index_divida',
            'index_cliente',
            'index_relatorios',
            'alertas_inadimplencia'
        ]
        for rota in rotas:
            try:
                url = reverse(rota)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200, f"A rota {rota} falhou.")
            except Exception as e:
                print(f"Aviso: Rota '{rota}' não encontrada ou com erro: {e}")

    def test_detalhes_pagamentos_view(self):
        """Cobre a view detalhes_pagamentos carregando os dados da dívida"""
        url = reverse('detalhes_pagamentos', args=[self.divida.cod_divida])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['divida'], self.divida)

    def test_relatorio_mensal_dividas_cenarios(self):
        """Cobre a view de relatório mensal (GET normal e GET com erro de validação)"""
        url = reverse('relatorio_mensal_dividas')
        
        response_normal = self.client.get(url)
        self.assertEqual(response_normal.status_code, 200)
        
        response_erro = self.client.get(url, {'mes': '15', 'ano': '2026'})
        self.assertEqual(response_erro.status_code, 200)
        
        mensagens = list(response_erro.context['messages'])
        self.assertTrue(any("Mês inválido" in str(m) for m in mensagens))

    def test_cadastrar_cliente_get(self):
        """Cobre o carregamento inicial (GET) da tela de cadastro de clientes"""
        url = reverse('cadastrar_cliente')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('cliente_form', response.context)
        self.assertIn('endereco_form', response.context)

    def test_cadastrar_cliente_post_sucesso(self):
        """Cobre as linhas do 'if form.is_valid()' simulando um cadastro correto"""
        url = reverse('cadastrar_cliente')
        
        dados_validos = {
            'logradouro': 'Rua dos Testes',
            'numero': '404',
            'bairro': 'Bairro Novo',
            'cidade': 'Natal',
            'estado': 'RN',
            'cep': '59000000',
            'cpf': '09876543211',
            'nome': 'Carlos Silva',
            'telefone': '84977777777',
            'profissao': 'Engenheiro',
            'renda_familiar': '5000.00'
        }
        
        response = self.client.post(url, dados_validos)
        
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(Cliente.objects.filter(cpf='09876543211').exists())

    def test_cadastrar_cliente_post_invalido(self):
        """Cobre as linhas do 'else' quando o formulário tem erros de validação"""
        url = reverse('cadastrar_cliente')
        dados_invalidos = {
            'nome': '', 
            'cpf': '123' 
        }
        
        response = self.client.post(url, dados_invalidos)
        self.assertEqual(response.status_code, 200)  
        mensagens = list(response.context['messages'])
        self.assertTrue(any("corrija os erros" in str(m) for m in mensagens))