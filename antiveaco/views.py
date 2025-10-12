from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Cliente, Divida, Pagamento
from .serializers import ClienteSerializer, DividaSerializer

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

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def divida_manager(request):
    if request.method == 'GET':
        return render(request, 'divida/cadastrar_divida.html', {
            'form': DividaForm()
        })
    
    elif request.method == 'POST':
        form = DividaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'divida/cadastrar_divida.html', {
                'form': DividaForm(),
                'mensagem': 'Dívida cadastrada com sucesso!'
            })

    elif request.method == 'PUT':
        cod_divida = request.data.get('cod_divida')

        try:
            update_divida_data = Divida.objects.get(pk=cod_divida)
        except Divida.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = DividaSerializer(update_divida_data, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
    elif request.method == 'DELETE':
        try:
            divida_to_delete = Divida.objects.get(pk=request.data.get('cod_divida'))
            divida_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Divida.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return render(request, 'index.html')

def index_divida(request):
    return render(request, 'divida/index_divida.html')