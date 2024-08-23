from django.db import models
from django.contrib.auth.models import User

class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Debe estar presente
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=255)
    telefono_personal = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES, default='arrendatario')

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Region(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class TipoInmueble(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Inmueble(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    m2_construidos = models.IntegerField()
    m2_terreno = models.IntegerField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE)
    precio_arriendo = models.DecimalField(max_digits=10, decimal_places=2)
    arrendador = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo_usuario': 'arrendador'})
    imagen_url = models.URLField(max_length=200, null=True, blank=True, default='')
    
    def __str__(self):
        return self.nombre

class InmuebleUsuario(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):           
        return self.nombre

class Contacto(models.Model):
    arrendatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo_usuario': 'arrendatario'})
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    remitente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensajes_enviados')
    destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Mensaje de {self.remitente} a {self.destinatario} sobre {self.inmueble}'
