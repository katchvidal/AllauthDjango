from django.db import models
from django.db.models.base import Model


# Create your models here.

    

class Doctor(models.Model):
    nombre = models.CharField( max_length=255)
    apellidopaterno = models.CharField( max_length=255, verbose_name='Apellido Paterno')
    apellidomaterno = models.CharField( max_length=255, verbose_name='Apellido Materno', blank=True, null=True)
    fechadenacimiento = models.DateField( verbose_name='Fecha de Nacimiento', blank=True, null=True )
    especialidad = models.CharField( max_length=255, blank=True, null=True )

    class Meta:
        ordering = ["apellidopaterno"]
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"

    def __str__(self):
        return self.nombre + ' ' + self.apellidopaterno 
        
class Paciente(models.Model):

    nombre = models.CharField( max_length=255, verbose_name='Nombre')
    apellidopaterno = models.CharField( max_length=255, verbose_name='Apellido Paterno')
    apellidomaterno = models.CharField( max_length=255, verbose_name='Apellido Materno', blank=True, null=True)
    fechadenacimiento = models.DateField( verbose_name='Fecha de Nacimiento', blank=True, null=True )
    doctor = models.ForeignKey( Doctor, on_delete=models.CASCADE )
    class Meta:
        ordering = ["apellidopaterno"]
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.nombre + ' ' + self.apellidopaterno

class Notas(models.Model):
    titulo = models.CharField( max_length=255 )
    contenido = models.CharField( max_length=255 )
    fecha = models.DateTimeField( auto_now_add=True )
    doctor = models.ForeignKey( Doctor, on_delete=models.CASCADE )
    paciente = models.ForeignKey( Paciente, on_delete=models.CASCADE )

    def __str__(self):
        return self.titulo

    class Meta:
        permissions = (
            ("notas", "Permiso para poder editar/crear/ver/borrar"),
        )