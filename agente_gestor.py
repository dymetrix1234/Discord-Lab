import os
import sys
import shlex

from Practica02 import gestor_comandos

this_dir = os.path.dirname(os.path.abspath(__file__))
if this_dir not in sys.path:
    sys.path.insert(0, this_dir)

try:
    import gestor_comandos
except ImportError as error:
    raise ImportError(f"No se pudo importar gestor_comandos: {error}") from error


def obtener_comandos_disponibles():
    comandos = []
    for nombre in dir(gestor_comandos):
        if nombre.startswith("_"):
            continue
        valor = getattr(gestor_comandos, nombre)
        if callable(valor):
            comandos.append(nombre)
    return sorted(comandos)


def ejecutar_comando(comando, *args):
    if comando in {"listar", "ayuda", "help"}:
        return "\n".join(obtener_comandos_disponibles())

    funcion = getattr(gestor_comandos, comando, None)
    if not callable(funcion):
        raise ValueError(f"Comando desconocido: {comando}")

    return funcion(*args)


def imprimir_ayuda():
    comandos = obtener_comandos_disponibles()
    mensaje = [
        "Comandos disponibles:",
        *[f" - {c}" for c in comandos],
        "Escriba 'salir' para terminar.",
    ]
    print("\n".join(mensaje))


def ejecutar_desde_linea_comandos(argv=None):
    argv = argv if argv is not None else sys.argv
    if len(argv) > 1:
        comando = argv[1]
        args = argv[2:]
        resultado = ejecutar_comando(comando, *args)
        if resultado is not None:
            print(resultado)
        return

    imprimir_ayuda()
    while True:
        try:
            entrada = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not entrada:
            continue
        if entrada.lower() in {"salir", "exit", "quit"}:
            break

        partes = shlex.split(entrada)
        comando = partes[0]
        args = partes[1:]
        try:
            resultado = ejecutar_comando(comando, *args)
            if resultado is not None:
                print(resultado)
        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    ejecutar_desde_linea_comandos()
