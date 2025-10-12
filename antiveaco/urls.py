from django.urls import path
from . import views

urlpatterns = [
    path('dividas/', views.lista_dividas, name='lista_dividas'),
    path('dividas/adicionar/', views.adicionar_divida, name='adicionar_divida'),
    path('dividas/editar/<int:cod_divida>/', views.editar_divida, name='editar_divida'),
    path('dividas/deletar/<int:cod_divida>/', views.deletar_divida, name='deletar_divida'),
]