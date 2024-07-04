from django.db import models
import datetime

# Obtener el rango de años desde 1980 hasta el año actual
YEAR_CHOICES = [(r, r) for r in range(2000, datetime.datetime.now().year + 1)]

class Vehiculo(models.Model):
    patente = models.CharField(max_length=10, primary_key=True)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.year})"

    class Meta:
        verbose_name_plural = "Vehiculos"

class Chofer(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField
    vehiculo = models.OneToOneField(Vehiculo, max_length=6, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.rut})-{self.nombre} {self.apellido}'

class RegistroContabilidad(models.Model):
    fecha_compra = models.DateField(null=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    vehiculo = models.OneToOneField(Vehiculo,max_length=6, null=False, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Registro de compra de {self.vehiculo.patente}'
