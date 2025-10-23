from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from django.db import transaction
from django.db.models import Sum
from decimal import Decimal

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Cliente, Divida, Pagamento
from .serializers import ClienteSerializer, DividaSerializer

from .forms import PagamentoForm
from .models import Pagamento

from .models import Cliente, Divida, Pagamento
from .forms import DividaForm

import json

def get_dividas(request):
    dividas = Divida.objects.all()

    cpf = request.GET.get('cpf_cliente')
    status = request.GET.get('status')
    valor_min = request.GET.get('valor_min')
    valor_max = request.GET.get('valor_max')

    if cpf:
        dividas = dividas.filter(cliente__cpf__icontains=cpf)
    if status:
        dividas = dividas.filter(status=status)
    if valor_min:
        dividas = dividas.filter(valor__gte=valor_min)
    if valor_max:
        dividas = dividas.filter(valor__lte=valor_max)

    return render(request, 'divida/pesquisar_divida.html', {'dividas': dividas})

def divida_manager(request, cod_divida=None):
    divida = None
    template = 'divida/cadastrar_divida.html'

    if cod_divida:
        divida = get_object_or_404(Divida, pk=cod_divida)
        if 'excluir' in request.POST and divida:
            divida.delete()
            messages.success(request, 'Dívida excluída com sucesso!')
            return redirect('pesquisar_divida')
        template = 'divida/atualizar_divida.html'
        
    if request.method == 'POST':
        form = DividaForm(request.POST, instance=divida)
        if form.is_valid():
            form.save()
            if divida:
                messages.success(request, 'Dívida atualizada com sucesso!')
                return redirect('pesquisar_divida')
            else:
                messages.success(request, 'Dívida cadastrada com sucesso!')
                return redirect('pesquisar_divida')
        else:
            return render(request, template, {
                'form': form,
                'erro': 'Erro ao salvar os dados.',
                'divida': divida
            })
    else:
        if divida:
            template = 'divida/atualizar_divida.html'
    
    form = DividaForm(instance=divida)
    return render(request, template, {
        'form': form,
        'divida': divida
    })

# Funções que apenas exibem páginas, sem lógica de CRUD
def index(request):
    return render(request, 'index.html')

def index_divida(request):
    return render(request, 'divida/index_divida.html')


def index_pagamento(request):
    """Renderiza o menu de opções para pagamentos."""
    return render(request, 'pagamento/index_pagamento.html')

def registrar_pagamento(request):
    cliente = None
    dividas_do_cliente = None
    soma_total = Decimal('0.00')
    form = PagamentoForm()

    # --- Lógica de Busca do Cliente (GET) ---
    cpf_busca = request.GET.get('cpf_cliente')
    if cpf_busca:
        try:
            cliente = Cliente.objects.get(cpf=cpf_busca)
            dividas_do_cliente = Divida.objects.filter(cliente=cliente, status__in=['Pendente', 'Parcial'])
            
            if dividas_do_cliente:
                soma = dividas_do_cliente.aggregate(soma_total=Sum('valor'))['soma_total']
                soma_total = soma or Decimal('0.00')

            form.fields['divida'].queryset = dividas_do_cliente
        except Cliente.DoesNotExist:
            messages.error(request, 'Nenhum cliente encontrado com o CPF informado.')

    # --- Lógica de Processamento (POST) ---
    if request.method == 'POST':
        # --- Cenário 1: Botão "Pagar Tudo" foi pressionado ---
        if 'pagar_tudo' in request.POST:
            cpf_cliente_post = request.POST.get('cpf_cliente')
            cliente_a_pagar = get_object_or_404(Cliente, cpf=cpf_cliente_post)
            dividas_a_pagar = Divida.objects.filter(cliente=cliente_a_pagar, status__in=['Pendente', 'Parcial'])

            with transaction.atomic():
                for divida in dividas_a_pagar:
                    Pagamento.objects.create(
                        divida=divida,
                        cliente=divida.cliente,
                        valor_pago=divida.valor,
                        status='Concluído'
                    )
                    divida.valor = 0
                    divida.status = 'Pago'
                    divida.save()
            
            messages.success(request, f'Todas as dívidas de {cliente_a_pagar.nome} foram quitadas com sucesso!')
            return redirect('lista_pagamentos')

        # --- Cenário 2: Formulário de pagamento único foi enviado (LÓGICA CORRIGIDA)---
        else:
            form = PagamentoForm(request.POST)
            if form.is_valid():
                pagamento = form.save(commit=False)
                divida = pagamento.divida
                
                if pagamento.valor_pago > divida.valor:
                    messages.error(request, f'O valor do pagamento (R$ {pagamento.valor_pago}) não pode ser maior que o saldo da dívida (R$ {divida.valor}).')
                else:
                    with transaction.atomic():
                        divida.valor -= pagamento.valor_pago
                        if divida.valor <= 0:
                            divida.valor = 0
                            divida.status = 'Pago'
                        else:
                            divida.status = 'Parcial'
                        
                        divida.save()
                        pagamento.cliente = divida.cliente
                        pagamento.save()
                    
                    messages.success(request, f'Pagamento de R$ {pagamento.valor_pago} registrado com sucesso!')
                    return redirect('lista_pagamentos')

    context = {
        'form': form,
        'cliente': cliente,
        'dividas_do_cliente': dividas_do_cliente,
        'soma_total': soma_total
    }
    return render(request, 'pagamento/registrar_pagamento.html', context)

def lista_pagamentos(request):
    """Exibe um relatório com todos os pagamentos registrados."""
    pagamentos = Pagamento.objects.all().order_by('-data_pagamento')
    return render(request, 'pagamento/lista_pagamentos.html', {'pagamentos': pagamentos})