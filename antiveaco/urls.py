from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dividas/', views.get_dividas, name='get_all_dividas'),
    path('dividas/<int:cod_divida>/', views.get_divida_by_id, name='get_divida_by_id'),
    path('data/', views.divida_manager, name='divida_manager'),
]