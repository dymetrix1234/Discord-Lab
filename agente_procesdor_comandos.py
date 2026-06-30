import discord
import os
from dotenv import load_dotenv
from agente_gestor_logica import analizar_comando

ruta_script = os.path.dirname(os.path.abspath(__file__))
ruta_env = os.path.join(ruta_script, '.env')
load_dotenv(dotenv_path=ruta_env)

TOKEN = os.getenv('DISCORD_TOKEN')

def mostrar_bienvenida():
    return (
        "📜 **Bot de Operaciones y Lógica V2 (Modo Estructurado)**\n"
        "📜 Primeros pasos Agente Discord UX:\n"
        "📜 Escriba `!Exit` para salir del Agente.\n"
        "📜 Escriba `!Inicio` para mostrar esta bienvenida nuevamente.\n\n"
        "⌨️ **Contrato de Comandos Disponibles:**\n"
        "• `!validar_identificador [variable]` - Reglas de nombrado PEP 8\n"
        "• `!evaluar_operadores [expresion]` - Cortocircuito y tablas de verdad\n"
        "• `!diagnosticar_tipado [valor]` - Análisis de tipado dinámico\n"
        "• `!evaluar_for [codigo]` - Validación estructural con AST\n"
        "• `!monitorear_while [limite]` - Traza de control de bucles\n"
        "• `!analizar_if [codigo]` - Jerarquía de indentación\n"
        "• `!analizar_mutabilidad [estructura] [accion]` - Análisis de referencias\n"
        "• `!gestionar_diccionario [clave] [valor]` - Reglas hash e inmutabilidad\n"
        "• `!demostrar_slicing [inicio] [fin]` - Rebanado de secuencias\n"
        "• `!simular_defensivo [tipo_error]` - Flujos try-except\n"
        "• `!explicar_bloque` - Diagramación de orden completo de excepciones\n"
        "• `!validar_propagacion [codigo]` - Simulación del stack trace\n"
        "• `!historial` - Consulta los últimos 5 comandos de la sesión\n"
    )

def main(entrada):
    PREFIJO = "!"
    if not entrada.startswith(PREFIJO):
        if entrada: 
            print("Recuerda usar '!' para comandos.")
            return "Recuerda usar '!' para comandos."

    cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
    comando = cuerpo[0].lower()

    if comando == "exit":
        print("Saliendo del gestor...")
        return "Saliendo del gestor..."
    elif comando == "inicio":
        print(mostrar_bienvenida())
        return mostrar_bienvenida()
    else:
        resultado = analizar_comando(entrada)
        print(f"Resultado del procesamiento: {resultado}")
        return resultado

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Sincronizado como {client.user} (ID: {client.user.id})')
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f"Mensaje recibido de {message.author}: {message.content}")

    if message.content.startswith('!'):
        resultado = main(message.content)
        print(f"Resultado enviado a Discord: {resultado}")
        await message.channel.send(f"**Bot Procesador:**\n{resultado}")

if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print(f"ERROR: No se encontró el TOKEN en la ruta: {ruta_env}")