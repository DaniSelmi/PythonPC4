import random
pip install pyfiglet
from pyfiglet import Figlet

def main():
    # Crear una instancia de Figlet
    figlet = Figlet()

    # Solicitar al usuario el nombre de una fuente
    fuente_seleccionada = input("Ingrese el nombre de una fuente (o presione Enter para seleccionar una aleatoria): ")

    # Si no se ingresa ninguna fuente, se selecciona una de forma aleatoria
    if not fuente_seleccionada:
        fuente_seleccionada = random.choice(figlet.getFonts())
        print(f"Fuente aleatoria seleccionada: {fuente_seleccionada}")
    
    # Establecer la fuente seleccionada
    try:
        figlet.setFont(font=fuente_seleccionada)
    except:
        print(f"Fuente '{fuente_seleccionada}' no encontrada. Se utilizará una fuente aleatoria.")
        fuente_seleccionada = random.choice(figlet.getFonts())
        figlet.setFont(font=fuente_seleccionada)
        print(f"Fuente aleatoria seleccionada: {fuente_seleccionada}")

    # Solicitar al usuario un texto
    texto_imprimir = input("Ingrese el texto a imprimir: ")

    # Imprimir el texto usando la fuente seleccionada
    print(figlet.renderText(texto_imprimir))

if __name__ == "__main__":
    main()