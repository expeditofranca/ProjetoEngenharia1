from rest_framework import serializers
from .models import Cliente, Divida

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class DividaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divida
        fields = '__all__'