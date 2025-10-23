from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dividas/gerenciar/', views.index_divida, name='index_divida'),
    path('dividas/cadastrar/', views.divida_manager, name='cadastrar_divida'),
    path('dividas/pesquisar/', views.get_dividas, name='pesquisar_divida'),
    path('dividas/atualizar/<int:cod_divida>/', views.divida_manager, name='atualizar_divida'),
    path('dividas/excluir/<int:cod_divida>/', views.divida_manager, name='excluir_divida'),
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('pagamentos/painel/', views.index_pagamento, name='index_pagamento'),
    path('pagamentos/registrar/', views.registrar_pagamento, name='registrar_pagamento'),
    path('pagamentos/', views.lista_pagamentos, name='lista_pagamentos'),
]