# producto,fecha,cantidad,precio
# producto1,2023-01-01,2,100
# producto2,2023-01-02,1,200

import csv
import sqlite3
from pymongo import MongoClient

def obtener_tipo_cambio(fecha, db_type='sqlite'):
    if db_type == 'sqlite':
        # Conectar a la base de datos SQLite
        sqlite_conn = sqlite3.connect('base.db')
        cursor = sqlite_conn.cursor()
        
        # Consultar el tipo de cambio de la fecha proporcionada
        cursor.execute("SELECT compra FROM sunat_info WHERE fecha = ?", (fecha,))
        resultado = cursor.fetchone()
        
        cursor.close()
        sqlite_conn.close()
        
    elif db_type == 'mongodb':
        # Conectar a MongoDB
        mongo_client = MongoClient('localhost', 27017)
        mongo_db = mongo_client['sunat_db']
        mongo_collection = mongo_db['sunat_info']
        
        # Consultar el tipo de cambio de la fecha proporcionada
        resultado = mongo_collection.find_one({"fecha": fecha}, {"compra": 1})
        
        mongo_client.close()

    return resultado[0] if resultado else None

def procesar_ventas(filename, db_type='sqlite'):
    with open(filename, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        print(f"{'Producto':<15} {'Fecha':<15} {'Cantidad':<10} {'Precio (USD)':<15} {'Precio (S/.)':<15}")
        print("=" * 70)

        for row in reader:
            producto = row['producto']
            fecha = row['fecha']
            cantidad = int(row['cantidad'])
            precio_usd = float(row['precio'])
            precio_total_usd = cantidad * precio_usd
            
            # Obtener el tipo de cambio de la fecha
            tipo_cambio = obtener_tipo_cambio(fecha, db_type)
            
            if tipo_cambio is not None:
                precio_total_sol = precio_total_usd * tipo_cambio
                print(f"{producto:<15} {fecha:<15} {cantidad:<10} {precio_total_usd:<15.2f} {precio_total_sol:<15.2f}")
            else:
                print(f"Tipo de cambio no encontrado para la fecha {fecha}.")

if __name__ == "__main__":
    # Especifica el nombre del archivo y el tipo de base de datos a utilizar
    procesar_ventas('ventas.csv', db_type='sqlite')  # Cambia a 'mongodb' si deseas usar MongoDB