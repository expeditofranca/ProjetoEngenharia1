from django.db import models

class Cliente(models.Model):
    cpf = models.CharField(max_length=11, unique=True, primary_key=True, default='')
    name = models.CharField(max_length=100, default='')
    telefone = models.CharField(max_length=15, default='')
    profissao = models.CharField(max_length=100, default='')
    renda_mensal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bairro = models.CharField(max_length=100, default='')
    rua = models.CharField(max_length=100, default='')
    numero = models.CharField(max_length=10, default='')

    def __str__(self):
        return f'{self.name} ({self.cpf})'
    

class Divida(models.Model):
    cod_divida = models.AutoField(primary_key=True)
    cpf_funcionario = models.CharField(max_length=11, default='')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_divida = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pendente')
    num_notafiscal = models.CharField(max_length=50, default='')

    def __str__(self):
        return f'Dívida {self.id} - Cliente: {self.cliente.name} - Valor: {self.valor}'

class Compra(models.Model):
    cod_compra = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    divida = models.ForeignKey(Divida, on_delete=models.SET_NULL, null=True, blank=True)
    data_compra = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fiado = models.BooleanField(default=False)
    status = models.CharField(max_length=20, default='Pendente')

    def __str__(self):
        return f'Compra {self.id} - Cliente: {self.cliente.name} - Data: {self.data_compra}'
    
class Pagamento(models.Model):
    cod_pagamento = models.AutoField(primary_key=True)
    divida = models.ForeignKey(Divida, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pagamento = models.DateField(auto_now_add=True)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, default='Concluído')

    def __str__(self):
        return f'Pagamento {self.id} - Cliente: {self.cliente.name} - Dívida: {self.divida.id} - Valor Pago: {self.valor_pago}'