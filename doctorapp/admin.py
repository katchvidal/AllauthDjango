from django.contrib import admin
from .models import Doctor, Paciente, Notas
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'nombre', 'apellidopaterno', 'especialidad',  )

class PacienteAdmin(admin.ModelAdmin):
    list_display = ( 'id',  'nombre', 'apellidopaterno', 'doctor', )


class NotasAdmin(admin.ModelAdmin):
    list_display = ( 'id',  'titulo', 'fecha', 'doctor', 'paciente', )



admin.site.register(Notas, NotasAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register( Permission)
admin.site.register( ContentType )