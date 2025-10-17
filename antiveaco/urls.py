from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dividas/', views.get_dividas, name='get_all_dividas'),
<<<<<<< HEAD
    path('dividas/gerenciar/', views.index_divida, name='index_divida'),
    path('dividas/<int:cod_divida>/', views.get_divida_by_id, name='get_divida_by_id'),
    path('data/', views.divida_manager, name='divida_manager'),
    path('dividas/cadastrar/', views.divida_manager, name='cadastrar_divida'), # corrigido nome duplicado de divida_manager
=======
    path('dividas/cadastrar/', views.divida_manager, name='cadastrar_divida'),
>>>>>>> ccd932c (nomes das urls atualizados)
    path('dividas/pesquisar/', views.get_dividas, name='pesquisar_divida'),
    path('dividas/atualizar/<int:cod_divida>/', views.divida_manager, name='atualizar_divida'),
    path('dividas/excluir/<int:cod_divida>/', views.divida_manager, name='excluir_divida'),
]