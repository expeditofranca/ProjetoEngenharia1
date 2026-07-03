from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.utils import timezone

from django.db import transaction
from django.db.models import Sum
from decimal import Decimal

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Cliente, Divida, Pagamento, Endereco
from .serializers import ClienteSerializer, DividaSerializer
from django.db.models import Q

from .forms import PagamentoForm
from .forms import DividaForm
from .forms import ClienteForm
from .forms import EnderecoForm

import json

def get_dividas(request):
    dividas = Divida.objects.all()

    busca_cliente = request.GET.get('busca_cliente')
    status = request.GET.get('status')
    valor_min = request.GET.get('valor_min')
    valor_max = request.GET.get('valor_max')

    if busca_cliente:
        dividas = dividas.filter(
            Q(cliente__nome__icontains=busca_cliente) | 
            Q(cliente__cpf__icontains=busca_cliente)
        )
        
    if status:
        dividas = dividas.filter(status=status)
    if valor_min:
        dividas = dividas.filter(valor__gte=valor_min)
    if valor_max:
        dividas = dividas.filter(valor__lte=valor_max)

    return render(request, 'divida/pesquisar_divida.html', {'dividas': dividas})

def divida_manager(request, cod_divida=None):
    # 1. Definir a instância e o template de forma direta em uma linha
    divida = get_object_or_404(Divida, pk=cod_divida) if cod_divida else None
    template = 'divida/atualizar_divida.html' if divida else 'divida/cadastrar_divida.html'

    # 2. Early Return para exclusão (evita aninhamento profundo)
    if request.method == 'POST' and 'excluir' in request.POST and divida:
        divida.delete()
        messages.success(request, 'Dívida excluída com sucesso!')
        return redirect('pesquisar_divida')

    # 3. Lidar com requisições GET (Apenas carregar a página)
    if request.method == 'GET':
        form = DividaForm(instance=divida)
        return render(request, template, {'form': form, 'divida': divida})

    # 4. Lidar com a criação/atualização no POST
    form = DividaForm(request.POST, instance=divida)
    
    if form.is_valid():
        divida_obj = form.save(commit=False)
        
        # Apenas para novas dívidas, iguala o saldo ao valor total
        if not divida: 
            divida_obj.saldo_restante = divida_obj.valor
            
        divida_obj.save()

        # Mensagem condicional em uma única linha
        mensagem = 'Dívida atualizada com sucesso!' if divida else 'Dívida cadastrada com sucesso!'
        messages.success(request, mensagem)
        return redirect('pesquisar_divida')

    # 5. Fallback: Se chegou aqui, o form é inválido no POST
    return render(request, template, {
        'form': form,
        'erro': 'Erro ao salvar os dados.',
        'divida': divida
    })

def cadastrar_cliente(request):
    if request.method == 'POST':
        # Se for um POST, preenchemos os forms com os dados enviados
        cliente_form = ClienteForm(request.POST)
        endereco_form = EnderecoForm(request.POST)

        # Verificamos se AMBOS os formulários são válidos
        if cliente_form.is_valid() and endereco_form.is_valid():
            try:
                # transaction.atomic garante que ou tudo salva, ou nada salva
                with transaction.atomic():
                    # 1. Salva o endereço primeiro para obter um objeto
                    endereco_obj = endereco_form.save()
                    
                    # 2. Prepara o cliente, mas não salva no banco ainda (commit=False)
                    cliente_obj = cliente_form.save(commit=False)
                    
                    # 3. Associa o endereço salvo ao cliente
                    cliente_obj.endereco = endereco_obj
                    
                    # 4. Agora sim, salva o cliente no banco
                    cliente_obj.save()

                messages.success(request, 'Cliente cadastrado com sucesso!')
                # Redireciona para a página de pesquisa (para o usuário ver o resultado)
                return redirect('pesquisar_cliente')
            
            except Exception as e:
                # Se algo der errado (ex: erro no banco), avisa o usuário
                messages.error(request, f'Erro ao salvar: {e}')
        
        else:
            # Se um dos forms for inválido, os erros serão exibidos
            messages.error(request, 'Por favor, corrija os erros no formulário.')
            # Monta o contexto com os formulários preenchidos e com os erros
            contexto = {
                'cliente_form': cliente_form,
                'endereco_form': endereco_form,
            }
            # Re-renderiza a página para mostrar os erros
            return render(request, 'cliente/cadastrar_cliente.html', contexto)

    else:
        # Se for um GET (primeira vez carregando a página), cria forms vazios
        cliente_form = ClienteForm()
        endereco_form = EnderecoForm()

    # Contexto padrão para o GET
    contexto = {
        'cliente_form': cliente_form,
        'endereco_form': endereco_form,
    }
    return render(request, 'cliente/cadastrar_cliente.html', contexto)

# Funções que apenas exibem páginas, sem lógica de CRUD
def index(request):
    return render(request, 'index.html')

def index_divida(request):
    return render(request, 'divida/index_divida.html')


def index_pagamento(request):
    """Renderiza o menu de opções para pagamentos."""
    return render(request, 'pagamento/index_pagamento.html')

# lógica de quitar todas as dívidas
def _processar_pagar_tudo(request, cpf_cliente):
    cliente_a_pagar = get_object_or_404(Cliente, cpf=cpf_cliente)
    dividas_a_pagar = Divida.objects.filter(cliente=cliente_a_pagar, status__in=['Pendente', 'Parcial'])

    with transaction.atomic():
        for divida in dividas_a_pagar:
            Pagamento.objects.create(
                divida=divida,
                cliente=divida.cliente,
                valor_pago=divida.saldo_restante,
                status='Concluído'
            )
            divida.saldo_restante = 0
            divida.status = 'Pago'
            divida.save()
    
    messages.success(request, f'Todas as dívidas de {cliente_a_pagar.nome} foram quitadas com sucesso!')
    return redirect('lista_pagamentos')


def _salvar_pagamento_unico(request, form):
    """Extraído para reduzir complexidade cognitiva do registrar_pagamento"""
    pagamento = form.save(commit=False)
    divida = pagamento.divida
    pagamento.cliente = divida.cliente

    if pagamento.valor_pago > divida.saldo_restante:
        messages.error(request, f'O valor do pagamento não pode ser maior que o saldo da dívida (R$ {divida.saldo_restante}).')
    else:
        with transaction.atomic():
            divida.saldo_restante -= pagamento.valor_pago
            divida.status = 'Pago' if divida.saldo_restante == 0 else 'Parcial'
            divida.save()
            pagamento.save()
        messages.success(request, f'Pagamento de R$ {pagamento.valor_pago} registrado com sucesso!')
        return redirect('lista_pagamentos')
    return None


def registrar_pagamento(request):
    if request.method == 'POST' and 'pagar_tudo' in request.POST:
        cpf = request.POST.get('cpf_cliente')
        return _processar_pagar_tudo(request, cpf)

    # --- Fluxo normal de pagamento único ---
    form = PagamentoForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        resultado = _salvar_pagamento_unico(request, form)
        if resultado:
            return resultado
            
    # --- Cenário 3: GET -> Busca de Cliente ---
    cliente = dividas_do_cliente = None
    soma_total = Decimal('0.00')
    cpf_busca = request.GET.get('cpf_cliente')
    
    clientes = Cliente.objects.all()

    if cpf_busca:
        try:
            cliente = Cliente.objects.get(cpf=cpf_busca)
            dividas_do_cliente = Divida.objects.filter(cliente=cliente, status__in=['Pendente', 'Parcial'])
            
            if dividas_do_cliente:
                soma = dividas_do_cliente.aggregate(soma=Sum('saldo_restante'))['soma']
                soma_total = soma or Decimal('0.00')
                form.fields['divida'].queryset = dividas_do_cliente
                
        except Cliente.DoesNotExist:
            messages.error(request, 'Nenhum cliente encontrado com o CPF informado.')

    return render(request, 'pagamento/registrar_pagamento.html', {
        'form': form,
        'cliente': cliente,
        'dividas_do_cliente': dividas_do_cliente,
        'soma_total': soma_total,
        'clientes': clientes
    })


def lista_pagamentos(request):
    """Exibe um relatório com todos os pagamentos registrados, com filtros."""
    pagamentos = Pagamento.objects.all().order_by('-data_pagamento')
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    cliente_busca = request.GET.get('cliente')

    if data_inicio:
        pagamentos = pagamentos.filter(data_pagamento__gte=data_inicio)
        
    if data_fim:
        pagamentos = pagamentos.filter(data_pagamento__lte=data_fim)
        
    if cliente_busca:
        pagamentos = pagamentos.filter(
            Q(cliente__nome__icontains=cliente_busca) |
            Q(cliente__cpf__icontains=cliente_busca)
        )

    total_filtrado = pagamentos.aggregate(total=Sum('valor_pago'))['total'] or 0

    contexto = {
        'pagamentos': pagamentos,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
        'cliente_busca': cliente_busca,
        'total_filtrado': total_filtrado,
    }
    
    return render(request, 'pagamento/lista_pagamentos.html', contexto)

def pesquisar_cliente(request):
    clientes = None
    query_nome = request.GET.get('nome_cliente')
    query_cpf = request.GET.get('cpf_cliente')
    if query_nome or query_cpf:
        queries = Q() 
        if query_nome:
            queries &= Q(nome__icontains=query_nome) 
        if query_cpf:
            queries &= Q(cpf__icontains=query_cpf)
        clientes = Cliente.objects.filter(queries)
    contexto = {
        'clientes': clientes
    }
    return render(request, 'cliente/pesquisar_cliente.html', contexto)


def editar_cliente(request, cpf_cliente):
    # 1. Busca o cliente pelo CPF e o seu endereço associado
    cliente = get_object_or_404(Cliente, cpf=cpf_cliente)
    endereco = cliente.endereco

    # 2. Se for um POST (clicou em "Salvar Alterações")
    if request.method == 'POST':
        # Carrega os formulários com os dados enviados (request.POST) 
        # e também com as instâncias (para saber QUE registro atualizar)
        cliente_form = ClienteForm(request.POST, instance=cliente)
        endereco_form = EnderecoForm(request.POST, instance=endereco)

        if cliente_form.is_valid() and endereco_form.is_valid():
            try:
                # Salva os dois formulários dentro de uma transação
                with transaction.atomic():
                    endereco_form.save()
                    cliente_form.save() # O cliente já está ligado ao endereço

                messages.success(request, 'Cliente atualizado com sucesso!')
                return redirect('pesquisar_cliente')
            except Exception as e:
                messages.error(request, f'Erro ao salvar: {e}')
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')

    # 3. Se for um GET (carregando a página pela primeira vez)
    else:
        # Cria os formulários preenchidos com os dados do banco
        cliente_form = ClienteForm(instance=cliente)
        endereco_form = EnderecoForm(instance=endereco)
    contexto = {
        'cliente_form': cliente_form,
        'endereco_form': endereco_form,
        'cliente_nome': cliente.nome # Para o título da página
    }
    return render(request, 'cliente/editar_cliente.html', contexto)


def excluir_cliente(request, cpf_cliente):
    cliente = get_object_or_404(Cliente, cpf=cpf_cliente)
    if request.method == 'POST':
        try:
            nome_cliente = cliente.nome
            cliente.delete()
            messages.success(request, f"Cliente '{nome_cliente}' foi excluído com sucesso.")
        except Exception as e:
            messages.error(request, f"Erro ao excluir cliente: {e}")
    
    return redirect('pesquisar_cliente')

def index_cliente(request):
    """Renderiza o menu de opções para Clientes."""
    return render(request, 'cliente/index_cliente.html')


def index_relatorios(request):
    return render(request, 'relatorios/index_relatorios.html')


def relatorio_mensal_dividas(request):

    mes = request.GET.get("mes")
    ano = request.GET.get("ano")

    dividas = Divida.objects.filter(status__in=["Pendente", "Parcial"])

    # valida mês
    if mes:
        mes = int(mes)
        if mes < 1 or mes > 12:
            messages.error(request, "Mês inválido")
            dividas = Divida.objects.none()
        else:
            dividas = dividas.filter(data_divida__month=mes)

    # valida ano
    if ano:
        ano = int(ano)
        dividas = dividas.filter(data_divida__year=ano)

    total_dividas = dividas.aggregate(total=Sum('valor'))['total'] or 0

    return render(request, "relatorios/relatorio_mensal_dividas.html", {
        "dividas": dividas,
        "total_dividas": total_dividas,
        "mes": mes,
        "ano": ano
    })
def alertas_inadimplencia(request):
    """Lista clientes com dívidas vencidas e saldo pendente."""
    hoje = timezone.now().date()
    
    dividas_atrasadas = Divida.objects.filter(
        data_vencimento__lt=hoje,
        saldo_restante__gt=0
    ).order_by('data_vencimento')

    return render(request, 'divida/alertas_inadimplencia.html', {
        'dividas_atrasadas': dividas_atrasadas
    })