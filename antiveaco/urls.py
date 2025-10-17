from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dividas/cadastrar/', views.divida_manager, name='divida_manager'),
    path('dividas/pesquisar/', views.get_dividas, name='pesquisar_divida'),
    path('dividas/atualizar/<int:cod_divida>/', views.divida_manager, name='atualizar_divida'),
    path('dividas/excluir/<int:cod_divida>/', views.divida_manager, name='excluir_divida'),
]