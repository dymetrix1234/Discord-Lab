import ast
import inspect
import importlib
import os
import sys


def load_tareas_module():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
    return importlib.import_module("tareas_agente")


def get_functions(module):
    return {
        name: func
        for name, func in inspect.getmembers(module, inspect.isfunction)
        if func.__module__ == module.__name__ and not name.startswith("_")
    }


def parse_arguments(args):
    parsed = []
    for arg in args:
        try:
            parsed.append(ast.literal_eval(arg))
        except (ValueError, SyntaxError):
            parsed.append(arg)
    return parsed


def print_help(functions):
    print("Comandos disponibles:")
    print("  list                - Lista las funciones disponibles en tareas_agente")
    print("  help                - Muestra esta ayuda")
    print("  exit                - Sale del procesador")
    print("  <funcion> [args...] - Llama a la funcion de tareas_agente con argumentos opcionales")
    print("\nFunciones disponibles:")
    for name, func in sorted(functions.items()):
        signature = str(inspect.signature(func))
        print(f"  {name}{signature}")


def execute_command(functions, command, args):
    if command == "list":
        print("Funciones disponibles:")
        for name in sorted(functions):
            print(f"  {name}")
        return
    if command == "help":
        print_help(functions)
        return
    if command == "exit":
        sys.exit(0)
    if command not in functions:
        print(f"Funcion no encontrada: {command}")
        return
    func = functions[command]
    parsed_args = parse_arguments(args)
    try:
        result = func(*parsed_args)
        if result is not None:
            print(result)
    except Exception as err:
        print(f"Error al ejecutar {command}: {err}")


def main():
    try:
        module = load_tareas_module()
    except ModuleNotFoundError:
        print("No se encontro el modulo tareas_agente. Asegurese de que el archivo tareas_agente.py este en el mismo directorio.")
        return
    functions = get_functions(module)
    if len(sys.argv) > 1:
        command = sys.argv[1]
        args = sys.argv[2:]
        execute_command(functions, command, args)
        return

    print("Procesador de tareas cargado. Escriba 'help' para ver los comandos.")
    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break
        if not line:
            continue
        parts = line.split()
        execute_command(functions, parts[0], parts[1:])


if __name__ == "__main__":
    main()
