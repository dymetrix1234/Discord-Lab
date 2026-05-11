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
    Elimina una tarea por su numero de indice
    '''
    if not indice.isdigit():
        return "Error: El índice debe ser un número."
    
    indice = int(indice)-1

    #agregamos la logica para preguntar si el elemento esta en la lista y eliminarla

    if 0 <= indice < len(lista_tareas):
        tarea_eliminada = lista_tareas.pop(indice)
    else:
        return "Error: No existe la tarea"
    return f"Tarea '{tarea_eliminada}' eliminada exitosamente."

def main ():
    tareas = []
    PREFIJO = "!"

    print ("bienvenido al gestor de tareas")
    activa = True
    while activa:
        entrada = input(">>> ").strip()
        if not entrada.startswith(PREFIJO):
            print("Error: Comando no reconocido.")
            continue

        #procesamiento de la enrada
        cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""

        #seleccion de accion
        if comando == "add":
            resultado = agregar_tarea(tareas, argumento)
            print
            