import os

def leer_temperaturas(filename):
    temperaturas = []

    # Leer el archivo y procesar cada línea
    with open(filename, 'r') as file:
        for line in file:
            # Separar la fecha de la temperatura
            fecha, temperatura = line.strip().split(',')
            temperaturas.append(float(temperatura))

    return temperaturas

def calcular_resumen(temperaturas):
    # Calcular temperatura promedio, máxima y mínima
    promedio = sum(temperaturas) / len(temperaturas)
    max_temp = max(temperaturas)
    min_temp = min(temperaturas)

    return promedio, max_temp, min_temp

def escribir_resumen(filename, promedio, max_temp, min_temp):
    with open(filename, 'w') as file:
        file.write(f"Temperatura promedio: {promedio:.2f}\n")
        file.write(f"Temperatura máxima: {max_temp:.2f}\n")
        file.write(f"Temperatura mínima: {min_temp:.2f}\n")

def main():
    # Nombre del archivo de entrada
    archivo_entrada = "temperaturas.txt"
    
    # Nombre del archivo de salida
    archivo_salida = "resumen_temperaturas.txt"
    
    # Leer las temperaturas desde el archivo
    temperaturas = leer_temperaturas(archivo_entrada)

    # Calcular los valores de resumen
    promedio, max_temp, min_temp = calcular_resumen(temperaturas)

    # Escribir los resultados en un nuevo archivo
    escribir_resumen(archivo_salida, promedio, max_temp, min_temp)

    print(f"Resumen de temperaturas escrito en {archivo_salida}")

if __name__ == "__main__":
    main()