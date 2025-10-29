from django.db import models


class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.logradouro}, {self.numero}, {self.cidade}'
    
class Cliente(models.Model):
    nome = models.CharField(max_length=255, default='')
    telefone = models.CharField(max_length=15, default='')
    cpf = models.CharField(max_length=11, unique=True, primary_key=True, default='')
    profissao = models.CharField(max_length=255, default='')
    renda_familiar = models.FloatField(max_length=10, default=0)
    status_cliente = models.BooleanField(default=True)

    endereco = models.OneToOneField(Endereco,on_delete=models.CASCADE)

    def __str__(self):
        return  f'{self.nome} ({self.cpf})'
    

class Divida(models.Model):
    cod_divida = models.AutoField(primary_key=True)
    cpf_funcionario = models.CharField(max_length=11, default='')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_divida = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pendente')
    num_notafiscal = models.CharField(max_length=50, default='')

    def __str__(self):
        return f'Dívida {self.cod_divida} - Cliente: {self.cliente.nome} - Valor: {self.valor}'
    
class Pagamento(models.Model):
    cod_pagamento = models.AutoField(primary_key=True)
    divida = models.ForeignKey(Divida, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pagamento = models.DateField(auto_now_add=True)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, default='Concluído')

    def __str__(self):
        return f'Pagamento {self.id} - Cliente: {self.cliente.name} - Dívida: {self.divida.id} - Valor Pago: {self.valor_pago}'