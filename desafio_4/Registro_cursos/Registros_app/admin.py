from django.contrib import admin
from .models import Direccion, Profesor, Estudiante, Curso

# Registrar los modelos en el admin
admin.site.register(Direccion)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Curso)