    # --- TESTE 3: Pagar Tudo ---
    def test_registrar_pagamento_pagar_tudo(self):
        """Testa se o botão Pagar Tudo quita todas as dívidas pendentes do cliente"""
        url = reverse('registrar_pagamento')
        
        response = self.client.post(url, {
            'pagar_tudo': 'true',
            'cpf_cliente': self.cliente.cpf
        })
        
        self.divida.refresh_from_db()
    
        self.assertEqual(self.divida.saldo_restante, Decimal('0.00'))
        self.assertEqual(self.divida.status, 'Pago')
        self.assertEqual(Pagamento.objects.count(), 1)