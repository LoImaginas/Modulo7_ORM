from django.db import models

class Tarea(models.Model):
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField(default=False) # borrado logico

class SubTarea(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField(default=False)
    tarea = models.ForeignKey(Tarea, related_name='subtareas', on_delete=models.CASCADE) #Related name = para no agregar el SET
