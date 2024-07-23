from django.db import models

class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    dpto = models.CharField(max_length=10, blank=True, null=True)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    
    def _str_(self):
        return f"{self.calle} {self.numero}, {self.comuna}, {self.ciudad}, {self.region}"

class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)

    def _str_(self):
        return f"{self.nombre} {self.apellido}"

class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    version = models.IntegerField()
    profesor = models.OneToOneField(Profesor, on_delete=models.CASCADE)

    def _str_(self):
        return self.nombre

class CursoEstudiante(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='estudiantes')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='cursos')

    class Meta:
        unique_together = ('curso', 'estudiante')

