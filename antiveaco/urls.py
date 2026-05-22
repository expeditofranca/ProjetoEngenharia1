from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    # =========================
    # Dívidas
    # =========================
    path('dividas/gerenciar/', views.index_divida, name='index_divida'),
    path('dividas/cadastrar/', views.divida_manager, name='cadastrar_divida'),
    path('dividas/pesquisar/', views.get_dividas, name='pesquisar_divida'),
    path('dividas/atualizar/<int:cod_divida>/', views.divida_manager, name='atualizar_divida'),
    path('dividas/excluir/<int:cod_divida>/', views.divida_manager, name='excluir_divida'),

    # =========================
    # CLIENTES
    # =========================
    path('dividas/alertas/', views.alertas_inadimplencia, name='alertas_inadimplencia'),
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/pesquisar/', views.pesquisar_cliente, name='pesquisar_cliente'),
    path('clientes/editar/<str:cpf_cliente>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/excluir/<str:cpf_cliente>/', views.excluir_cliente, name='excluir_cliente'),
    path('clientes/gerenciar/', views.index_cliente, name='index_cliente'),

    # =========================
    # PAGAMENTOS
    # =========================
    path('pagamentos/painel/', views.index_pagamento, name='index_pagamento'),
    path('pagamentos/registrar/', views.registrar_pagamento, name='registrar_pagamento'),
    path('pagamentos/', views.lista_pagamentos, name='lista_pagamentos'),

    # =========================
    # RELATÓRIOS
    # =========================
    path('relatorios/', views.index_relatorios, name='index_relatorios'),
    path('relatorio_mensal_dividas/', views.relatorio_mensal_dividas, name='relatorio_mensal_dividas'),
]