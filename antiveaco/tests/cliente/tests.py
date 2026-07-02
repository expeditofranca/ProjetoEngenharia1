from django.test import TestCase
from django.urls import reverse
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

    # testando o valor padrão do campo status_cliente
    def test_status_cliente_padrao(self):
        cliente = Cliente.objects.create(
            nome="Carlos",
            telefone="84977777777",
            cpf="11122233344",
            profissao="Designer",
            renda_familiar=2500,
            endereco=self.endereco
        )

        self.assertTrue(cliente.status_cliente)

    def test_metodo_str(self):
        cliente = Cliente.objects.create(
            nome="Maria",
            telefone="84988888888",
            cpf="98765432100",
            profissao="Engenheira",
            renda_familiar=5000,
            endereco=self.endereco
        )

        # verificando a representação em string do cliente
        self.assertEqual(str(cliente), "Maria (98765432100)")

class ClienteViewsTest(TestCase):
    def setUp(self):
        # 1. Cria um endereço e um cliente para usarmos nas requisições HTTP
        self.endereco = Endereco.objects.create(
            logradouro="Rua A",
            numero="123",
            bairro="Centro",
            cidade="Natal",
            estado="RN",
            cep="59000000"
        )
        self.cliente = Cliente.objects.create(
            nome="João Silva",
            telefone="84999999999",
            cpf="12345678901",
            profissao="Professor",
            renda_familiar=3500.50,
            endereco=self.endereco
        )

    # --- Teste da linha 325 (index_cliente) ---
    def test_index_cliente_carrega_corretamente(self):
        url = reverse('index_cliente')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # --- Teste das linhas 255-266 (pesquisar_cliente) ---
    def test_pesquisar_cliente_filtro_cpf(self):
        url = reverse('pesquisar_cliente')
        response = self.client.get(url, {'cpf_cliente': self.cliente.cpf})
        self.assertEqual(response.status_code, 200)
        # Verifica se o cliente buscado está na lista retornada para o template
        self.assertIn(self.cliente, response.context['clientes'])

    # --- Teste das linhas 312-321 (excluir_cliente via POST) ---
    def test_excluir_cliente_sucesso(self):
        # Atenção: verifique se a sua URL de excluir cliente recebe o CPF como argumento
        url = reverse('excluir_cliente', args=[self.cliente.cpf])
        response = self.client.post(url)
        
        # Verifica se fomos redirecionados de volta para a tela de pesquisa
        self.assertRedirects(response, reverse('pesquisar_cliente'))
        # Garante que o cliente foi apagado do banco de dados
        self.assertEqual(Cliente.objects.count(), 0)

    # --- Teste da linha 296 (editar_cliente com erro de formulário) ---
    def test_editar_cliente_formulario_invalido(self):
        url = reverse('editar_cliente', args=[self.cliente.cpf])
        # Mandamos um POST faltando dados obrigatórios ou com dados inválidos (ex: nome vazio)
        response = self.client.post(url, {
            'nome': '',  # Forçando o formulário a ser inválido
            'cpf': self.cliente.cpf
        })
        
        # A página deve recarregar (status 200) mostrando o erro, em vez de redirecionar
        self.assertEqual(response.status_code, 200)
        
        # Verifica se a mensagem de erro exata (aquela da linha 296) foi gerada
        from django.contrib.messages import get_messages
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any('Por favor, corrija os erros no formulário.' in str(m) for m in messages))