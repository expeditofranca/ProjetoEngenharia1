from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Cliente, Divida, Pagamento
from .serializers import ClienteSerializer, DividaSerializer

import json

@api_view(['GET'])
def get_dividas(request):
    if request.method == 'GET':
        dividas = Divida.objects.all()

        serializer = DividaSerializer(dividas, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

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
        try:
            if request.GET.get('divida'):
                cod_divida = request.GET.get('divida')

                try:
                    divida = Divida.objects.get(pk=cod_divida)
                except Divida.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                serializer = DividaSerializer(divida)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Divida.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'POST':
        new_divida_data = request.data

        serializer = DividaSerializer(data=new_divida_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

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

    return Response(status=status.HTTP_400_BAD_REQUEST)