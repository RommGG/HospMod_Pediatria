from django.db import models
from mongoengine import Document, fields
from djongo.models import DjongoManager
# Create your models here.
class nacimientosBebes(models.Model):
    fecha_nacimiento = models.DateField(null=True)
    hora_nacimiento = models.TimeField(null=True)
    lugar_nacimiento = models.CharField(max_length=100, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    longitud = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    nombre_padre = models.CharField(max_length=100, null=True)
    nombre_madre = models.CharField(max_length=100, null=True)
    telefono_contacto = models.CharField(max_length=20, null=True)
    email_contacto = models.EmailField(null=True)
    observaciones = models.TextField(null=True)
    tipo_nacimiento = models.CharField(max_length=10, null=True)
    frecuencia_cardiaca = models.IntegerField(null=True)
    temperatura = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    presion_arterial_sistolica = models.IntegerField(null=True)
    presion_arterial_diastolica = models.IntegerField(null=True)
    sexo = models.CharField(max_length=15, null=True)

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre_padre} y {self.nombre_madre}"

class ViewNacimientos(models.Model):
    total_pacientes = models.IntegerField(primary_key=True)
    pn_masculino = models.IntegerField(null=True)
    pn_femeninos = models.IntegerField(null=True)
    c_masculino = models.IntegerField(null=True)
    c_femenino = models.IntegerField(null=True)
    class Meta:
        managed = False  # Indicar que Django no debe manejar la tabla de la base de datos
        db_table = 'vw_nacimientos_genero'

class ViewNacimientosCiudad(models.Model):
    id = models.IntegerField(primary_key=True)
    lugar_nacimiento = models.CharField(max_length=100, null=True)
    cantidad_nacimientos = models.IntegerField(null=True)
    class Meta:
        managed = False  # Indicar que Django no debe manejar la tabla de la base de datos
        db_table = 'vw_nacimientos_por_ciudad'