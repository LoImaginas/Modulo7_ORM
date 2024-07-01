from django.db import models

class Tarea(models.Model):
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField(default=False)

class SubTarea(models.Model):
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField(default=False)
    tarea = models.ForeignKey(Tarea, related_name='subtareas', on_delete=models.CASCADE)