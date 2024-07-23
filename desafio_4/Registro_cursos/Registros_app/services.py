from django.db import transaction
from .models import Estudiante, Curso, Profesor, Direccion, CursoEstudiante

def crear_direccion(calle, numero, dpto=None, comuna=None, ciudad=None, region=None):
    try:
        with transaction.atomic():
            direccion = Direccion.objects.create(
                calle=calle,
                numero=numero,
                dpto=dpto,
                comuna=comuna or "Desconocida",  # Valor predeterminado para comuna
                ciudad=ciudad,
                region=region,
            )
        return direccion
    except Exception as e:
        return f"Error inesperado: {str(e)}"

def crear_estudiante(rut, nombre, apellido, fecha_nac, creado_por, **direccion_data):
    with transaction.atomic():
        # Crear la dirección
        direccion = Direccion.objects.create(
            calle=direccion_data['calle'],
            numero=direccion_data['numero'],
            dpto=direccion_data.get('dpto'),  # Usamos .get() para manejar opcionalmente dpto
            comuna=direccion_data.get('comuna', 'Desconocida'),  # Valor predeterminado para comuna
            ciudad=direccion_data['ciudad'],
            region=direccion_data['region'],
        )
        
        # Crear el estudiante
        estudiante = Estudiante.objects.create(
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            fecha_nac=fecha_nac,
            creado_por=creado_por,
            direccion=direccion
        )
        return estudiante

def actualizar_estudiante(rut, **kwargs):
    estudiante = Estudiante.objects.get(rut=rut)
    for key, value in kwargs.items():
        setattr(estudiante, key, value)
    estudiante.save()
    return estudiante

def obtener_estudiante(rut):
    return Estudiante.objects.get(rut=rut)

def eliminar_estudiante(rut):
    estudiante = Estudiante.objects.get(rut=rut)
    estudiante.delete()

def crear_curso(codigo, nombre, version, profesor):
    curso = Curso.objects.create(
        codigo=codigo,
        nombre=nombre,
        version=version,
        profesor=profesor
    )
    return curso

def actualizar_curso(codigo, **kwargs):
    curso = Curso.objects.get(codigo=codigo)
    for key, value in kwargs.items():
        setattr(curso, key, value)
    curso.save()
    return curso

def obtener_curso(codigo):
    return Curso.objects.get(codigo=codigo)

def eliminar_curso(codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

def crear_profesor(rut, nombre, apellido, creado_por):
    profesor = Profesor.objects.create(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        creado_por=creado_por
    )
    return profesor

def actualizar_profesor(rut, **kwargs):
    profesor = Profesor.objects.get(rut=rut)
    for key, value in kwargs.items():
        setattr(profesor, key, value)
    profesor.save()
    return profesor

def obtener_profesor(rut):
    return Profesor.objects.get(rut=rut)

def eliminar_profesor(rut):
    profesor = Profesor.objects.get(rut=rut)
    profesor.delete()

def agregar_cursos_a_estudiante(rut_estudiante, codigo_curso):
    try:
        # Buscar el estudiante y el curso
        estudiante = Estudiante.objects.get(rut=rut_estudiante)
        curso = Curso.objects.get(codigo=codigo_curso)

        # Crear la relación CursoEstudiante
        CursoEstudiante.objects.create(curso=curso, estudiante=estudiante)

        return f"Curso {curso.nombre} agregado al estudiante {estudiante.nombre} {estudiante.apellido} correctamente."
    except Curso.DoesNotExist:
        return f"Error: El curso con código {codigo_curso} no existe."
    except Estudiante.DoesNotExist:
        return f"Error: El estudiante con rut {rut_estudiante} no existe."
    except Exception as e:
        return f"Error inesperado: {str(e)}"
    
def agrega_profesor_a_curso(id_profesor, codigo_curso):
    try:
        profesor = Profesor.objects.get(rut=id_profesor)
        curso = Curso.objects.get(codigo=codigo_curso)

        # Asignar el profesor al curso
        curso.profesor = profesor
        curso.save()

        return f"Profesor {profesor.nombre} {profesor.apellido} asignado al curso {curso.nombre} correctamente."
    except Profesor.DoesNotExist:
        return "Error: El profesor especificado no existe."
    except Curso.DoesNotExist:
        return "Error: El curso especificado no existe."
    except Exception as e:
        return f"Error inesperado: {str(e)}"   

def obtener_estudiantes_por_curso(codigo_curso):
    curso = Curso.objects.get(codigo=codigo_curso)
    return curso.cursoestudiante

def imprime_estudiante_cursos(rut_estudiante):
    try:
        estudiante = Estudiante.objects.get(rut=rut_estudiante)
        cursos = CursoEstudiante.objects.filter(estudiante=estudiante)
        if cursos.exists():
            resultado = f"Cursos de {estudiante.nombre} {estudiante.apellido}:\n"
            for curso in cursos:
                resultado += f"- {curso.curso.nombre}\n"
            return resultado
        else:
            return f"No se encontraron cursos para el estudiante con rut {rut_estudiante}"
    except Estudiante.DoesNotExist:
        return f"No se encontró un estudiante con rut {rut_estudiante}"
    except Exception as e:
        return f"Error inesperado: {str(e)}"