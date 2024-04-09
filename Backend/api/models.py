from django.db import models

#modicando el model

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
    tipo_nacimiento = models.CharField(max_length=8, choices=[('normal', 'Normal'), ('cesarea', 'Cesárea')], null=True)
    frecuencia_cardiaca = models.IntegerField(null=True)
    temperatura = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    presion_arterial_sistolica = models.IntegerField(null=True)
    presion_arterial_diastolica = models.IntegerField(null=True)

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre_padre} y {self.nombre_madre}"



class SeguimientoPediatrico(models.Model):
    id_paciente = models.OneToOneField(nacimientosBebes, on_delete=models.CASCADE, primary_key=True)
    cita_id = models.IntegerField(null=True)
    fecha_seguimiento = models.DateField(null=True)
    edad_anios = models.IntegerField(null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    longitud = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    perimetro_cranial = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    temperatura = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    frecuencia_respiratoria = models.IntegerField(null=True)
    frecuencia_cardiaca = models.IntegerField(null=True)
    presion_arterial_sistolica = models.IntegerField(null=True)
    presion_arterial_diastolica = models.IntegerField(null=True)
    vacunas_administradas = models.TextField(null=True)
    examenes_medicos_realizados = models.TextField(null=True)
    observaciones = models.TextField(null=True)

    def __str__(self):
        return f"ID Paciente: {self.id_paciente}, Fecha seguimiento: {self.fecha_seguimiento}"
