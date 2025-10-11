from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dividas/', views.get_dividas, name='get_all_dividas'),
]