pip install requests sqlite3 pymongo

import requests
import sqlite3
from pymongo import MongoClient

# URL de la API
url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"

# Crear conexión con SQLite
sqlite_conn = sqlite3.connect('base.db')
cursor = sqlite_conn.cursor()

# Crear tabla sunat_info si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS sunat_info (
    fecha TEXT PRIMARY KEY,
    compra REAL,
    venta REAL
)
''')

# Crear conexión con MongoDB
mongo_client = MongoClient('localhost', 27017)
mongo_db = mongo_client['sunat_db']
mongo_collection = mongo_db['sunat_info']

# Obtener y almacenar datos
for month in range(1, 13):
    for day in range(1, 32):
        try:
            # Formatear la fecha
            date = f"2023-{month:02d}-{day:02d}"
            
            # Realizar la solicitud GET
            response = requests.get(url, params={"fecha": date})
            data = response.json()
            
            # Verificar si la respuesta tiene datos válidos
            if 'compra' in data and 'venta' in data:
                compra = data['compra']
                venta = data['venta']
                
                # Insertar en SQLite
                cursor.execute('''
                    INSERT OR REPLACE INTO sunat_info (fecha, compra, venta)
                    VALUES (?, ?, ?)
                ''', (date, compra, venta))
                
                # Insertar en MongoDB
                mongo_collection.update_one(
                    {"fecha": date},
                    {"$set": {"compra": compra, "venta": venta}},
                    upsert=True
                )
        except Exception as e:
            print(f"Error al procesar la fecha {date}: {e}")

# Guardar cambios en SQLite
sqlite_conn.commit()

# Cerrar conexiones
cursor.close()
sqlite_conn.close()
mongo_client.close()

print("Datos almacenados correctamente en SQLite y MongoDB.")

import sqlite3

def mostrar_datos_sqlite():
    # Conectar a la base de datos SQLite
    sqlite_conn = sqlite3.connect('base.db')
    cursor = sqlite_conn.cursor()

    # Obtener todos los registros de la tabla sunat_info
    cursor.execute("SELECT * FROM sunat_info")
    registros = cursor.fetchall()

    # Mostrar los registros
    for registro in registros:
        print(f"Fecha: {registro[0]}, Compra: {registro[1]}, Venta: {registro[2]}")

    # Cerrar conexión
    cursor.close()
    sqlite_conn.close()

mostrar_datos_sqlite()