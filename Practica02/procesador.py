import datetime

# --- Definición de Funciones de Lógica ---

def obtener_saludo(nombre_bot):
    """Retorna un saludo formateado."""
    return f"🤖 Hola, soy {nombre_bot}. Estoy listo para procesar tus comandos."

def procesar_comando_recordar(argumento):
    """Valida y procesa la acción de recordar un dato."""
    if not argumento:
        return "⚠️ Error: Falta el nombre. Uso: !recordar [nombre]"
    return f"✅ Dato recibido: '{argumento}'. (Nota: En esta fase, los datos no se guardan permanentemente)."

def calcular_uptime(hora_inicio):
    """Calcula la diferencia de tiempo entre el inicio y el momento actual."""
    ahora = datetime.datetime.now()
    diferencia = ahora - hora_inicio
    segundos = int(diferencia.total_seconds())
    return f"⏳ Tiempo de ejecución: {segundos} segundos."

def mostrar_ayuda():
    """Retorna la lista de comandos disponibles."""
    return (
        "📜 Comandos disponibles:\n"
        "  !saludo   - Muestra el saludo del bot.\n"
        "  !recordar - Simula el registro de un nombre.\n"
        "  !tiempo   - Muestra cuánto lleva el programa abierto.\n"
        "  !salir    - Termina la simulación."
    )

# --- Función Principal (Control de Flujo) ---

def iniciar_agente():
    NOMBRE_BOT = "PyBot_V2"
    PREFIJO = "!"
    hora_inicio_programa = datetime.datetime.now()
    
    print(f"--- Simulación de {NOMBRE_BOT} Iniciada ---")
    print("Escribe '!ayuda' para ver los comandos disponibles.\n")
    
    ejecutando = True
    
    while ejecutando:
        entrada = input(f"[{NOMBRE_BOT}] Ingrese comando: ").strip()
        
        # Validar si es un comando (empieza con el prefijo)
        if not entrada.startswith(PREFIJO):
            print("❌ Error: Los comandos deben empezar con '!'\n")
            continue
            
        # Separar el comando del argumento
        # Ejemplo: "!recordar Juan" -> comando="recordar", argumento="Juan"
        partes = entrada[len(PREFIJO):].split(maxsplit=1)
        comando = partes[0].lower()
        argumento = partes[1] if len(partes) > 1 else ""
        
        # Estructura de decisión (Switch-case simulado con if-elif)
        if comando == "salir":
            print("Desconectando agente... ¡Adiós!")
            ejecutando = False
            
        elif comando == "ayuda":
            print(mostrar_ayuda())
            
        elif comando == "saludo":
            print(obtener_saludo(NOMBRE_BOT))
            
        elif comando == "recordar":
            respuesta = procesar_comando_recordar(argumento)
            print(respuesta)
            
        elif comando == "tiempo":
            print(calcular_uptime(hora_inicio_programa))
            
        else:
            print(f"❓ Comando '{comando}' no reconocido. Intente con '!ayuda'.")
        
        print("-" * 30)

# Punto de entrada del programa
if __name__ == "__main__":
    iniciar_agente()