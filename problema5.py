import os

class TablaMultiplicar:
    def __init__(self, numero):
        self.numero = numero
        self.filename = f"tabla-{self.numero}.txt"

    def crear_tabla(self):
        with open(self.filename, 'w') as file:
            for i in range(1, 11):
                file.write(f"{self.numero} x {i} = {self.numero * i}\n")
        print(f"Tabla de multiplicar del {self.numero} guardada en {self.filename}")

    def leer_tabla(self):
        try:
            with open(self.filename, 'r') as file:
                contenido = file.read()
            print(f"Contenido de {self.filename}:\n{contenido}")
        except FileNotFoundError:
            print(f"El archivo {self.filename} no existe.")

    def leer_linea_tabla(self, linea):
        try:
            with open(self.filename, 'r') as file:
                lineas = file.readlines()
                if 1 <= linea <= len(lineas):
                print(f"Línea {linea} de {self.filename}: {lineas[linea - 1].strip()}")
            else:
                print(f"La línea {linea} no existe en {self.filename}.")
        except FileNotFoundError:
            print(f"El archivo {self.filename} no existe.")


def solicitar_numero(mensaje, rango_min=1, rango_max=10):
    while True:
        try:
            numero = int(input(mensaje))
            if rango_min <= numero <= rango_max:
                return numero
            else:
                print(f"Por favor, ingrese un número entre {rango_min} y {rango_max}.")
        except ValueError:
            print("Debe ingresar un número entero válido.")

def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Crear una tabla de multiplicar")
    print("2. Leer una tabla de multiplicar")
    print("3. Leer una línea específica de una tabla de multiplicar")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = solicitar_numero("Ingrese una opción (1-4): ", 1, 4)

        if opcion == 1:
            numero = solicitar_numero("Ingrese un número entre 1 y 10: ")
            tabla = TablaMultiplicar(numero)
            tabla.crear_tabla()

        elif opcion == 2:
            numero = solicitar_numero("Ingrese un número entre 1 y 10: ")
            tabla = TablaMultiplicar(numero)
            tabla.leer_tabla()

        elif opcion == 3:
            numero = solicitar_numero("Ingrese un número entre 1 y 10: ")
            linea = solicitar_numero("Ingrese el número de línea que desea leer (1-10): ")
            tabla = TablaMultiplicar(numero)
            tabla.leer_linea_tabla(linea)

        elif opcion == 4:
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()