from django.conf.urls import url
from django.views.generic.edit import FormView
from doctorapp.models import Notas
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from .models import Notas
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .form import NotaForm
from django.urls import reverse_lazy
from .mixin import SuperUserMixin, ValidPermissionMixin

# Create your views here.

#   Pagina de Entrada para Personas que Puedan Logguear
class doctorhome(LoginRequiredMixin, TemplateView):
    template_name = 'public/doctor/inicio.html'

#   Formulario Para Crear Notas -> Requiere de un Permiso 
class doctornotas( ValidPermissionMixin, SuccessMessageMixin, CreateView ):
    form_class = NotaForm
    model = Notas
    template_name = 'public/doctor/crearnotas.html'
    permission_required = 'notas'
    success_url = reverse_lazy('docnota')
    success_message = "%(titulo)s was created successfully"
