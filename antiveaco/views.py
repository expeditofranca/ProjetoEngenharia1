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