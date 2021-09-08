from typing import Pattern
from django.contrib import admin
from django.urls import path, include
from .views import doctorhome, doctornotas

urlpatterns = [
    path('inicio', doctorhome.as_view(), name='docinicio'),
    path('notas', doctornotas.as_view(), name='docnota'),
]
