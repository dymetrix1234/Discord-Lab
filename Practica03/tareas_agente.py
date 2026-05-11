import datetime

def agregar_tarea(lista_tareas, descripcion):
    '''
    Agregar una tarea a la listasi cumple con los requisitos
    '''
    if descripcion < 3:
        return "Longitud invalida."
    #crear formato para tarea
    fecha = datetime.datetime.now().strftime("%H:%M")
    nueva_tarea = f"{fecha} - {descripcion}"
    lista_tareas.append(nueva_tarea)
    return f"Tarea '{descripcion}' agregada exitosamente."
