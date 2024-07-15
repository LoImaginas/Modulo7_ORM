from .models import Usuario, Inmueble

def crear_usuario(nombre, apellido, rut, direccion, telefono, email, tipo_usuario):
    usuario = Usuario.objects.create(
        nombre=nombre, 
        apellido=apellido, 
        rut=rut, 
        direccion=direccion, 
        telefono=telefono, 
        email=email, 
        tipo_usuario=tipo_usuario
    )
    return usuario

def obtener_usuarios():
    usuarios = Usuario.objects.all()
    return usuarios

def actualizar_usuario(usuario_id, nombre, apellido, rut, direccion, telefono, email, tipo_usuario):
    usuario = Usuario.objects.get(id=usuario_id)
    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.rut = rut
    usuario.direccion = direccion
    usuario.telefono = telefono
    usuario.email = email
    usuario.tipo_usuario = tipo_usuario
    usuario.save()
    return usuario

def borrar_usuario(usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    usuario.delete()

def crear_inmueble(nombre, descripcion, m2_construidos, m2_terreno, estacionamientos, habitaciones, banos, direccion, comuna, tipo_inmueble, precio_arriendo):
    inmueble = Inmueble.objects.create(
        nombre=nombre,
        descripcion=descripcion,
        m2_construidos=m2_construidos,
        m2_terreno=m2_terreno,
        estacionamientos=estacionamientos,
        habitaciones=habitaciones,
        banos=banos,
        direccion=direccion,
        comuna=comuna,
        tipo_inmueble=tipo_inmueble,
        precio_arriendo=precio_arriendo
    )
    return inmueble

def obtener_inmuebles():
    inmuebles = Inmueble.objects.all()
    return inmuebles


def actualizar_inmueble(inmueble_id, nombre, descripcion, m2_construidos, m2_terreno, estacionamientos, habitaciones, banos, direccion, comuna, tipo_inmueble, precio_arriendo):
    inmueble = Inmueble.objects.get(id=inmueble_id)
    inmueble.nombre = nombre
    inmueble.descripcion = descripcion
    inmueble.m2_construidos = m2_construidos
    inmueble.m2_terreno = m2_terreno
    inmueble.estacionamientos = estacionamientos
    inmueble.habitaciones = habitaciones
    inmueble.banos = banos
    inmueble.direccion = direccion
    inmueble.comuna = comuna
    inmueble.tipo_inmueble = tipo_inmueble
    inmueble.precio_arriendo = precio_arriendo
    inmueble.save()
    return inmueble


def borrar_inmueble(inmueble_id):
    inmueble = Inmueble.objects.get(id=inmueble_id)
    inmueble.delete()