from rest_framework import serializers
from .models import Cliente, Compra, Divida, Pagamento

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'