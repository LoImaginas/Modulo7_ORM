from django.db import models

# Create your models here.

class AdlTest(models.Model):
    campo1 = models.CharField(max_length=100) # Define una columna 'campo1' de tipo char con un máximo de 100 caracteres.
    valor1 = models.IntegerField() # Define una columna 'valor1' de tipo integer.

    def __str__(self):  #sobre escritura
        return f"{self.campo1} - {self.valor1}" # Devuelve una representación en string del modelo.