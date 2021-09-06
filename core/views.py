from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.models import User
from .form import RegisterForm
from django.urls import reverse_lazy

class home( LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

class Registro( generic.CreateView):
    model=User
    form_class=RegisterForm
    template_name = 'register.html'
    success_url= reverse_lazy('home')