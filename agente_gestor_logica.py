import argparse
import ast
import inspect
import importlib


def _eval_literal(value):
    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return value


def _get_module_functions(module):
    return {
        name: func
        for name, func in inspect.getmembers(module, inspect.isfunction)
        if func.__module__ == module.__name__
    }


def _format_signature(func):
    return f"{func.__name__}{inspect.signature(func)}"


def _print_available_commands(functions):
    if not functions:
        print("No se encontraron funciones en agente_logica.py.")
        return
    print("Funciones disponibles en agente_logica.py:")
    for name, func in sorted(functions.items()):
        print(f"  {name}: {_format_signature(func)}")


def main():
    try:
        agente_logica = importlib.import_module('agente_logica')
    except ModuleNotFoundError:
        print('No se pudo importar el módulo agente_logica. Asegúrate de que exista en el mismo directorio.')
        return

    functions = _get_module_functions(agente_logica)

    parser = argparse.ArgumentParser(
        description='Llama a las funciones definidas en agente_logica.py mediante comandos.'
    )
    parser.add_argument('command', nargs='?', help='Nombre de la función a ejecutar, o "list" para ver las funciones disponibles.')
    parser.add_argument('params', nargs='*', help='Argumentos posicionales o argumentos clave=valor para la función.')
    args = parser.parse_args()

    if not args.command or args.command in {'list', 'help'}:
        _print_available_commands(functions)
        return

    command = args.command
    if command not in functions:
        print(f'Comando no encontrado: {command}')
        _print_available_commands(functions)
        return

    func = functions[command]
    positional_args = []
    keyword_args = {}

    for param in args.params:
        if '=' in param:
            key, value = param.split('=', 1)
            keyword_args[key] = _eval_literal(value)
        else:
            positional_args.append(_eval_literal(param))

    try:
        result = func(*positional_args, **keyword_args)
        if result is not None:
            print(result)
    except TypeError as error:
        print(f'Error al llamar a {command}: {error}')


if __name__ == '__main__':
    main()
