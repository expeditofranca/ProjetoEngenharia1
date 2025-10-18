from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse, HttpResponse
from django.contrib import messages

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Cliente, Divida, Pagamento
from .serializers import ClienteSerializer, DividaSerializer

from .forms import PagamentoForm
from .models import Pagamento

from .forms import DividaForm

import json

@api_view(['GET'])
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

@api_view(['GET'])
def get_divida_by_id(request, cod_divida):
    try:
        divida = Divida.objects.get(pk=cod_divida)
    except Divida.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DividaSerializer(divida)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def divida_manager(request, cod_divida=None):
    divida = get_object_or_404(Divida, pk=cod_divida)
    template = 'divida/cadastrar_divida.html'

    if 'excluir' in request.POST and divida:
        divida.delete()
        messages.success(request, 'Dívida excluída com sucesso!')
        return redirect('pesquisar_divida')

    if cod_divida:
        template = 'divida/atualizar_divida.html'
        
    if request.method == 'POST':
        form = DividaForm(request.POST, instance=divida)
        if form.is_valid():
            form.save()
            mensagem = (
                'Dívida atualizada com sucesso!'
                if divida else 'Dívida cadastrada com sucesso!'
            )
            if divida:
                messages.success(request, 'Dívida atualizada com sucesso!')
                return redirect('pesquisar_divida')

            else:
                return render(request, template, {
                    'form': DividaForm(),
                    'mensagem': mensagem
                })
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
    """Controla o formulário de registro de um novo pagamento."""
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            pagamento = form.save(commit=False)
            divida = pagamento.divida
            divida.valor -= pagamento.valor_pago
            if divida.valor <= 0:
                divida.valor = 0
                divida.status = 'Pago'
            
            divida.save()
            pagamento.cliente = divida.cliente
            pagamento.save()
            
            messages.success(request, f'Pagamento de R$ {pagamento.valor_pago} registrado com sucesso!')
            return redirect('lista_pagamentos')
    else:
        form = PagamentoForm()
    
    return render(request, 'pagamento/registrar_pagamento.html', {'form': form})

def lista_pagamentos(request):
    """Exibe um relatório com todos os pagamentos registrados."""
    pagamentos = Pagamento.objects.all().order_by('-data_pagamento')
    return render(request, 'pagamento/lista_pagamentos.html', {'pagamentos': pagamentos})