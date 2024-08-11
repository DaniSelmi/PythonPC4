import requests

# URL de la imagen
url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# Descargar la imagen
response = requests.get(url)

# Guardar la imagen en un archivo
image_filename = "imagen_descargada.jpg"
with open(image_filename, "wb") as file:
    file.write(response.content)

print(f"Imagen descargada y guardada como {image_filename}")


#Comprimir la imagen en un archivo ZIP
import zipfile

# Nombre del archivo ZIP
zip_filename = "imagen_comprimida.zip"

# Crear un archivo ZIP y agregar la imagen
with zipfile.ZipFile(zip_filename, "w") as zipf:
    zipf.write(image_filename)

print(f"Imagen comprimida y guardada como {zip_filename}")


# Extraer el archivo ZIP
with zipfile.ZipFile(zip_filename, "r") as zipf:
    zipf.extractall(".")

print(f"Imagen extraída del archivo ZIP y guardada en el directorio actual.")