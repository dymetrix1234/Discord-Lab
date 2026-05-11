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

def listar_tareas(lista_tareas):
    '''
    Formatea la lista de tereas para su visualizacion
    '''
    if not lista_tareas:
        return "No hay tareas pendientes."
    
    #agregar una variable llamada resultado
    resultado = "listado de tareas \n"

    #iterar lista de tareas y formatear la salida
    for i, tarea in enumerate(lista_tareas, start=1):
        resultado += f"{i}, {tarea}\n"
    return resultado

def eliminar_tarea(lista_tareas, indice):
    '''
    Elimina una tarea de la lista si el indice es valido
    '''
    if indice < 1 or indice > len(lista_tareas):
        return "Indice invalido."
    
    tarea_eliminada = lista_tareas.pop(indice - 1)
    return f"Tarea '{tarea_eliminada}' eliminada exitosamente."