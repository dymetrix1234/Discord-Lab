import keyword
import re
import ast

historial_comandos = []

def registrar_en_historial(comando: str):
    if len(historial_comandos) >= 5:
        historial_comandos.pop(0)
    historial_comandos.append(comando)

def obtener_historial_formateado() -> str:
    if not historial_comandos:
        return "No hay registros en el historial de comandos de esta sesión."
    res = "📋 **Últimos comandos registrados en el historial:**\n"
    for i, cmd in enumerate(historial_comandos, 1):
        res += f"{i}. `!{cmd}`\n"
    return res

def validar_identificador(nombre_variable: str) -> str:
    nombre_variable = nombre_variable.strip()
    if not nombre_variable:
        return "⚠️ Error: Debes proporcionar un nombre de identificador."
    if keyword.iskeyword(nombre_variable):
        return f"❌ '{nombre_variable}' es una palabra reservada de Python y no puede usarse como identificador bajo PEP 8."
    if nombre_variable[0].isdigit():
        return f"❌ '{nombre_variable}' es inválido. Un identificador no puede comenzar con un número."
    if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', nombre_variable):
        return f"❌ '{nombre_variable}' contiene caracteres no permitidos. Solo se admiten letras, números y guiones bajos."
    return f"✅ '{nombre_variable}' cumple con el estándar PEP 8 y es un identificador válido."

def evaluar_operadores_logicos(expresion: str) -> str:
    expresion = expresion.strip()
    if not expresion:
        return "⚠️ Error: Proporciona una expresión lógica. Ejemplo: !evaluar_operadores True and False"
    try:
        arbol = ast.parse(expresion, mode='eval')
        for nodo in ast.walk(arbol):
            if isinstance(nodo, (ast.BitAnd, ast.BitOr, ast.BitXor, ast.Invert)):
                return "❌ Error Pedagógico: Has utilizado operadores de bits (&, |, ~). En Python, para lógica condicional debes usar 'and', 'or' y 'not'."
        
        resultado = eval(expresion, {"__builtins__": None}, {"True": True, "False": False})
        explicacion = f"🔍 **Diagnóstico del Cortocircuito Lógico:**\n"
        explicacion += f"Expresión evaluada: `{expresion}`\n"
        explicacion += f"Resultado Booleano Final: **{resultado}**\n\n"
        explicacion += "💡 *Recuerda:* Python evalúa de izquierda a derecha. En un bloque 'and', si el primer elemento es False, no evalúa el resto. En un bloque 'or', si el primero es True, frena la evaluación inmediatamente."
        return explicacion
    except Exception:
        return "❌ Error: Expresión inválida. Usa valores booleanos nativos como 'True and False'."

def diagnosticar_tipado_dinámico(valor_entrada: str) -> str:
    valor_entrada = valor_entrada.strip()
    if not valor_entrada:
        return "⚠️ Error: Envía un valor para diagnosticar."
    try:
        objeto = ast.literal_eval(valor_entrada)
    except Exception:
        objeto = valor_entrada

    tipo = type(objeto).__name__
    reporte = f"📝 **Análisis de Tipado Dinámico:**\n"
    reporte += f"El valor introducido fue interpretado como el tipo: `<class '{tipo}'>`.\n\n"
    reporte += "💡 **Ejemplos didácticos para este tipo de dato:**\n"
    if tipo == "str":
        reporte += "✅ Válido: Concatenar con otro texto (`\"Hola\" + \" Mundo\"`)\n"
        reporte += "❌ Inválido: Sumar directamente con enteros (`\"Texto\" + 5`) -> Lanza TypeError."
    elif tipo in ["int", "float"]:
        reporte += f"✅ Válido: Operaciones matemáticas directas (`{objeto} + 10`)\n"
        reporte += f"❌ Inválido: Intentar iterar sobre él (`for i in {objeto}:`) -> Lanza TypeError."
    elif tipo == "bool":
        reporte += "✅ Válido: Evaluaciones lógicas e inversión de estado (`not True`)\n"
        reporte += "❌ Inválido: Modificar sus elementos internos por índice."
    else:
        reporte += "Este tipo de dato nativo mantiene un comportamiento de tipado fuerte."
    return reporte

def evaluar_ciclo_for(codigo_alumno: str) -> str:
    if not codigo_alumno:
        return "⚠️ Error: Envía un fragmento de código con estructura de ciclo for."
    try:
        arbol = ast.parse(codigo_alumno)
        for nodo in ast.walk(arbol):
            if isinstance(nodo, ast.For):
                if isinstance(nodo.iter, ast.Call) and getattr(nodo.iter.func, 'id', '') == 'range':
                    return "✅ Validación Estructural (AST) Exitosa: El ciclo 'for' implementa de manera correcta la palabra clave 'in' y el generador 'range()'."
                return "⚠️ Alerta Sintáctica: Se detectó un ciclo 'for', pero no está utilizando la función generadora 'range()' para delimitar las iteraciones numéricas."
        return "❌ Error: No se localizó ninguna estructura válida de ciclo 'for' de Python en tu código."
    except SyntaxError as e:
        return f"❌ Alerta de Error Sintáctico: Tu código tiene fallas de escritura o problemas de indentación jerárquica.\nDetalle: Línea {e.lineno}, Error: {e.msg}"

def monitorear_ciclo_while(limite: str) -> str:
    if not limite.isdigit():
        return "⚠️ Error: Debes ingresar un número entero válido como límite de iteraciones simuladas."
    veces = int(limite)
    if veces > 10:
        return "⚠️ Simulación abortada: El límite máximo permitido de simulación es de 10 iteraciones para mitigar riesgos de bucles infinitos."
        
    traza = "🖥️ **Traza de Ejecución Controlada (Ciclo While Simulado):**\n"
    contador = 0
    while contador < veces:
        traza += f" `[Iteración {contador + 1}]` Contador = {contador} | Condición ({contador} < {veces}) -> True\n"
        contador += 1
    traza += f"🏁 `[Fin del Ciclo]` Contador final = {contador} | Condición ({contador} < {veces}) -> False. Bucle finalizado limpiamente."
    return traza

def analizar_condicionales_anidados(codigo_if: str) -> str:
    if not codigo_if:
        return "⚠️ Error: Proporciona un bloque de condicionales para mapear."
    try:
        arbol = ast.parse(codigo_if)
        nodos_if = [nodo for nodo in ast.walk(arbol) if isinstance(nodo, ast.If)]
        if not nodos_if:
            return "❌ Error: No se localizó la estructura de un condicional 'if'."
            
        guia = "🗺️ **Mapeo Jerárquico de Flujo Lógico:**\n"
        guia += f"Se detectaron {len(nodos_if)} ramificaciones lógicas condicionales.\n"
        guia += "Estructura correcta validada:\n"
        if "elif" in codigo_if:
            guia += "🔹 Mapeo Lógico: El bloque incorpora subcondiciones encadenadas mediante la sintaxis 'elif'.\n"
        else:
            guia += "🔹 Mapeo Lógico: Bloque condicional plano o anidamiento directo.\n"
        guia += "💡 *Nota Pedagógica:* Recuerda que la sangría (indentación) determina con precisión qué acciones dependen de cada cumplimiento relacional."
        return guia
    except SyntaxError as e:
        return f"❌ Error de Indentación/Sintaxis: No se pudo generar la estructura visual del árbol.\nDetalle: Línea {e.lineno}: {e.msg}"

def analizar_mutabilidad_coleccion(tipo_estructura: str, operacion: str) -> str:
    tipo_estructura = tipo_estructura.lower().strip()
    operacion = operacion.lower().strip()
    if tipo_estructura not in ["lista", "tupla", "diccionario"]:
        return "⚠️ Error: Las estructuras válidas para análisis son: 'lista', 'tupla' o 'diccionario'."
        
    reporte = f"🧠 **Diagnóstico de Mutabilidad de Objetos y Gestión de Referencias:**\n"
    if tipo_estructura == "tupla":
        reporte += "Tipo: **Tupla (Inmutable)**\n"
        reporte += f"Intento de acción: `{operacion}`\n\n"
        reporte += "❌ **Comportamiento en Memoria:** Las tuplas rechazan la asignación o mutación por índice de manera estricta. "
        reporte += "Si intentas alterar sus elementos, Python arrojará un `TypeError` ya que la dirección de memoria de la estructura es fija y protegida."
    else:
        reporte += f"Tipo: **{tipo_estructura.capitalize()} (Mutable)**\n"
        reporte += f"Intento de acción: `{operacion}`\n\n"
        reporte += "✅ **Comportamiento en Memoria:** Al ejecutar mutaciones como `.append()` en listas o asignaciones de claves en diccionarios, "
        reporte += "la operación se realiza **in-place**. Esto significa que el objeto se modifica conservando exactamente su misma dirección de memoria (ID base invariable)."
    return reporte

def gestionar_diccionario_estudiante(clave: str, valor: str) -> str:
    clave = clave.strip()
    valor = valor.strip()
    if not clave or not valor:
        return "⚠️ Uso correcto: !gestionar_diccionario [clave] [valor]"
    if (clave.startswith('[') and clave.endswith(']')) or (clave.startswith('{') and clave.endswith('}')):
        reporte_error = "❌ **Fallo de Inmutabilidad en Clave detectado (TypeError Simulado):**\n"
        reporte_error += f"Intentaste insertar una estructura mutable como clave: `{clave}`.\n"
        reporte_error += "💡 **Anatomía de Diccionarios en Python:** Las claves en memoria deben ser objetos inmutables y transformables en un índice único (**hashables**), tales como cadenas, enteros o tuplas. Las listas y diccionarios no son permitidos."
        return reporte_error
    return f"✅ **Inserción Exitosa en Diccionario Simulado:**\nSe almacenó el par asociativo: `{{{clave}: {valor}}}` de manera correcta en el espacio hash."

def demostrar_slicing_listas(inicio_str: str, fin_str: str) -> str:
    lista_base = ["Python", "Java", "C++", "JavaScript", "Go", "Rust"]
    try:
        inicio = int(inicio_str) if inicio_str else 0
        fin = int(fin_str) if fin_str else len(lista_base)
    except ValueError:
        return "⚠️ Error: Los límites del rebanado (slicing) deben ser números enteros o dejarse vacíos."
        
    subcoleccion = lista_base[inicio:fin]
    markdown = "✂️ **Demostración de Rebanado (Slicing) de Secuencias:**\n"
    markdown += f"Lista Original completa: `{lista_base}`\n"
    markdown += f"Sintaxis empleada en los índices: `[ {inicio_str if inicio_str else ''} : {fin_str if fin_str else ''} ]`\n\n"
    markdown += f"📦 **Subcolección Extraída:**\n```python\n{subcoleccion}\n```\n"
    markdown += "💡 *Concepto:* Los índices negativos cuentan desde el final hacia atrás, y omitir un límite superior toma la secuencia hasta el extremo libre."
    return markdown

def simular_flujo_defensivo(tipo_error: str) -> str:
    tipo_error = tipo_error.strip()
    errors_disponibles = {
        "ZeroDivisionError": lambda: 1 / 0,
        "ValueError": lambda: int("TextoInvalido"),
        "TypeError": lambda: "texto" + 5
    }
    if tipo_error not in errors_disponibles:
        return f"⚠️ Error: Elige un tipo de error válido para simular: {list(errors_disponibles.keys())}"
        
    guia = f"🛡️ **Simulación de Programación Defensiva (Bloque Try-Except):**\n"
    try:
        guia += f"1. Provocando intencionalmente el fallo de tipo `{tipo_error}` mediante la palabra clave `raise`...\n"
        errors_disponibles[tipo_error]()
    except Exception as e:
        guia += f"2. 🛑 **Excepción Interceptada Exitosamente:** El motor de Python capturó un `{type(e).__name__}`.\n"
        guia += f"3. Salida limpia al usuario: *\"Error de entrada: Por favor verifica tus operaciones matemáticas o formatos.\"*\n\n"
        guia += "✅ El script continuó su ciclo de vida en el servidor sin detenerse de forma abrupta."
        return guia

def explicar_bloque_completo_excepciones() -> str:
    guia = "⚙️ **Guía Visual Avanzada de Tolerancia a Fallos (Try-Except-Else-Finally):**\n\n"
    guia += "🟢 **Flujo 1: Ejecución Limpia (Sin Excepciones)**\n"
    guia += " ↳ `try:` Se ejecuta el bloque inicial de código.\n"
    guia += " ↳ `else:` ¡Se ejecuta este bloque! Ya que no ocurrió ningún error intermedio.\n"
    guia += " ↳ `finally:` Se ejecuta este bloque de limpieza pase lo que pase al final.\n\n"
    guia += "🔴 **Flujo 2: Ejecución Defectuosa (Con Excepciones)**\n"
    guia += " ↳ `try:` Se interrumpe la ejecución al detectar un fallo.\n"
    guia += " ↳ `except:` Intercepta el problema y desvía la emergencia.\n"
    guia += " ↳ `else:` Omitido por completo debido a la presencia de fallos.\n"
    guia += " ↳ `finally:` Se ejecuta este bloque obligatoriamente para cerrar recursos en memoria."
    return guia

def validar_propagacion_errores(codigo_try: str) -> str:
    codigo_try = codigo_try.strip()
    if not codigo_try:
        return "⚠️ Error: Proporciona un caso de estudio de código para evaluar la propagación de la pila."
        
    mapa = "🥞 **Simulación de Stack Trace y Propagación de Excepciones:**\n"
    mapa += "Al originarse una excepción dentro de funciones anidadas:\n"
    mapa += " `[Contexto Local: funcion_interna()]` Lanza una excepción en memoria.\n"
    mapa += "   ↓ Contexto destruido (Las variables locales se liberan de la memoria).\n"
    mapa += " `[Contexto Superior: funcion_padre()]` Recibe la excepción propagada hacia arriba.\n"
    if "except" in codigo_try:
        mapa += "   ↓ 🎉 El bloque `except` interceptó la excepción en la capa superior. Propagación contenida con éxito."
    else:
        mapa += "   ↓ 💥 Fuga de Excepción: La burbuja rompió el entorno local y escaló al sistema principal causando un desplome."
    return mapa

def analizar_comando(entrada):
    mensaje = entrada.strip()
    if mensaje.startswith("!"):
        partes = mensaje.split(" ", 1)
        comando = partes[0].lower()
        argumento = partes[1].strip() if len(partes) > 1 else ""

        if comando == "!validar_identificador":
            registrar_en_historial("validar_identificador")
            return validar_identificador(argumento)
        elif comando == "!evaluar_operadores":
            registrar_en_historial("evaluar_operadores")
            return evaluar_operadores_logicos(argumento)
        elif comando == "!diagnosticar_tipado":
            registrar_en_historial("diagnosticar_tipado")
            return diagnosticar_tipado_dinámico(argumento)
        elif comando == "!evaluar_for":
            registrar_en_historial("evaluar_for")
            return evaluar_ciclo_for(argumento)
        elif comando == "!monitorear_while":
            registrar_en_historial("monitorear_while")
            return monitorear_ciclo_while(argumento)
        elif comando == "!analizar_if":
            registrar_en_historial("analizar_if")
            return analizar_condicionales_anidados(argumento)
        elif comando == "!analizar_mutabilidad":
            registrar_en_historial("analizar_mutabilidad")
            args = argumento.split(maxsplit=1)
            est = args[0] if len(args) > 0 else ""
            acc = args[1] if len(args) > 1 else ""
            return analizar_mutabilidad_coleccion(est, acc)
        elif comando == "!gestionar_diccionario":
            registrar_en_historial("gestionar_diccionario")
            args = argumento.split(maxsplit=1)
            clv = args[0] if len(args) > 0 else ""
            val = args[1] if len(args) > 1 else ""
            return gestionar_diccionario_estudiante(clv, val)
        elif comando == "!demostrar_slicing":
            registrar_en_historial("demostrar_slicing")
            args = argumento.split(maxsplit=1)
            ini = args[0] if len(args) > 0 else ""
            fin = args[1] if len(args) > 1 else ""
            return demostrar_slicing_listas(ini, fin)
        elif comando == "!simular_defensivo":
            registrar_en_historial("simular_defensivo")
            return simular_flujo_defensivo(argumento)
        elif comando == "!explicar_bloque":
            registrar_en_historial("explicar_bloque")
            return explicar_bloque_completo_excepciones()
        elif comando == "!validar_propagacion":
            registrar_en_historial("validar_propagacion")
            return validar_propagacion_errores(argumento)
        elif comando == "!historial":
            return obtener_historial_formateado()
        elif comando == "!ayuda":
            return ("Comandos disponibles:\n"
                    "!validar_identificador [variable] - Reglas de nombrado PEP 8\n"
                    "!evaluar_operadores [expresion] - Cortocircuito y tablas de verdad\n"
                    "!diagnosticar_tipado [valor] - Análisis de tipado dinámico\n"
                    "!evaluar_for [codigo] - Validación estructural con AST\n"
                    "!monitorear_while [limite] - Traza de control de bucles\n"
                    "!analizar_if [codigo] - Jerarquía de indentación\n"
                    "!analizar_mutabilidad [estructura] [accion] - Análisis de referencias\n"
                    "!gestionar_diccionario [clave] [valor] - Reglas hash e inmutabilidad\n"
                    "!demostrar_slicing [inicio] [fin] - Rebanado de secuencias\n"
                    "!simular_defensivo [tipo_error] - Flujos try-except\n"
                    "!explicar_bloque - Diagramación de orden completo de excepciones\n"
                    "!validar_propagacion [codigo] - Simulación del stack trace\n"
                    "!historial - Muestra los últimos 5 comandos usados")
        else:
            return "Comando no reconocido. Escribe !ayuda para ver los comandos disponibles."
            
    return "Recuerda que los comandos deben comenzar con '!'. Escribe !ayuda para ver los comandos disponibles."

if __name__ == "__main__":
    print("--- Agente de Lógica Avanzado: Modo de Consola Local ---")
    print("Prueba comandos del contrato como: !validar_identificador mi_variable o !monitorear_while 5\n")
    while True:
        user_input = input("Alumno >> ")
        if user_input.lower() in ["salir", "exit"]: 
            break
        respuesta = analizar_comando(user_input)
        print(f"Bot >> {respuesta}\n")