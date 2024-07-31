import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inmuebles_en_arriendo.settings')
django.setup()

from Arriendos_app.models import Inmueble, Comuna, Region

def consultar_inmuebles_por_comunas():
    resultado = {}
    comunas = Comuna.objects.all()
    
    for comuna in comunas:
        inmuebles = Inmueble.objects.filter(comuna=comuna).values('nombre', 'descripcion')
        resultado[comuna.nombre] = list(inmuebles)
    
    with open('inmuebles_por_comunas.txt', 'w') as file:
        for comuna, inmuebles in resultado.items():
            file.write(f"Comuna: {comuna}\n")
            for inmueble in inmuebles:
                file.write(f"  Nombre: {inmueble['nombre']}\n")
                file.write(f"  Descripción: {inmueble['descripcion']}\n")
            file.write("\n")

def consultar_inmuebles_por_regiones():
    resultado = {}
    regiones = Region.objects.all()
    
    for region in regiones:
        inmuebles = Inmueble.objects.filter(comuna__region=region).values('nombre', 'descripcion')
        resultado[region.nombre] = list(inmuebles)
    
    with open('inmuebles_por_regiones.txt', 'w') as file:
        for region, inmuebles in resultado.items():
            file.write(f"Región: {region}\n")
            for inmueble in inmuebles:
                file.write(f"  Nombre: {inmueble['nombre']}\n")
                file.write(f"  Descripción: {inmueble['descripcion']}\n")
            file.write("\n")

if __name__ == "__main__":
    consultar_inmuebles_por_comunas()
    consultar_inmuebles_por_regiones()