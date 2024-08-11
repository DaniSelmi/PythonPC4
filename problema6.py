def contar_lineas_codigo(filepath):
    # Verificar que el archivo tiene la extensión .py
    if not filepath.endswith(".py"):
        print("El archivo no es un archivo .py.")
        return
    
    try:
        with open(filepath, 'r') as file:
            lineas_codigo = 0

            for linea in file.readlines():
                linea_strip = linea.strip()

                # Ignorar líneas en blanco y comentarios
                if linea_strip and not linea_strip.startswith("#"):
                    lineas_codigo += 1

        print(f"El archivo '{filepath}' tiene {lineas_codigo} líneas de código.")
    
    except FileNotFoundError:
        print("El archivo no fue encontrado. Verifique la ruta.")

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta_archivo)

if __name__ == "__main__":
    main()