from django.db import models
from django.db.models import fields
# models.py
from django.forms import ModelForm
from .models import Notas

class NotaForm(ModelForm):

    class Meta:
        model = Notas
        fields = '__all__'