from .models import Vehiculo, Chofer, RegistroContabilidad
from datetime import date

def imprimir_modelos():
    print("Modelos de Vehículos")
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        print(f"Vehículo: Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Patente: {vehiculo.patente}, Año: {vehiculo.year}")

    print("\nModelos de Choferes")
    choferes = Chofer.objects.all()
    for chofer in choferes:
        print(f"Chofer: RUT: {chofer.rut}, Nombre: {chofer.nombre}, Apellido: {chofer.apellido}, Activo: {chofer.activo}")

    print("\nModelos de Registros Contables")
    registros = RegistroContabilidad.objects.all()
    for registro in registros:
        print(f"Registro Contable: Fecha de Compra: {registro.fecha_compra}, Valor: {registro.valor}, Vehículo: {registro.vehiculo}")


def crear_vehiculo(pPatente, pMarca, pModelo, pYear):
    # Si pYear es una fecha datetime.date, extraemos el año
    year_value = pYear.year if isinstance(pYear, date) else pYear
    vehiculo = Vehiculo(patente=pPatente, marca=pMarca, modelo=pModelo, year=year_value)
    vehiculo.save()
    imprimir_modelos()
    return vehiculo

def crear_chofer(pRut, pNombre, pApellido, pVehiculo, pActivo, pCreacion_registro):
    chofer = Chofer(rut=pRut, nombre=pNombre, apellido=pApellido, vehiculo=pVehiculo, activo=pActivo, creacion_registro=pCreacion_registro)
    chofer.save()
    imprimir_modelos()
    return chofer


def crear_registro_contable(pFecha_compra, pValor, pVehiculo):
    registro = RegistroContabilidad(fecha_compra=pFecha_compra, valor=pValor, vehiculo=pVehiculo)
    registro.save()
    imprimir_modelos()
    return registro

def deshabilitar_chofer(pRut):
    chofer = Chofer.objects.get(rut=pRut)
    chofer.activo = False
    chofer.save()
    imprimir_modelos()

def habilitar_chofer(pRut):
    chofer = Chofer.objects.get(rut=pRut)
    chofer.activo = True
    chofer.save()
    imprimir_modelos()

def deshabilitar_vehiculo(pPatente):
    vehiculo = Vehiculo.objects.get(patente=pPatente)
    vehiculo.activo = False
    vehiculo.save()
    imprimir_modelos()

def habilitar_vehiculo(pPatente):
    vehiculo = Vehiculo.objects.get(patente=pPatente)
    vehiculo.activo = True
    vehiculo.save()
    imprimir_modelos()

def obtener_vehiculo(pPatente):
    return Vehiculo.objects.get(patente=pPatente)
   
def obtener_chofer(pRut):
    return Chofer.objects.get(rut=pRut)
    
def asignar_chofer_a_vehiculo(pRut, pPatente):
    chofer = Chofer.objects.get(rut=pRut)
    vehiculo = Vehiculo.objects.get(patente=pPatente)
    chofer.vehiculo = vehiculo
    chofer.save()
    imprimir_modelos()
    
def imprimir_datos_vehiculos():
    print("Datos de Vehículos")
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        print(f"Vehículo: Patente: {vehiculo.patente}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.year}")