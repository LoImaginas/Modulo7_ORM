from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.all().prefetch_related('subtareas')
    data = []
    for tarea in tareas:
        subtareas = list(tarea.subtareas.all())
        data.append({'tarea': tarea, 'subtareas': subtareas})
    return data

def crear_nueva_tarea(descripcion):
    tarea = Tarea.objects.create(descripcion=descripcion)
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(tarea_id, descripcion):
    tarea = Tarea.objects.get(id=tarea_id)
    subtarea = SubTarea.objects.create(tarea=tarea, descripcion=descripcion)
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(subtarea_id):
    subtarea = SubTarea.objects.get(id=subtarea_id)
    subtarea.delete()
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla(data):
    for item in data:
        tarea = item['tarea']
        subtareas = item['subtareas']
        print(f"[{tarea.id}] {tarea.descripcion}")
        for subtarea in subtareas:
            print(f".... [{subtarea.id}] {subtarea.descripcion}")