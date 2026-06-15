import sys
from pathlib import Path

root = Path(__file__).resolve().parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

import procesador


def ejecutar_comando(comando, *args, **kwargs):
    comando = comando.strip()
    if not hasattr(procesador, comando):
        raise ValueError(f"Comando no encontrado: {comando}")

    funcion = getattr(procesador, comando)
    if not callable(funcion):
        raise ValueError(f"{comando} no es una función ejecutable")

    return funcion(*args, **kwargs)


def procesar_linea(linea):
    partes = linea.strip().split()
    if not partes:
        raise ValueError("Línea vacía")

    comando = partes[0]
    argumentos = []
    for valor in partes[1:]:
        try:
            argumentos.append(int(valor))
        except ValueError:
            try:
                argumentos.append(float(valor))
            except ValueError:
                argumentos.append(valor)

    return ejecutar_comando(comando, *argumentos)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Uso: python agente_procesdor_comandos.py <comando> [args...]")
        sys.exit(1)

    entrada = " ".join(sys.argv[1:])
    try:
        resultado = procesar_linea(entrada)
        if resultado is not None:
            print(resultado)
    except Exception as error:
        print(f"Error: {error}")
